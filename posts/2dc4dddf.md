<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.site/pc?spm={{spm}})

## 现有方案的痛点

市面上 Changelog 生成工具不少，`conventional-changelog`、`git-changelog`、`release-drafter` 都能用，但它们有一个共同前提：**团队得严格遵守约定式提交规范**。实际项目里，`fix bug`、`update`、`修复了问题` 这种提交满地都是，你没法指望所有人都按规范写。这些工具拿到这种"垃圾进"，只能给你"垃圾出"。

那用 AI 呢？比如把 Git Log 复制到 ChatGPT 或者让 Cursor 帮忙整理，确实能生成不错的内容。但问题是：

- **token 浪费严重**：现在的 AI 工具都是大而全的 Agent，接入大量 MCP 和 Skill，你只是想让它整理几条提交记录，它也要加载一堆上下文，消耗的 token 远超实际需要
- **批量场景撑不住**：想为整个项目的提交历史批量生成 Changelog？几次就报上下文超长，得手动切分范围重来
- **流程割裂**：IDE 里选中提交 → 复制 → 切到外部工具 → 粘贴 → 等结果 → 复制回来，每次都要中断开发流程
- **提交信息本身的困境**：不只是整理历史记录痛苦，写 commit message 也一样——改了一堆文件，不知道怎么一句话说清楚

而这个场景的 AI 调用其实非常简单：**输入是选中的提交记录（或者代码 diff），输出是格式化的文本**，一轮问答就够了。不需要 Agent 思考，不需要调工具，不需要长上下文。用最原始的"你问我答"模式，token 消耗比通用 AI 工具少一个数量级。

所以我的思路是：**把这种极简的 AI 调用直接嵌到 IDE 里**，选中 Git 提交 → 右键 → 一键生成，不需要离开 IntelliJ IDEA，不多消耗一个 token。

## 功能一览

插件提供四个核心功能：

| 功能 | 入口 | 说明 |
|------|------|------|
| 生成 Changelog | Git Log 右键菜单 | 基于选中的提交记录，生成版本更新日志 |
| 生成日报 | Git Log 右键菜单 | 基于当天的提交记录生成工作日报 |
| 生成周报 | Git Log 右键菜单 | 汇总一周提交生成团队周报 |
| 生成提交信息 | Git 提交页面工具栏 | 基于代码 diff 生成规范的 commit message |

所有生成都走 AI，支持 OpenAI、Anthropic、Ollama 等多种后端，通过 [IntelliAI Engine](https://github.com/dong4j/zeka-stack/tree/main/intelli-ai-engine) 统一调用。

## 和其他方案比，好在哪

核心差异就一句话：**这是一个轻量级的专用 AI 插件，而不是一个通用 AI Agent**。

**vs 传统 Changelog 工具**（conventional-changelog、release-drafter 等）：
- 不依赖提交规范。就算团队的提交记录是 `fix bug`、`update`，AI 也能基于 diff 和上下文理解实际改了什么
- 不只是格式化，是真的"理解"代码变更，生成有意义的描述

**vs 通用 AI 工具**（ChatGPT、Cursor 等）：
- Token 消耗低一个数量级。没有 Agent、没有 MCP、没有 Skill 加载，就是纯粹的 prompt → response
- 无缝集成在 IDE 里，选中提交 → 右键 → 出结果，不需要切换窗口
- 支持多线程批量生成，不存在上下文超长的问题
- 模板可定制，生成风格和格式完全可控

**vs 其他 Changelog 插件**：
- 不只是 Changelog。同一个插件覆盖了 Changelog、日报、周报、commit message 四个场景
- 基于代码 diff 生成 commit message，不是只看文件名猜
- 支持多种 AI 后端，不绑定某一家

## 核心：用最少的 token 生成最准确的结果

这个插件最核心的价值不是"能调 AI"，而是**怎么把喂给 AI 的数据压缩到极致，同时不丢失关键信息**。

别人可能直接把 `git diff` 原样扔给 AI，但实际项目里这行不通：

- 一次提交可能改了几十个文件，diff 文本动辄几万行
- 自动生成的文件（proto、swagger、ORM 映射等）占了大量篇幅但对理解变更没用
- 删除的文件不需要把内容发给 AI，只需要告诉它"删了什么"
- 纯格式化变更（空格、import 顺序、注释修改）会淹没真正有意义的改动

插件在组装 prompt 之前，对 diff 做了多层过滤和压缩。

### 变更类型识别

插件不会对所有文件一视同仁，而是根据变更类型采用不同的处理策略：

```java
// CodeDiffUtil.java
if (changeType == CodeDiff.ChangeType.DELETE) {
    // 删除的文件：不发 diff 内容，只记录文件路径和行数
    diffContent = null;
} else if (changeType == CodeDiff.ChangeType.ADD) {
    // 新增文件：只预览前 50 行，跳过 import 语句，限制 4000 字符
    diffContent = buildAddedFilePreview(change, virtualFile);
} else if (changeType == CodeDiff.ChangeType.RENAME) {
    // 纯重命名（没有内容变更）：只记录 "moved from A to B"
    diffContent = buildMovedFileSummary(change);
} else {
    // 修改文件：提取真正的 diff
    diffContent = extractDiffResult(change);
}
```

这就意味着：
- **删除一个 500 行的文件**：AI 只看到 `src/foo.java deleted`，不会把 500 行代码发过去
- **新增一个生成的代码文件**：AI 只看到前 50 行预览，不是把整个文件塞进去
- **重命名一个文件**：AI 只看到 `moved from old.java to new.java`，不需要 diff

### 过滤噪音 diff

在生成 unified diff 时，插件对每个 diff 块做了四层噪音过滤：

```java
// CodeDiffUtil.java - generateUnifiedDiffInternal()

// 1. 纯空白字符变更：前后内容去掉空白后一样，跳过
if (isWhitespaceOnlyChange(beforeChanged, afterChanged)) {
    continue;
}

// 2. 纯 import 变更：只改了 import 语句，跳过
if (isImportOnlyChange(beforeChanged, afterChanged)) {
    continue;
}

// 3. 纯注释变更：Java 文件中只改了注释，跳过
if (isJavaFile && isCommentOnlyChange(beforeChanged, afterChanged)) {
    continue;
}

// 4. 纯顺序调整：行内容没变，只是顺序调了，跳过
if (isJavaFile && isReorderOnlyChange(beforeChanged, afterChanged)) {
    continue;
}
```

这四层过滤可以在大多数场景下把 diff 量砍掉 30%-50%。

### 硬限制截断

即使经过过滤，某些文件的 diff 仍然可能很长（比如大文件的重构）。插件设置了多层硬限制：

```java
// 每个文件最多保留 6 个 diff 块
private static final int MAX_HUNKS_PER_FILE = 6;

// 单个 diff 块最多保留 20 行
private static final int MAX_LINES_PER_HUNK = 20;

// 单行最大 240 字符（超过截断）
private static final int MAX_DIFF_LINE_CHARS = 240;

// 新增文件预览最大 4000 字符
private static final int MAX_ADDED_PREVIEW_CHARS = 4000;

// 单文件 diff 最大 12000 字符（超过直接截断）
private static final int MAX_DIFF_CHARS_PER_FILE = 12000;
```

这意味着不管你的提交改了多大的文件，每个文件发给 AI 的数据量是有上限的。一个文件改了 200 处，AI 也只看到最有意义的 6 个 hunk、每个最多 20 行。

### PSI 语义增强

过滤和截断解决的是"少发"的问题，但还有一个挑战：**diff 本身缺少上下文**。比如你改了一个方法体，diff 只显示 `+` 和 `-` 的行，AI 不知道这个方法叫什么、属于哪个类。

插件通过 IntelliJ PSI 接口，在 diff 块中注入符号上下文：

```java
// CodeDiffUtil.java - generateUnifiedDiffInternal()
String context = resolveSymbolContext(virtualFile, afterStart, beforeStart);
if (context != null && !context.isEmpty()) {
    diff.append("上下文: ").append(context).append("\n");
}
```

PSI 解析器支持 Java、Kotlin、Go、Python、XML 等语言，能自动识别变更所在的类名、方法名、模块名。这样 AI 看到的不是一堆裸 diff，而是带有语义标注的结构化数据。

### 实际效果

一套组合拳下来，同样的代码变更，插件发给 AI 的 token 量大约是直接发 `git diff` 的 **1/5 到 1/10**。而且因为噪音被过滤掉了，AI 的生成质量反而更高——它不会被格式化变更误导，能专注于理解真正的业务改动。

## 架构设计

整体分四层：

```
┌─────────────────────────────────────────────────────────────┐
│                    IntelliJ IDEA                           │
├─────────────────────────────────────────────────────────────┤
│  UI Layer                                                   │
│  ├── Git Log 右键菜单                                       │
│  ├── Git 提交页面集成                                       │
│  ├── 设置面板                                               │
│  └── 结果展示对话框                                         │
├─────────────────────────────────────────────────────────────┤
│  Service Layer                                              │
│  ├── ChangelogService (核心服务)                             │
│  ├── CommitMessageGenerator (提交信息生成器)                 │
│  ├── Git 操作封装                                           │
│  └── 模板管理器                                             │
├─────────────────────────────────────────────────────────────┤
│  AI Integration Layer                                       │
│  ├── IntelliAI Engine 依赖                                  │
│  ├── Prompt 模板引擎                                        │
│  └── 响应处理器                                             │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                 │
│  ├── JGit 提交记录读取                                      │
│  ├── Code Diff 分析                                         │
│  └── 配置持久化                                             │
└─────────────────────────────────────────────────────────────┘
```

### 核心服务：ChangelogService

这是整个插件的核心，负责读取提交、组装 prompt、调 AI 生成内容：

```java
@Service(Service.Level.PROJECT)
public final class ChangelogService {

    @NotNull
    public String generateChangelog(@NotNull List<String> commitHashes) {
        // 1. 通过 JGit 读取提交记录
        List<CommitInfo> commits = readCommits(commitHashes);

        // 2. 按日期分组，组装 prompt
        String prompt = buildPrompt(commits);

        // 3. 调用 AI 服务
        return callAIService(prompt);
    }

    @NotNull
    public String generateDailyReport(@NotNull List<String> commitHashes) {
        // 使用日报模板
    }

    @NotNull
    public String generateWeeklyReport(@NotNull List<String> commitHashes) {
        // 使用周报模板
    }
}
```

### 读取 Git 提交

用 JGit 读取选中的提交记录，提取 hash、消息、作者、时间：

```java
@NotNull
private List<CommitInfo> readCommits(@NotNull List<String> commitHashes) {
    List<CommitInfo> commits = new ArrayList<>();
    Repository repository = getRepository();

    try (Git git = new Git(repository)) {
        for (String hash : commitHashes) {
            ObjectId commitId = repository.resolve(hash);
            if (commitId != null) {
                RevCommit commit = git.log()
                    .add(commitId)
                    .setMaxCount(1)
                    .call()
                    .iterator()
                    .next();

                commits.add(new CommitInfo(
                    commit.getName(),
                    commit.getShortMessage(),
                    commit.getFullMessage(),
                    new Date(commit.getCommitTime() * 1000L),
                    commit.getAuthorIdent().getName()
                ));
            }
        }
    }
    return commits;
}
```

### 基于 Diff 生成提交信息

除了从提交记录生成 Changelog，插件还能在提交前分析代码 diff，自动生成 commit message：

```java
@NotNull
public String generateCommitMessageFromDiff(@NotNull Collection<Change> changes) {
    // 1. 提取代码变更信息
    List<CodeDiff> codeDiffs = CodeDiffUtil.extractCodeDiffs(changes);

    if (codeDiffs.isEmpty()) {
        throw new Exception("没有检测到代码变更");
    }

    // 2. 构建 prompt，包含文件路径、变更类型、增删行数、diff 内容
    String prompt = buildPromptFromCodeDiff(codeDiffs);

    // 3. 调用 AI
    return callAIServiceForCommitMessage(prompt);
}
```

Diff 分析会过滤掉纯格式化变更（空白字符改动），只保留有意义的代码变更：

```java
private static boolean isMeaningfulChange(CodeDiff diff) {
    if (diff.addedLines == 0 && diff.deletedLines == 0) {
        return false;
    }
    if (diff.diffContent != null &&
        diff.diffContent.matches("(?s).*^\\s*[+-]\\s*$.*")) {
        return false;
    }
    return true;
}
```

### Prompt 设计

Changelog 生成用的系统提示词：

```java
private static final String CHANGELOG_SYSTEM_PROMPT = """
    你是一位专业的技术文档撰写专家。

    根据 Git 提交记录生成版本更新日志。

    生成原则：
    1. 用户导向：重点说明对用户的价值，不是技术细节
    2. 分类清晰：按功能类型分类
    3. 语言简洁：避免过于技术化的描述
    4. 格式规范：Markdown 格式，适当 emoji

    分类标准：
    - 🎉 重大更新：重要功能发布、架构升级
    - 🚀 新增功能：新功能模块
    - 🐛 问题修复：Bug 修复
    - 🔧 技术改进：性能优化、重构
    - 📚 文档更新：文档相关

    注意：
    - 输出不要用代码块包裹
    - 根据实际情况灵活调整分类
    """;
```

Prompt 模板是可配置的，用户可以在设置面板里自定义。

## 模板系统

插件内置了几种模板，也支持用户自定义。模板里用 `{version}`、`{commits}`、`{date}` 等占位符：

```java
@NotNull
private String buildPrompt(@NotNull List<CommitInfo> commits) {
    SettingsState settings = SettingsState.getInstance();
    String template = settings.changelogTemplate;
    String commitsText = buildCommitsText(commits);

    return template
        .replace("{version}", "v1.0.0")
        .replace("{commits}", commitsText);
}
```

提交记录会按日期分组后再塞进 prompt，这样 AI 能理解时间序列：

```java
@NotNull
private String buildCommitsText(@NotNull List<CommitInfo> commits) {
    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
    Map<String, List<CommitInfo>> commitsByDate = new LinkedHashMap<>();

    for (CommitInfo commit : commits) {
        String dateStr = dateFormat.format(commit.date);
        commitsByDate.computeIfAbsent(dateStr, k -> new ArrayList<>()).add(commit);
    }

    StringBuilder sb = new StringBuilder();
    for (Map.Entry<String, List<CommitInfo>> entry : commitsByDate.entrySet()) {
        sb.append("### ").append(entry.getKey()).append("\n\n");
        for (CommitInfo commit : entry.getValue()) {
            sb.append("- ").append(commit.shortMessage).append("\n");
        }
        sb.append("\n");
    }
    return sb.toString().trim();
}
```

## 生成效果示例

### Changelog 生成

输入（Git 提交记录）：

```
### 2024-10-27

- fix: 修复用户登录 token 过期问题
- feat: 新增用户积分系统
- refactor: 重构订单处理逻辑
- fix: 修复支付接口超时问题
- docs: 更新 API 文档
```

输出：

```markdown
# v1.2.0 版本更新 (2024-10-27)

## 🚀 新增功能

### 用户积分系统
- 新建完整的用户积分管理体系
- 支持积分获取、消费、查询功能
- 集成签到、分享等积分获取渠道

## 🐛 问题修复

### 登录稳定性提升
- 修复了用户登录时 token 过期导致的异常问题
- 优化 token 刷新机制，提升登录体验

### 支付系统优化
- 修复支付接口在高并发下的超时问题
- 优化支付重试机制，提高支付成功率

## 🔧 技术改进

### 订单处理重构
- 重构订单处理的业务逻辑，提升代码可维护性
- 优化订单状态流转，减少逻辑错误
```

### 基于 Diff 生成 Commit Message

输入（代码变更）：

```java
// 文件: UserService.java
// 新增 15 行，删除 8 行
+ public UserDTO getUser(String userId) {
+     return userMapper.findById(userId);
+ }
```

输出：

```
feat(user): 新增用户查询服务

- 新增 UserService 类，提供用户信息查询功能
- 实现基于用户ID的查询方法 getUser
- 集成 MyBatis 进行数据库操作
- 添加完整的 JavaDoc 文档

Closes #123
```

## 异步处理和性能

生成过程放在后台线程，不阻塞 UI：

```java
@Override
protected void actionPerformed(@NotNull AnActionEvent e,
                               @NotNull List<String> commitHashes) {
    Project project = e.getProject();
    if (project == null) return;

    ProgressManager.getInstance().run(new Task.Backgroundable(project, "生成 Changelog") {
        @Override
        public void run(@NotNull ProgressIndicator indicator) {
            try {
                indicator.setText("正在读取提交记录...");
                ChangelogService service = ChangelogService.getInstance(project);
                String changelog = service.generateChangelog(commitHashes);

                ApplicationManager.getApplication().invokeLater(() -> {
                    showResultDialog(project, changelog);
                });
            } catch (Exception ex) {
                ApplicationManager.getApplication().invokeLater(() -> {
                    showErrorDialog(project, ex.getMessage());
                });
            }
        }
    });
}
```

提交记录做了缓存，同一个 hash 不会重复读取：

```java
private final Map<String, String> commitCache = new ConcurrentHashMap<>();

@NotNull
private List<CommitInfo> readCommits(@NotNull List<String> commitHashes) {
    // ...
    for (String hash : commitHashes) {
        String cached = commitCache.get(hash);
        if (cached != null) {
            commits.add(deserializeCommitInfo(cached));
            continue;
        }
        // 读取并缓存
    }
}
```

## 配置项

设置面板支持：

- **AI 提供商**：OpenAI、Anthropic、Ollama 等
- **模板定制**：Changelog、日报、周报各自的 prompt 模板
- **系统提示词**：调整 AI 的生成风格
- **语言偏好**：生成内容的语言和格式

## 效率对比

| 场景 | 手动 | 插件 | 提升 |
|------|------|------|------|
| 版本 Changelog | 2-3 小时 | 5-10 分钟 | ~24x |
| 工作日报 | 30-60 分钟 | 3-5 分钟 | ~12x |
| 工作周报 | 1-2 小时 | 10-15 分钟 | ~8x |
| Commit message 规范 | 看心情 | 95% 规范率 | - |

**相关文章**:

1. [[build-idea-plugin-ai-engine|IntelliAI Engine]] - 统一接入 30+ AI 服务商的底层平台
2. [[build-idea-plugin-ai-terminal|IntelliAI Terminal]] - 终端自然语言生成 Shell 命令
3. [[build-idea-plugin-ai-javadoc|IntelliAI JavaDoc]] - AI 驱动的 JavaDoc 自动生成插件

## 相关链接

- **IntelliJ 插件市场**: [https://plugins.jetbrains.com/plugin/intelliai-changelog](https://plugins.jetbrains.com/plugin/intelliai-changelog)
- **GitHub**: [https://github.com/dong4j/zeka-stack](https://github.com/dong4j/zeka-stack)
- **IntelliAI Engine**: [https://github.com/dong4j/zeka-stack/tree/main/intelli-ai-engine](https://github.com/dong4j/zeka-stack/tree/main/intelli-ai-engine)
- **Changelog 开发文档**: [https://ideaplugin.dong4j.site/changelog/docs.html](https://ideaplugin.dong4j.site/changelog/docs.html)
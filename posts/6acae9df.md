<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.site/pc?spm={{spm}})

## 我的 AI Native 开发者画像（2026）
> 基于 196 天的本地 Claude Code + Codex 对话数据自动生成 · 2026-05-08T15:18:22+08:00
> _默认对外分享版：项目名已匿名，敏感字段已清洗。_

---

## 一览
- 在 **196** 天里完成 **481** 次 Claude sessions + **296** 次 Codex threads，共 **1.9万** 条 Claude 消息
- 日均产出：**20.69** commits / **8.1万** 行代码变动 / **28.23** GitHub contributions
- 同时维护 **18** 个本地仓库，横跨 **74** 类语言/文件扩展
- 同期 GitHub：**2,155** commits / **1** PRs / **30** issues / **2,682** 总贡献
- 本地 git：**1,966** commits / **+5.24M** / **-2.46M**
- AI 投入：**27.24M** Claude 新付费 token + **1.46B** Codex token；复用 **215.98M** 缓存（占 Claude I/O **88.8%**）
- 主力工具：Claude Code + Codex CLI

## 🚀 Velocity & Leverage — AI 让一个人拥有了小团队的交付能力
> 18 个仓库、74 类语言/文件扩展、日均 20.69 commits。这里的价值不只是更快写代码，而是能在多个上下文之间持续推进。
| 指标 | 数值 | 说明 |
| --- | ---: | --- |
| 日均 commits | 20.69 | 本地 git commits / 活跃天数 |
| 日均代码变动 | 8.1万 行 | additions + deletions / 活跃天数 |
| 同时维护仓库 | 18 个 | 候选仓库中过去一年有当前用户 commit |
| 跨栈语言 | 74 类 | 基于 git numstat 文件扩展估算 |
| GitHub 贡献爆发 | 2025-12-31~2026-01-05；2026-01-07~2026-01-12；2026-01-14~2026-01-16 | 连续 3+ 天 daily > 20 的窗口 |
| 开源影响力 | 128 stars | 跨 24 个被 star 的仓库 |

## 🤖 AI-Native 实践
> 不是偶尔问问 AI，而是把多模型、planning、skill、hook 和本地自动化接到日常开发链路里。

### 多模型编排
| 模型 | sessions / threads | spent tokens | cache-read | 用途倾向 |
| --- | ---: | ---: | ---: | --- |
| glm-4.7 | 0 | 11.48M | 68.84M | 补充模型 / 特定任务 |
| glm-5.1 | 0 | 6.64M | 76.39M | 补充模型 / 特定任务 |
| mimo-v2.5-pro | 0 | 3.94M | 6.74M | 补充模型 / 特定任务 |
| MiniMax-M2.1 | 0 | 2.13M | 14.88M | 补充模型 / 特定任务 |
| deepseek-v4-pro | 0 | 98.8万 | 20.34M | 补充模型 / 特定任务 |
| claude-sonnet-4-6 | 0 | 77.6万 | 13.53M | 快速迭代 / 批量任务 |
| claude-opus-4-7 | 0 | 57.5万 | 3.22M | 深度推理 / 长上下文 |
| deepseek-v4-flash | 0 | 40.6万 | 8.02M | 补充模型 / 特定任务 |
| gpt-5.2-codex (Codex) | 71 | 755.53M | — | 代码协作 / 仓库执行 |
| gpt-5.5 (Codex) | 28 | 322.93M | — | 代码协作 / 仓库执行 |
| gpt-5.3-codex (Codex) | 11 | 152.56M | — | 代码协作 / 仓库执行 |
| gpt-5.1-codex-max (Codex) | 37 | 93.77M | — | 代码协作 / 仓库执行 |
| gpt-5.2 (Codex) | 24 | 58.71M | — | 代码协作 / 仓库执行 |

### 高级能力深度使用
- **Plan-mode**: **0** 次
- **Effort 调节**: **0** 次
- **Skill 调用**: **8** 次；Skills 共 **30** 个
- **Plans**: **0** 份；Hooks: **11** 个；MCP servers: **0** 个；Automations: **0** 个；Rules: **1** 个

### Prompt caching 熟练度
每花费 1 个新 token，复用 **7.93** 个缓存 token（cache-read 占 Claude I/O 的 **88.8%**）。

### Reasoning effort 偏好
medium **170**（**57.4%**） · unspecified **104**（**35.1%**） · high **12**（**4.1%**） · low **10**（**3.4%**）

## 🔧 AI 基础设施 — 不只用 AI，还在给 AI 造工具
> 从 skill 到 hook 到 automation，重点是把一次性的提示词沉淀成可复用的工作流。

### 自建 / 本地 Skills
| 名称 | 描述 | 工具 |
| --- | --- | --- |
| sora | Use when the user asks to generate, edit, extend, poll, list, download, or delete Sora videos, creat | Codex |
| wechat-article-to-markdown | Fetch WeChat Official Account (微信公众号) articles from mp.weixin.qq.com and convert to Markdown. 微信文章转  | Codex |
| pdf | Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter;  | Codex |
| playwright | Use when the task requires automating a real browser from the terminal (navigation, form filling, sn | Codex |
| resume-optimizer | 面向求职者的简历审计与优化 skill。用于：(1) 深度审计简历内容，定位最影响面试通过率的问题 (2) 将职责型表述改写为成果型表述，突出量化结果、业务价值与交付产物 (3) 结合目标岗位 JD  | Codex |
| drawio | Always use when user asks to create, generate, draw, or design a diagram, flowchart, architecture di | Codex |
| llm-wiki | Build and maintain a Karpathy-style LLM knowledge base — a self-compiling Obsidian markdown wiki whe | Codex |
| doc | Use when the task involves reading, creating, or editing `.docx` documents, especially when formatti | Codex |
| architecture-diagram | Create professional, dark-themed architecture diagrams as standalone HTML files with SVG graphics. U | Codex |
| readme-skill | 生成一份对外可分享、脱敏的 AI-Native 开发者 README。 量化展示我对 Claude Code + Codex CLI 的使用深度、AI 协作风格、项目与领域分布、 兴趣主题，以及与 G | Codex |

### 安装的 Skills
| 名称 | 描述 | 工具 |
| --- | --- | --- |
| write | Invoke only when explicitly asked to write, edit, or polish prose in Chinese or English. Strips AI w | Claude |
| defuddle | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to | Claude |
| design | Invoke when building any UI, component, page, or visual interface. Produces distinctive design with  | Claude |
| learn | Invoke when diving deep into an unfamiliar domain, preparing a research article, or turning collecte | Claude |
| think | Invoke before writing any code for a new feature, design, or architecture decision. Turns rough idea | Claude |
| humanizer-zh | 去除文本中的 AI 生成痕迹。适用于编辑或审阅文本，使其听起来更自然、更像人类书写。 基于维基百科的"AI 写作特征"综合指南。检测并修复以下模式：夸大的象征意义、 宣传性语言、以 -ing 结尾的肤 | Claude |
| hunt | Invoke when debugging any error, crash, unexpected behavior, or failing test. Finds root cause befor | Claude |
| wechat-article-to-markdown | Fetch WeChat Official Account (微信公众号) articles from mp.weixin.qq.com and convert to Markdown. 微信文章转  | Claude |
| obsidian-markdown | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other O | Claude |
| health | Invoke when Claude ignores instructions, behaves inconsistently, hooks malfunction, or MCP servers n | Claude |
| read | Invoke when given any URL, web page link, or PDF to read. Fetches the content as clean Markdown via  | Claude |
| find-skills | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a  | Claude |

## 🛠️ AI 协作风格

### 最常用的 slash 命令 Top 10
| # | 命令 | 次数 | 含义 |
| --- | --- | ---: | --- |
| 1 | `/exit` | 60 | 工作流控制 |
| 2 | `/ide` | 36 | 工作流控制 |
| 3 | `/mcp` | 16 | 工作流控制 |
| 4 | `/init` | 10 | 工作流控制 |
| 5 | `/plugin` | 9 | 工作流控制 |
| 6 | `/model` | 6 | 工作流控制 |
| 7 | `/skills` | 6 | 工作流控制 |
| 8 | `/terminal-setup` | 3 | 工作流控制 |
| 9 | `/permissions` | 3 | 工作流控制 |
| 10 | `/context` | 3 | 工作流控制 |

### Session 架构
- **0.0%** 的命令型 session 以 `/plan` 开头，说明复杂任务里有明显的先规划倾向。
- **0.0%** 的命令型 session 使用过 `/compact` 或 `/clear`，会主动管理上下文窗口。
- `/resume` 恢复率约 **0.0%**；平均会话深度 **39.8** 条消息 / session。
- 最长 session: **17.9** 小时 / **307** 条消息。

## 📂 项目与领域分布
跨 **77** 个项目活跃，按领域分布：
| 领域 | 项目数 |
| --- | ---: |
| ML / RL / 论文 | 77 |

### Top 项目（脱敏）
| 项目 | Claude | Codex | Git commits | 编排模式 | 领域 |
| --- | ---: | ---: | ---: | --- | --- |
| 项目 A | 474 | 0 | 0 | Claude 主导 | ML / RL / 论文 |
| 项目 B | 0 | 121 | 999 | Codex 主导 | ML / RL / 论文 |
| 项目 C | 16 | 5 | 139 | Claude 主导 | ML / RL / 论文 |
| 项目 D | 0 | 15 | 139 | Codex 主导 | ML / RL / 论文 |
| 项目 E | 0 | 11 | 120 | Codex 主导 | ML / RL / 论文 |
| 项目 F | 0 | 11 | 81 | Codex 主导 | ML / RL / 论文 |
| 项目 G | 0 | 8 | 82 | Codex 主导 | ML / RL / 论文 |
| 项目 H | 0 | 2 | 100 | Codex 主导 | ML / RL / 论文 |
| 项目 I | 16 | 5 | 0 | Claude 主导 | ML / RL / 论文 |
| 项目 J | 9 | 7 | 0 | 双引擎 | ML / RL / 论文 |
| 项目 K | 0 | 1 | 64 | Codex 主导 | ML / RL / 论文 |
| 项目 L | 4 | 1 | 38 | Claude 主导 | ML / RL / 论文 |

编排模式统计：双引擎 **1** 个 · Claude 主导 **4** 个 · Codex 主导 **7** 个

## 🧬 Evolution 曲线 — AI 用法在进化
```
2026-01  Claude Code 进入日常使用，开始积累 sessions 与 prompt-caching
2025-10  Codex CLI 开始记录本地 threads，双工具协作成型
2026-05  Skills / hooks / rules 进入基础设施层，沉淀可复用能力
```
月度活跃趋势：
| 月份 | Claude sessions | Codex threads | 里程碑 |
| --- | ---: | ---: | --- |
| 2025-10 | 0 | 2 | Codex 活跃 |
| 2025-11 | 0 | 18 | Codex 活跃 |
| 2025-12 | 0 | 83 | Codex 活跃 |
| 2026-01 | 26 | 114 | Claude 活跃 / Codex 活跃 |
| 2026-02 | 3 | 22 | Claude 活跃 / Codex 活跃 |
| 2026-03 | 0 | 10 | Codex 活跃 |
| 2026-04 | 409 | 22 | Claude 活跃 / Codex 活跃 |
| 2026-05 | 43 | 25 | Claude 活跃 / Codex 活跃 |

## 💡 兴趣主题 & 关键词
> **dong4j**·669　**java**·470　**com**·403　**users**·395　**developer**·380　**生成**·368　**md**·353　**ai**·343　**教材**·298　**tool**·262　**使用**·244　**hexo**·243　**stack**·236　**chunk**·234　**intellij**·223　**site**·220　**zeka**·212　**id**·209　**问题**·206　**idea**·202　**info**·198　**文件**·195　**html**·190　**https**·188　**dev**·182

## ⏱️ 工作节奏

### 24 小时活跃热力图
```
00 ██████████████ 188
01 ███████████████ 194
02 ████ 56
03 ██ 26
04 ███ 41
05 █ 10
06  0
07 █ 2
08 █ 9
09 ████████ 111
10 ████████ 105
11 ████████████ 159
12 ███████ 86
13 ███████ 88
14 ██████████ 134
15 ██████████ 129
16 ██████████████ 179
17 ███████████ 150
18 ██████ 78
19 ███████ 90
20 ████████████ 153
21 ██████████████ 180
22 ████████████████ 209
23 ██████████████████ 238
```
峰值时段：23, 22, 01

### 时间跨度
- 首次 / 最近活跃: 2025-10-25 / 2026-05-08
- 活跃天数 / 最长连续 / Claude 单日峰值: 95 / 29 / 2026-04-24（6839 messages）

## 💎 Token 经济学
> **1.49B** 新付费 token 撬动 **215.98M** 缓存复用，Claude cache 杠杆比 **1 : 7.93**；总通过我手里约 **1.70B** token。

### 每模型 token 明细（按 spent 排序）
| 模型 | spent | cache-read | leverage | 占总 spent |
| --- | ---: | ---: | ---: | ---: |
| glm-4.7 | 11.48M | 68.84M | 6.00x | 0.8% |
| glm-5.1 | 6.64M | 76.39M | 11.51x | 0.4% |
| mimo-v2.5-pro | 3.94M | 6.74M | 1.71x | 0.3% |
| MiniMax-M2.1 | 2.13M | 14.88M | 6.99x | 0.1% |
| deepseek-v4-pro | 98.8万 | 20.34M | 20.58x | 0.1% |
| claude-sonnet-4-6 | 77.6万 | 13.53M | 17.44x | 0.1% |
| claude-opus-4-7 | 57.5万 | 3.22M | 5.59x | 0.0% |
| deepseek-v4-flash | 40.6万 | 8.02M | 19.77x | 0.0% |
| claude-haiku-4-5-20251001 | 27.0万 | 3.92M | 14.50x | 0.0% |
| claude-sonnet-4-5-20250929 | 3.8万 | 9.4万 | 2.48x | 0.0% |
| gpt-5.2-codex (Codex) | 755.53M | — | — | 50.8% |
| gpt-5.5 (Codex) | 322.93M | — | — | 21.7% |
| gpt-5.3-codex (Codex) | 152.56M | — | — | 10.3% |
| gpt-5.1-codex-max (Codex) | 93.77M | — | — | 6.3% |
| gpt-5.2 (Codex) | 58.71M | — | — | 3.9% |

### 月度 token 趋势
| 月份 | Claude spent | Claude cache | Codex tokens | 主力模型 | 注解 |
| --- | ---: | ---: | ---: | --- | --- |
| 2025-10 | 0 | 0 | 0 | — | Codex 为主 |
| 2025-11 | 0 | 0 | 0 | — | Codex 为主 |
| 2025-12 | 0 | 0 | 217.23M | gpt-5.1-codex-max | Codex 为主 |
| 2026-01 | 39.5万 | 0 | 669.14M | gpt-5.2-codex | 双工具并行 |
| 2026-02 | 0 | 0 | 98.39M | gpt-5.3-codex | Codex 为主 |
| 2026-03 | 0 | 0 | 29.69M | gpt-5.4 | Codex 为主 |
| 2026-04 | 19.58M | 0 | 342.47M | gpt-5.5 | 双工具并行 |
| 2026-05 | 4.20M | 0 | 102.78M | gpt-5.5 | 双工具并行 |

### 单位投入产出（仅参考，勿当 KPI）
- 每 commit ≈ **1.4万** Claude spent tokens
- 每行代码变动 ≈ **3.54** Claude spent tokens
> 提醒：AI 产出还包含大量不直接转化为 commit 的高价值劳动，例如架构 review、数据清洗、plan 推演和 skill 重构。

## 💰 产出 & 投入

### GitHub 同期产出
- 365 天总贡献: **2,682** · 拥有仓库: **276**
- commits / PRs / issues / reviews: **2,155** / **1** / **30** / **0**
- restricted contributions: **449**
- 最高产单日: 2026-01-03(57) · 2026-01-07(51) · 2026-01-05(48) · 2026-01-08(47) · 2025-06-26(44)

#### Top 仓库
| 仓库 | language | commits | stars |
| --- | --- | ---: | ---: |
| zeka-stack/zeka-idea-plugin | Java | 999 | 6 |
| dong4j/self-star-list | Shell | 366 | 0 |
| dong4j/markdown-image-kit | Java | 118 | 69 |
| dong4j/spring-ai-cookbook | Java | 97 | 3 |
| zeka-stack/cubo-starter | Java | 94 | 0 |
| zeka-stack/blen-kernel | Java | 67 | 0 |
| zeka-stack/arco-maven-plugin | Java | 57 | 0 |
| zeka-stack/cubo-starter-examples | Java | 55 | 0 |
| zeka-stack/arco-builder | — | 40 | 1 |
| dong4j/dev-site | Astro | 37 | 0 |

### 本地 Git 产出
- 候选仓库内过去一年当前用户 commits: **1,966** · 代码变动: **+5.24M / -2.46M**

### 主要语言 / 文件类型
GitHub 仓库语言：HTML 404.33M · Java 5.54M · TypeScript 4.72M · CSS 1.60M · JavaScript 1.48M · Python 60.6万 · Stylus 33.8万 · MDX 30.2万 · Shell 26.7万 · Pug 18.2万 · Astro 17.0万 · XSLT 8.0万 · Go 5.9万 · Kotlin 5.2万 · Makefile 1.7万

本地文件类型：json" 3.98M · md 1.13M · md" 78.5万 · java 62.4万 · html 27.9万 · json 14.3万 · tsx 10.2万 · js 8.4万 · html" 5.9万 · ts 5.9万 · svg 4.6万 · sql 4.4万 · yaml 4.4万 · csv" 3.1万 · less 2.4万 · sh 2.4万 · xml 2.0万 · yml" 2.0万 · doc" 2.0万 · properties 1.9万

## 📊 数据来源 & 隐私承诺
- 数据 100% 本地：`~/.claude/*` + `~/.codex/*` + 本地 `git log` + GitHub via `gh`
- 对话正文仅用于关键词与协作风格分析，原文不会出现在报告中
- 项目名已匿名，API key / token / 邮箱 已正则清洗
- 报告由 Readme.skill 规则生成，可重复运行
- 生成时间: **2026-05-08T15:18:22+08:00**
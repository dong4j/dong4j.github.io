---
title: ZSH 启动慢，原来是这个问题！
abbrlink: 8d9a
date: 2024-12-04 00:00:00
ai:
  - 本文详细介绍了 macOS 中将 zsh 配置为默认 shell 时，由于配置文件加载顺序导致的启动时间过长的问题。文章首先解释了 Bash 和 zsh 的配置加载顺序差异，并分析了问题出现的可能原因。接着，通过排查发现是由于
    `.zshrc` 文件向 `.zprofile` 添加了大量重复的 `eval` 命令导致。最后，提供了优化 zsh 启动时间的建议和参考资料。
tags:
  - macOS
  - zsh
  - 配置加载顺序
  - Homebrew
  - 启动时间优化
categories:
  - 新时代码农
cover:
description: 本文详细介绍了 macOS 中将 zsh 配置为默认 shell 时，由于配置文件加载顺序导致的启动时间过长的问题。文章首先解释了 Bash
  和 zsh 的配置加载顺序差异，并分析了问题出现的可能原因。接着，通过排查发现是由于 `.zshrc` 文件向 `.zprofile` 添加了大量重复的 `eval`
  命令导致。最后，提供了优化 zsh 启动时间的建议和参考资料。
keywords:
  - macOS
  - zsh
  - 配置加载顺序
  - Homebrew
  - 启动时间优化
---

## 背景

事情的起因是 ComfyUI 官网出桌面版了, 虽然是 Bete 版本, 当还是准备试用一下, 结果第一步安装环境就卡住了:

![20241229144917_jrgVhQ2O.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144917_jrgVhQ2O.webp)

`The default interactive shell is now zsh. To update your account to use zsh, please run 'chsh -s bin/zsh'.`

这个再熟悉不过了, 提示我们更新 shell 为 zsh, 但是我并不想更新, 我并不想把 zsh 用作我的默认 shell, 因为 zhs 的启动时间太长.

这个问题是在将老系统迁移到新买的 MBP 时出现的, 现象是将 zsh 作为默认 shell 后, 每次打开终端都需要等待 1-2 分钟, 才出现提示符. 这显然是不能接受的.

后来使用 `Command` 直接指定 `/bin/zsh` 就可以了, 也就没在深究这个问题.

![20241229144917_9dgdO327.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144917_9dgdO327.webp)

但今天这个问题逃不过去了, 就开始研究一下, 彻底解决这个问题.

## shell 配置加载顺序

因为现象是使用默认的 `/bin/bash` , 然后直接是用 `/bin/zsh` 切换到 zsh 打开速度很快.

但是将 zsh 设置为系统默认 shell 时就会卡住, 且 Title 处会有多个 job 循环显示, 所以我猜测是 zsh 的配置文件加载顺序有问题.

在 Unix 和类 Unix 操作系统中，shell 有两种类型的会话：

- `interactive login shell`：这种类型的 shell 在 **用户登录时被启动**，通常是用户首次打开终端或连接到服务器时所见的 shell。login shell 负责加载与系统配置相关的文件，例如/etc/profile、~/.profile 等。这些文件用于设置环境变量、配置别名和函数、加载系统级别的 bash 插件等。

- `interactive non-login shell`：这种类型的 shell 在 **用户已经登录并且不涉及新会话的情况下启动**，例如通过 bash -i 或通过某些图形界面工具打开的终端窗口。non-login shell 通常不会加载与登录相关的文件，而是从当前用户的.bashrc 或.zshrc（如果是使用 zsh）等个人配置文件中读取设置。

### bash 配置加载顺序

对于 Bash，它们的工作原理如下。阅读相应的列。执行 A，然后执行 B，然后执行 C 等等。B1、B2、B3 表示它只执行找到的第一个文件。

| config             | interactive login shell | interactive non-login shell | script |
| ------------------ | ----------------------- | --------------------------- | ------ |
| `/etc/profile`     | A                       |                             |        |
| `/etc/bash.bashrc` |                         | A                           |        |
| `~/.bashrc`        |                         | B                           |        |
| `~/.bash_profile`  | B1                      |                             |        |
| `~/.bash_login`    | B2                      |                             |        |
| `~/.profile`       | B3                      |                             |        |
| `BASH_ENV`         |                         |                             | A      |
|                    |                         |                             |        |
| `~/.bash_logout`   | C                       |                             |        |

以 `interactive login shell` 为例:

1. 首先读取 `/etc/profile`
2. 然后加载 `~/.bash_profile`, `~/.bash_login`, `~/.profile` 三者中能找到的第一个配置;
3. 用户注销时执行 `~/.bash_logout`(如果存在的话);

执行顺序图:

![bash_load_config_order.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/bash_load_config_order.drawio.svg)

**1. 是否为交互式 Shell (Interactive?)**

- **Yes**：进入交互式模式，即用户可以在终端输入命令。
- **No**：非交互式模式，通常用于脚本执行。

**2. 交互式模式下**

**是否为登录 Shell (Login shell?)**

- **Yes**（登录 Shell）：

  - 如果 `--noprofile` 参数被指定，则 **不加载任何配置文件**。
  - 如果没有 `--noprofile`：
    - **加载** `/etc/profile`。
    - 然后依次查找以下文件中的第一个存在的文件：
      - `~/.bash_profile`
      - `~/.bash_login`
      - `~/.profile`
    - 这些文件可能包含对 ~/.bashrc 的引用。

- **No**（非登录 Shell）：
  - 如果指定 `--rcfile <file>`，则加载指定的配置文件。
  - 如果没有指定 --rcfile：
    - **没有** `--norc` **参数**：加载 `/etc/bash.bashrc` 和 `~/.bashrc`。
    - **有** `--norc` **参数**：不加载任何文件。

**3. 非交互式模式下**

- 如果指定 `--login` 参数，则加载 `/etc/profile` 及登录 Shell 配置文件。
- 如果没有 `--login`，但设置了 `$BASH_ENV` 变量，则加载该变量指定的文件。

#### 总结

- **登录 Shell** 通常在用户首次登录时启动，会加载 `/etc/profile` 和用户特定的登录配置文件（如 `~/.bash_profile`）。
- **非登录 Shell** 常用于终端内启动的子 Shell，主要加载 `~/.bashrc`。
- **非交互式 Shell** 主要用于脚本执行，加载 `$BASH_ENV` 指定的环境。

---

### zsh 配置加载顺序

对于 zsh：如果`~/.zshrc`不存在， zsh 似乎也会读取`~/.profile`)

| config          | interactive login shell | interactive non-login shell | script |
| --------------- | ----------------------- | --------------------------- | ------ |
| `/etc/zshenv`   | A                       | A                           | A      |
| `~/.zshenv`     | B                       | B                           | B      |
| `/etc/zprofile` | C                       |                             |        |
| `~/.zprofile`   | D                       |                             |        |
| `/etc/zshrc`    | E                       | C                           |        |
| `~/.zshrc`      | F                       | D                           |        |
| `/etc/zlogin`   | G                       |                             |        |
| `~/.zlogin`     | H                       |                             |        |
|                 |                         |                             |        |
| `~/.zlogout`    | I                       |                             |        |
| `/etc/zlogout`  | J                       |                             |        |

#### 总结

- 对于 `bash`，请将内容放入 `~/.bashrc` 中，然后使用 `~/.bash_profile` 来获取它;
- 对于 `zsh`，将内容放入 `~/.zshrc` 中，该操作始终执行;

## 问题排查

在清楚 bash 和 zsh 的配置加载顺序之后, 逐渐缩下了排查问题的范围, 现象是 zsh 作为默认终端加载慢(`interactive non-login shell`), 而在命令行中执行 `/bin/zsh` 切换到 zsh 就很快, 所以应该是 `/etc/zprofile` 和 `~/.zprofile` 配置的问题.

这是 `/etc/zprofile` 的配置:

```bash
# System-wide profile for interactive zsh(1) login shells.

# Setup user specific overrides for this in ~/.zprofile. See zshbuiltins(1)
# and zshoptions(1) for more details.

if [ -x /usr/libexec/path_helper ]; then
	eval `/usr/libexec/path_helper -s`
fi
```

应该没有什么问题, 注释说的是 **`~/.zprofile` 中的配置会覆盖这里的配置**.

那么见证奇迹的时刻出现了, 当我打开 `~/.zprofile` 后, 感觉不得不写一篇博客来记录一下:

![20241229144917_3xJ4AaVs.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144917_3xJ4AaVs.webp)

这个文件中有 4000+ 行相同的 `eval "$(/opt/homebrew/bin/brew shellenv)"` 配置.......

而在 `.zshrc` 存在如下配置:

```bash
...
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/dong4j/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
...
```

那问题现在就明了了: **因为每次启动 zsh 最终都会读取 `.zshrc` 文件, 然后 `.zshrc` 又会向 `.zprofile` 添加一行 `eval "$(/opt/homebrew/bin/brew shellenv)"` , 而第一次启动 zsh 的时候又要执行 `.zprofile` 里面几千行同样的命令**...... 😂😂😂

`eval "$(/opt/homebrew/bin/brew shellenv)"` 的作用是将 **Homebrew** 的环境变量配置到当前的 Shell 中，使得 Homebrew 的命令和软件可以正常使用。具体来说：

`/opt/homebrew/bin/brew shellenv` 会输出一系列环境变量设置命令:

```bash
export HOMEBREW_PREFIX="/opt/homebrew";
export HOMEBREW_CELLAR="/opt/homebrew/Cellar";
export HOMEBREW_REPOSITORY="/opt/homebrew";
fpath[1,0]="/opt/homebrew/share/zsh/site-functions";
PATH="/opt/homebrew/bin:/opt/homebrew/sbin:..........; export PATH;
[ -z "${MANPATH-}" ] || export MANPATH=":${MANPATH#:}";
export INFOPATH="/opt/homebrew/share/info:${INFOPATH:-}";
```

而 `eval` 会执行字符串形式的命令，将 brew shellenv 输出的环境变量立即加载到当前 Shell 环境中。

**总结起来**:

- **Homebrew** 在 macOS 上默认安装在 `/opt/homebrew`（Apple Silicon 或 Homebrew 自行编译的环境），为了让终端能够找到 brew 命令及其安装的软件，需要将其路径加入到 PATH 和其他环境变量中。

- 直接执行 eval 命令可以立即生效，而无需重启终端或手动修改配置文件。

而在翻看 **Homebrew** 的 **Discussions** 正好看到一个 [相关的讨论](https://github.com/orgs/Homebrew/discussions/446):

![20241229144917_npHEw9tq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144917_npHEw9tq.webp)

所以解决的办法就是删除 `.zshrc` 中的相关配置, 然后清理 `.zprofile`.

## macOS 设置 zsh 为默认 shell

从 macOS Catalina 开始，macOS 使用 zsh 作为默认登录 shell 和交互式 shell.

### 从命令行

在终端中，输入`$ chsh -s path`，其中*路径*是 /etc/shells 中列出的 shell 路径之一，例如 /bin/zsh、/bin/bash、/bin/csh、/bin/dash、/bin/ksh、/bin/sh 或 /bin/tcsh。

### 从用户和群组设置

在 macOS Ventura 或更高版本中：

1. 选择苹果菜单  >“系统设置”，然后单击边栏中的“用户与群组”。
2. 按住 Control 键并点按右侧用户列表中的用户名或用户图片，然后选择“高级选项”。
3. 出现提示时输入您的用户名和密码。
4. 从“登录 shell”菜单中选择一个 shell，然后单击“确定”保存更改。

在早期版本的 macOS 中：

1. 选择苹果菜单  >“系统偏好设置”，然后单击“用户与群组”。
2. 单击锁![20241229144917_kSBIoKG7.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144917_kSBIoKG7.webp)，然后输入您的用户名和密码。
3. 按住 Control 键并点按左侧用户列表中的用户名，然后选择“高级选项”。
4. 从“登录 shell”菜单中选择一个 shell，然后单击“确定”保存更改。

**参考:**

- [Use zsh as the default shell on your Mac](https://support.apple.com/en-ca/102360)

---

## zsh 启动时间优化

相关教程:

- [zsh 和 oh my zsh 冷启动速度优化](https://blog.skk.moe/post/make-oh-my-zsh-fly/)
- [优化 zsh 的启动速度](https://zhuanlan.zhihu.com/p/464117825)
- [解决 zsh 启动速度慢的优化方法](https://zhuanlan.zhihu.com/p/68303393)

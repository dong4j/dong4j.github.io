---
title: 使用 EXO 在多台设备上运行 LLM 的尝试
ai: true
abbrlink: bbe181f7
date: 2025-01-28 17:20:30
description:
categories:
tags:
cover:
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 简介

[EXO](https://github.com/exo-explore/exo?tab=readme-ov-file)

## python 3.12

因为我一直使用 miconda 来管理 python 的环境, 不过目前的 python 版本为 3.10, [EXO](https://github.com/exo-explore/exo?tab=readme-ov-file) 要求 python 版本为 3.12, 所以先尝试升级到 3.12.

```shell
conda activate
conda update conda
conda update python
python --version
```

遗憾的是版本依然是 3.10.x

造成这一问题的原因是因为 [conda forge](https://zhida.zhihu.com/search?content_id=236274981&content_type=Article&match_order=1&q=conda+forge&zhida_source=entity) 尚未完成迁移工作。迁移是指在 conda forge 上重新构建软件包以支持新的全局版本的过程，例如 Python 3.12 或 R 4.3。关于 Python 3.12 的迁移工作进展，我们可以在 [https://conda-forge.org/status/#python312](https://conda-forge.org/status/#python312)上查看：

所以我们需要首先解决 python 版本问题.

在 macOS 上使用 Conda 安装独立的 Python 3.12 环境，可通过以下步骤实现：

---

### **方法一：使用 Conda 直接安装（推荐优先尝试）**

```bash
conda search python
conda install python=3.12.8
```

---

### **方法二：手动安装 Python 3.12 + Conda 环境**

若 Conda 源中暂无 Python 3.12，可手动安装后绑定到 Conda 环境。

1. **通过 Homebrew 安装 Python 3.12**：

   ```bash
   brew update
   brew install python@3.12
   ```

   - 安装后路径通常为：`/usr/local/opt/python@3.12/bin/python3.12`

2. **创建 Conda 环境并指定 Python 路径**：

   ```bash
   conda create -n py312 --python=/usr/local/opt/python@3.12/bin/python3.12
   ```

3. **激活环境并验证**：
   ```bash
   conda activate py312
   python --version  # 应显示 Python 3.12.x
   ```

---

### **方法三：使用 pyenv 管理多版本 Python（灵活推荐）**

1. **安装 pyenv**：

   ```bash
   brew install pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **安装 Python 3.12**：

   ```bash
   pyenv install 3.12.0
   ```

3. **创建 Conda 环境并关联 pyenv 的 Python**：
   ```bash
   conda create -n py312 --python=$(pyenv prefix 3.12.0)/bin/python
   ```

---

### **常见问题解决**

1. **Conda 找不到 Python 3.12**：

   - 确认已添加 `conda-forge` 渠道。
   - 尝试搜索可用版本：
     ```bash
     conda search -c conda-forge python
     ```

2. **环境激活后 Python 版本未变**：

   - 检查是否误用系统 Python：
     ```bash
     which python  # 应显示 Conda 环境路径（如 ~/miniconda3/envs/py312/bin/python）
     ```

3. **依赖冲突**：
   - 创建纯净环境：
     ```bash
     conda create -n py312 python=3.12 --no-deps
     ```

---

### **总结建议**

- 优先尝试 **方法一**，若 Conda 支持则最简洁。
- 若需最新版或 Conda 源延迟，使用 **方法三（pyenv）** 更灵活。
- 手动绑定（方法二）适合熟悉路径管理的用户。

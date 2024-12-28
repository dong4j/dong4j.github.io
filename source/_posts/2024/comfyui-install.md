---
title: ComfyUI Desktop 安装问题
ai: true
categories: AI
tags: ComfyUI
cover: /images/cover/comfyui-install.png
abbrlink: 3c58
date: 2024-12-24 00:00:00
password: 123456   
message: 密码是 123456
---

![](/images/cover/comfyui-install.png)

## 简介

最近 [ComfyUI Desktop](https://github.com/Comfy-Org/desktop) 发布了 Bate 版本，但是安装的时候遇到了一些问题，记录一下。

## 问题

这次我尝试第二次安装 ComfyUI-Desktop，版本 0.3.33(241212)。自动安装没有成功。在查看日志并手动运行缺失的命令后，安装成功。想给遇到同样问题的朋友一个解决方法。我不知道这是否是一个 bug，但它在我的机器上没有正确部署。

## 解决

[这是我第一次安装时遇到的问题](https://github.com/Comfy-Org/desktop/issues/398)，似乎 0.3.33 版本已经修复了它，但我在 zsh 下仍然遇到问题, 所以这次我将仅使用初始 `.zshrc` 文件：

```bash
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)
source $ZSH/oh-my-zsh.sh
```

然后尝试首次启动：

![image_source/2024/comfyui-install/158af3be-6d51-4cfb-b4c6-f2bad78e4cc2.png](158af3be-6d51-4cfb-b4c6-f2bad78e4cc2.webp)

日志如下：

```
[2024-12-14 22:01:21.481] [info]  Running command: /Users/dong4j/comfy/ComfyUI/.venv/bin/python -m ensurepip --upgrade in /Users/dong4j/comfy/ComfyUI
[2024-12-14 22:01:23.353] [info]  Successfully created virtual environment at /Users/dong4j/comfy/ComfyUI/.venv
[2024-12-14 22:01:23.354] [info]  Installing PyTorch Nightly for macOS.
[2024-12-14 22:01:23.354] [info]  Running uv command: /Applications/ComfyUI.app/Contents/Resources/uv/macos/uv pip install -U --prerelease allow torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
...
[2024-12-14 22:01:23.367] [info]  �]2;clear; /Applications/ComfyUI.app/Contents/Resources/uv/macos/uv "pip"  "-U"  ��]1;clear;�
[2024-12-14 22:01:23.369] [info]
[2024-12-14 22:01:23.375] [info]  error: unexpected argument '--end-1734184883354:0' found

  tip: to pass '--end-1734184883354:0' as a value, use '-- --end-1734184883354:0'

Usage: uv pip install --upgrade --prerelease <PRERELEASE> <PACKAGE|--requirements <REQUIREMENTS>|--editable <EDITABLE>> <--index <INDEX>|--default-index <DEFAULT_INDEX>|--index-url <INDEX_URL>|--extra-index-url <EXTRA_INDEX_URL>|--find-links <FIND_LINKS>|--no-index>

For more information, try '--help'.
```

**关键点是**:

```bash
/Applications/ComfyUI.app/Contents/Resources/uv/macos/uv pip install -U --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

应该是之前尝试安装过 [PyTorch](https://developer.apple.com/metal/pytorch/)，但是不知道什么原因失败了，所以直接使用了虚拟环境中安装的 python（启动 ComfyUI-Desktop 时设置的目录：Users/dong4j/comfy）：

```bash
/Users/dong4j/comfy/ComfyUI/.venv/bin/pip3 install -U --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

执行完成后可以进行如下测试：

```python
import torch
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")
```

测试结果：

```bash
/Users/dong4j/comfy/ComfyUI/.venv/bin/python torch_test.py
tensor([1.], device='mps:0')
```

安装后的软件包列表：

```
➜  ComfyUI /Users/dong4j/comfy/ComfyUI/.venv/bin/pip3 list
Package           Version
----------------- ------------------
filelock          3.16.1
fsspec            2024.10.0
Jinja2            3.1.4
MarkupSafe        3.0.2
mpmath            1.3.0
networkx          3.4.2
numpy             2.2.0
pillow            11.0.0
pip               24.0
setuptools        75.6.0
sympy             1.13.1
torch             2.6.0.dev20241214
torchaudio        2.6.0.dev20241214
torchvision       0.22.0.dev20241214
typing_extensions 4.12.2
```

然后再次重启 ComfyUI-Desktop：然后再次重启 ComfyUI-Desktop：

![image_source/2024/comfyui-install/f5f96164-718e-4369-a08c-b074ddf4c024.png](f5f96164-718e-4369-a08c-b074ddf4c024.webp)

继续进行后续安装步骤应该就正常了，但是还缺少一些软件包，此时的软件包列表如下：

```
➜  ComfyUI /Users/dong4j/comfy/ComfyUI/.venv/bin/pip3 list
Package            Version
------------------ ------------------
certifi            2024.12.14
cffi               1.17.1
charset-normalizer 3.4.0
click              8.1.7
cryptography       44.0.0
Deprecated         1.2.15
filelock           3.16.1
fsspec             2024.10.0
gitdb              4.0.11
GitPython          3.1.43
huggingface-hub    0.26.5
idna               3.10
Jinja2             3.1.4
markdown-it-py     3.0.0
MarkupSafe         3.0.2
matrix-client      0.4.0
mdurl              0.1.2
mpmath             1.3.0
networkx           3.4.2
numpy              1.26.4
packaging          24.2
pillow             11.0.0
pip                24.0
pycparser          2.22
PyGithub           2.5.0
Pygments           2.18.0
PyJWT              2.10.1
PyNaCl             1.5.0
PyYAML             6.0.2
regex              2024.11.6
requests           2.32.3
rich               13.9.4
safetensors        0.4.5
setuptools         75.6.0
shellingham        1.5.4
smmap              5.0.1
sympy              1.13.1
tokenizers         0.21.0
torch              2.6.0.dev20241214
torchaudio         2.6.0.dev20241214
torchvision        0.22.0.dev20241214
tqdm               4.67.1
transformers       4.47.0
typer              0.15.1
typing_extensions  4.12.2
urllib3            1.26.20
wrapt              1.17.0
```

这次我尝试直接使用 ComfyUI 的 `requirements.txt` 安装依赖项（之前我已经尝试过一步一步手动安装依赖项并成功启动，按照提示安装：psutil、einops、scipy、torchsde、aiohttp、spandrel、kornia [使用`~/comfy/ComfyUI/.venv/bin/pip3 install xxx`]）：

```bash
~/comfy/ComfyUI/.venv/bin/pip3 install -r /Applications/ComfyUI.app/Contents/Resources/ComfyUI/requirements.txt
```

接下来是第三次发射：

![image_source/2024/comfyui-install/1ea4e799-daaf-4b46-bfab-a45132132b69.png](1ea4e799-daaf-4b46-bfab-a45132132b69.webp)

![image_source/2024/comfyui-install/151e374b-068e-4f3e-bee2-ff2698d97fd0.png](151e374b-068e-4f3e-bee2-ff2698d97fd0.webp)

## 总结

1. PyTorch 安装失败，导致后续步骤无法执行；
2. 无法自动安装其他依赖项。

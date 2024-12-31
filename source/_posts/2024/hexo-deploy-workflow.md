---
title: Hexo 博客部署与图片处理指南：自定义脚本的多平台实践与技巧
tags:
  - 图片处理
  - 自动清理脚本
  - ffmpeg转换
  - Hexo配置
  - HomeLab部署
abbrlink: 598d
date: 2024-12-30 10:45:57
categories:
ai:
  - 本文讨论了图片处理过程和优化方法，包括手动删除多余的图片、将图片转换成webp格式、上传到图床并替换图片标签、以及部署到服务器或GitHub。同时介绍了Hexo配置文件使用方式：通过`--config`参数指定自定义配置文件路径，允许在多个文件中合并配置，并说明了主题配置的两种方法——主题特定的配置文件和独立的配置文件。最后提到可以将内容部署到HomeLab或GitHub以及备份策略。
description: 本文讨论了图片处理过程和优化方法，包括手动删除多余的图片、将图片转换成webp格式、上传到图床并替换图片标签、以及部署到服务器或GitHub。同时介绍了Hexo配置文件使用方式：通过`--config`参数指定自定义配置文件路径，允许在多个文件中合并配置，并说明了主题配置的两种方法——主题特定的配置文件和独立的配置文件。最后提到可以将内容部署到HomeLab或GitHub以及备份策略。
cover: /images/cover/hexo-deploy-workflow.png
password: egb;wef
message: 未完成
---

![alt text](/images/cover/hexo-deploy-workflow.png)

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>



## 简介

随着博客文章的数量不断增加，尤其是长篇文章中需要插入大量图片，发布一篇博客变得更加复杂。这包括图片的剪切、格式转换、清理多余图片、上传图床、替换 Markdown 中的图片标签，以及最终发布到站点。如果全程手动操作，无疑会非常繁琐。为了解决这个问题，我将这些步骤全部实现为独立的脚本，最后通过 Makefile 将它们串联起来，打造了一套完整的 Hexo 部署工作流。

那么接下来就是讲怎么实现这个流程了, 这里就以 Hexo 为例, 只要了解整个思路, 我觉得其他的任何博客都可以实现这套流程.

## 图片处理

一图胜千言，因此我非常喜欢在博客中插入大量图片。无论是截图、网络图片，还是用 Drawio 绘制的 SVG，精心挑选的配图不仅能够提升博客的视觉效果，还能直观地增强内容的表达力和吸引力。

以前我对图片的处理步骤大致为:

1. 第一步是使用截图工具简单的处理一下图片, 比如截图, 调整尺寸, 打马赛克, 添加圆角, 添加阴影等等;
2. 第二步是将图片转换成 webp, 尽量在保证图片质量的前提下减小图片尺寸;
3. 第三步就是上传到图床, 然后替换原来的图片标签;

上面的步骤是一个正向流程, 但是可能会遇到这样的问题:

1. 图片忘了处理敏感信息;
2. 截取的图片没有达到预期;
3. 某个地方的配图需要更换为新图片;

可能还有一些其他原因需要重新处理或更换图片的话, 上面的图片处理流程要重新来一遍, 还得手动删除不再使用的图片.

一篇博客的发布, 可能大量时间都在处理图片. 所以为了规避这个问题, 本着能偷懒就偷懒的原则, 我开始尝试使用脚本处理图片, 所以接下来就是介绍图片的处理流程.

### 插入图片

>  我写博客的主力工具是 Typora, 还会结合 VSCode 来管理整个博客的文件, 截图工具使用了 [CleanShot X](https://cleanshot.com/).



[Typora](https://typoraio.cn/) 有一个很棒的功能: **插入图片时** 执行指定的操作. 比如我这里就是直接复制到 **指定目录** (这个操作同样适用于网络图片, Typora 会直接将原始图片下载到指定目录).

![20241231103443_bT7yAiud](./hexo-deploy-workflow/20241231103443_bT7yAiud.png)

按照上面的配置之后, Typora 插入的图片标签格式为:

```
![20241231103443_bT7yAiud](./hexo-deploy-workflow/20241231103443_bT7yAiud.png)
```



使用 Hexo 作为博客系统的朋友都知道, Hexo 可以将与 Markdown 文件同名的目录作为资源目录, 所以我在 Typora 中配置的就是 `./${filename}`.
不过 Hexo 需要配置一下(`_config.yml`) :

```yaml
post_asset_folder: true
relative_link: false
marked:
  prependRoot: true
  postAsset: true
```

**设置详解：**

- `post_asset_folder: true`
  执行 `hexo new post xxx `时，会同时生成  `./source/_posts/xxx.md`文件和 `./source/_posts/xxx` 目录，可以将该文章相关联的资源放置在该资源目录中。
- `relative_link: false`
  不要将链接改为与根目录的相对地址。此为默认配置。
- `prependRoot: true`
  将文章根路径添加到文章内的链接之前。此为默认配置。
- `postAsset: true`
  在 `post_asset_folder` 设置为 `true` 的情况下，在根据 `prependRoot` 的设置在所有链接开头添加文章根路径之前，先将文章内资源的路径解析为相对于资源目录的路径。

**举例说明：**

执行 `hexo new post demo` 后，在 `demo` 文章的资源路径下存放了 `a.jpg`，目录结构如下：

```
./source/_posts
├── demo.md
└── demo
    └── a.jpg
```

Hexo 正确显示图片的写法应该是:

```
![](a.jpg)
```

所以就会存在这样的问题: 在 Typora 中可以正常显示图片, 而 Hexo 网页中则无法显示. 这个问题有 2 种解决方案:

1. 在 Typora 中写完博客后, 全局手动将 `./demo/` 替换成空字符串;
2. 修改 `hexo-renderer-marked` 插件代码;

这里我们介绍第二种方式(其实我使用的是第一种方式, 因为我不想轻易修改 Hexo 的原始代码, 会为后续升级带来一些问题).

因为 `hexo-renderer-marked` 渲染插件默认的图片相对路径根目录是 `./source/_posts/demo/`，我们需要让这个路径向上回退一层，变成 `demo.md` 文件所在的目录，与本地编辑器预览时默认的根目录一致，这样既满足了本地编辑器的渲染需求，又能 让 Hexo 正确加载网页中的图片。

打开 `./node_modules/hexo-renderer-marked/lib/renderer.js`，搜索 `image(href, title, text)` 定位到修改图片相对路径的代码:

```javascript
// Prepend root to image path
image(href, title, text) {
	...

  if (!/^(#|\/\/|http(s)?:)/.test(href) && !relative_link && prependRoot) {
    if (!href.startsWith('/') && !href.startsWith('\\') && postPath) {
      const PostAsset = hexo.model('PostAsset');
      // findById requires forward slash
      const asset = PostAsset.findById(join(postPath, href.replace(/\\/g, '/')));
      // asset.path is backward slash in Windows
      if (asset) href = asset.path.replace(/\\/g, '/');
    }
    href = url_for.call(hexo, href);
  }

  ...
}
```


修改为:


```javascript
// Prepend root to image path
image(href, title, text) {
	...

  if (!/^(#|\/\/|http(s)?:)/.test(href) && !relative_link && prependRoot) {
    if (!href.startsWith('/') && !href.startsWith('\\') && postPath) {
      const PostAsset = hexo.model('PostAsset');
      // findById requires forward slash
      const fixPostPath = join(postPath, '../');
      const asset = PostAsset.findById(join(fixPostPath, href.replace(/\\/g, '/')));
      // asset.path is backward slash in Windows
      if (asset) href = asset.path.replace(/\\/g, '/');
    }
    href = url_for.call(hexo, href);
  }

  ...
}
```

简单地说，这里的修改就是将文章路径 `postPath` 换成了它的上一级路径 `fixPostPath`，更换的方法就是在 `postPath` 后面加上`../`。

现在，切换到 `demo.md`，保留 FrontMatte 中 `cover` 的图片路径，将文章中的图片路径变更为 `demo/a.jpg`：

需要注意的是 `./node_modules` 一般来说不被 Git 追踪，而且相关插件在更新后会覆盖掉人为修改，所以这个改动一般难以跨设备同步。现阶段可以采用的办法之一便是在仓库里另外保存 `renderer.js`，并在部署时、安装插件后，使用自动指令覆盖插件中的文件。

**参考资料**

- Github仓库中有关此问题的issue及解决方案：[#216](https://github.com/hexojs/hexo-renderer-marked/issues/216#issuecomment-1214703941)

---

### 清理图片



### 图片转换

1. 图片转换为 webp 以减少体积;
2. 按照一定规则重命名图片;

```python
import os
import re
import sys
import subprocess
import random
import string
from datetime import datetime
from utils import find_all_image_tags, extract_image_url_from_tag, extract_image_urls_from_md, get_all_md_files, find_md_file, is_url

SUPPORTED_IMAGE_FORMATS = {'.png', '.jpg', '.jpeg', '.bmp'}  # 添加更多支持的格式

def log(message):
    """
    打印中文日志信息。
    """
    print(f"日志：{message}")

def is_valid_filename(filename):
    """
    检查文件名是否已满足特定的命名规则。
    """
    naming_pattern = re.compile(r'^\d{14}_[a-zA-Z0-9]{8}\.webp$')
    return naming_pattern.match(filename) is not None

def generate_random_string(length=8):
    """
    生成指定长度的随机字符串。
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def convert_image_to_webp(image_path, quality=75):
    """
    使用ffmpeg将支持的图片格式转换为webp格式，如果图片已经是webp或不是支持的格式则跳过。
    """
    log(f"尝试转换图片 {image_path} 到webp格式")

    # 检查是否为URL或不是支持的图片格式
    if (is_url(image_path) or not os.path.splitext(image_path)[1].lower() in SUPPORTED_IMAGE_FORMATS):
        log(f"路径 {image_path} 是一个URL或不是支持的图片格式，跳过转换。")
        return image_path
    
    # 检查是否已存在同名的webp文件
    webp_path = os.path.splitext(image_path)[0] + '.webp'
    if os.path.exists(webp_path):
        log(f"同名webp文件已存在：{webp_path}，跳过转换。")
        return webp_path

    # 生成输出路径
    output_path = os.path.splitext(image_path)[0] + '.webp'

    # 构建并执行ffmpeg命令
    command = f"ffmpeg -i '{image_path}' -q:v {quality} '{output_path}' -loglevel quiet"
    subprocess.run(command, shell=True, check=True)  # 添加check=True以捕获错误

    log(f"图片 {image_path} 已转换为 {output_path}")
    return output_path

def rename_webp_file(webp_path, starts_with_images=False):
    """
    根据规则重命名webp文件，如果文件已存在则跳过。
    """
    # 检查文件是否为webp文件
    if not webp_path.lower().endswith('.webp'):
        log(f"文件 {webp_path} 不是webp文件，跳过重命名。")
        return os.path.basename(webp_path)
    
    
    # 检查文件名是否已满足规则
    if is_valid_filename(os.path.basename(webp_path)):
        log(f"文件 {webp_path} 名称已满足规则")
        if starts_with_images:
            return "/images/cover/" + os.path.basename(webp_path)   
        else:
            return os.path.basename(webp_path)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_string = generate_random_string()
    new_name = f"{timestamp}_{random_string}.webp"
    new_path = os.path.join(os.path.dirname(webp_path), new_name)
    if os.path.exists(new_path):
        log(f"文件 {new_path} 已存在，跳过重命名。")
        return os.path.basename(webp_path)
    os.rename(webp_path, new_path)
    if starts_with_images:
        # 图片路径以 /images 开头
        new_name = "/images/cover/" + new_name
    log(f"文件 {webp_path} 重命名为 {new_path}")
    return new_name

def update_md_image_tags(md_file, image_tag_map):
    """
    更新Markdown文件中的图片标签。
    """
    with open(md_file, 'r+', encoding='utf-8') as file:
        content = file.read()

        # 跳过不必要的替换
        updated = False
    
        for old_tag, new_tag in image_tag_map.items():
            print(f"正在处理图片标签：{old_tag} -> {new_tag}")
            if old_tag != new_tag and old_tag in content:
                content = content.replace(old_tag, new_tag)
                updated = True
                if '/images/cover/' in old_tag:
                    log(f"替换 cover 标签")
                    content = content.replace('cover: ' + extract_image_url_from_tag(old_tag), 'cover: ' + extract_image_url_from_tag(new_tag))

        # 只有在有更新时才写回文件
        if updated:
            file.seek(0)
            file.write(content)
            file.truncate()
        else:
            print(f"文件 {md_file} 中没有需要更新的图片标签。")

def get_referenced_images(md_file):
    """
    获取Markdown文件中引用的所有图片。
    """
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return extract_image_urls_from_md(content)


def process_md_file(md_file):
    """
    处理单个Markdown文件及其图片，避免重复处理。
    """
    log(f"正在处理 Markdown 文件：{md_file}")

    image_dir = os.path.splitext(md_file)[0]
    if not os.path.isdir(image_dir):
        log(f"未找到文件 {md_file} 对应的图片目录。")
        return

    image_tag_map = {}

    all_image_tags = find_all_image_tags(md_file)
    print(all_image_tags)

    for image_tag in all_image_tags:
        image_path = extract_image_url_from_tag(image_tag)
        if image_path.startswith('http'):
            log(f"已经是图床图片, 不需要转换 {image_path} ")
            continue  # Skip external images

        if image_path.startswith('/images'):
            # 图片路径以 /images 开头，需要在 source/images 目录下查找
            source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source')
            full_image_path = os.path.join(source_dir, 'images', image_path[len('/images'):].lstrip('/'))
        else:
            # 图片路径不是以 /images 开头，直接在文章目录下查找
            full_image_path = os.path.join(image_dir, image_path)
        
        if os.path.isfile(full_image_path):
            webp_path = convert_image_to_webp(full_image_path)
            # 检查 webp_path 是否为网络图片
            if not is_url(webp_path):
                new_name = rename_webp_file(webp_path, starts_with_images=True if image_path.startswith('/images') else False)
                new_tag = f"![{new_name}]({new_name})"
                image_tag_map[image_tag] = new_tag
            else:
                log(f"路径 {webp_path} 是一个URL，跳过重命名和标签替换。")

    if image_tag_map:
        update_md_image_tags(md_file, image_tag_map)

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    log(f"博客文章的基准目录：{base_dir}")

    # 初始化要处理的Markdown文件列表
    md_files_to_process = []

    if not args:
        # 处理所有Markdown文件
        md_files_to_process = get_all_md_files(base_dir)
    elif len(args) == 1 and args[0].isdigit():
         # 处理指定年份的Markdown文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(year_dir)
        else:
            log(f"年份目录 {args[0]} 不存在。")
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename)
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到Markdown文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return

    # 循环处理所有确定的Markdown文件
    for md_file in md_files_to_process:
        process_md_file(md_file)

    log("==================图片转换完成==================")
if __name__ == "__main__":
    main()	
```





### 批量上传图片

1. 拷贝 md 文件到 'source/_posts/publish' 目录下, 此目录作为最终需要发布的博客文章目录;
2. 通过 `picgo upload` 批量上传图片到图床;

关于第一点这里需要解释一下为什么还要专门搞一个目录来存放最终发布文章目录.

以前将图片上传到图床, 但是跑路了, 本地的博客中的图片全都是上传图床后的在线地址且本地的图片也没有备份,  所以图片全部丢失.

痛定思痛后想出了现在这个方法: **本地存放原始的图片和博客文章**, 需要发布到线上时, 拷贝一份原始博客出来, 然后替换其中的图片地址.

这样我本地留有原始的博客和图片, 再也不怕图床跑路了, 大不了我重新上传并发布一次.

这里先说图片上传的操作, **在上传之前拷贝原始博客以及本地和发布线上版本的配置** 可以在 [文章处理](#文章处理) 一节中查看.



```python
import re
import os
import sys
import shutil
import subprocess
from utils import find_all_image_tags, extract_image_url_from_tag, extract_image_urls_from_md, get_all_md_files, find_md_file, is_url

def log(message):
    """
    打印中文日志信息。
    """
    print(f"日志：{message}")

def upload_image(image_path):
    # 使用picgo命令上传图片，并获取输出
    result = subprocess.run(['picgo', 'upload', image_path], capture_output=True, text=True)
    # 提取图床地址，只匹配以https开头的字符串
    url_match = re.search(r'https://[^ ]+', result.stdout)
    if url_match:
        return url_match.group().strip()
    else:
        raise Exception(f"无法从输出中提取图床地址: {result.stdout}")

def replace_image_tags_in_md(md_file, base_dir, publish_dir):
    print(f"正在处理Markdown文件：{md_file}")
    # 计算Markdown文件相对于base_dir的路径
    relative_path = os.path.relpath(md_file, start=base_dir)
    # 构建发布目录下的Markdown文件路径
    publish_md_file = os.path.join(publish_dir, relative_path)
    # 确保发布目录下的子目录存在
    os.makedirs(os.path.dirname(publish_md_file), exist_ok=True)

    # 检查发布目录下的Markdown文件是否已存在
    if os.path.exists(publish_md_file):
        print(f"文件已存在：{publish_md_file}")
        return  # 文件存在，退出函数
    
    # 复制原始Markdown文件到发布目录
    shutil.copyfile(md_file, publish_md_file)

    # 读取发布目录下的Markdown文件内容
    with open(publish_md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取所有图片标签
    image_tags = find_all_image_tags(md_file)

    for tag in image_tags:
        # 从标签中提取图片文件名
        image_name = extract_image_url_from_tag(tag)
        # 如果 image_name 为空字符串，跳过当前循环
        if not image_name or is_url(image_name):
            print(f"标签 {tag} 中未找到有效的图片路径或者已经是图床地址，跳过。")
            continue

        if image_name.startswith('/images'):
            # 图片路径以 /images 开头，需要在 source/images 目录下查找
            source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source')
            image_path = os.path.join(source_dir, 'images', image_name[len('/images'):].lstrip('/'))
        else:
            # 图片路径不是以 /images 开头，直接在文章目录下查找
            image_path = os.path.join(os.path.splitext(md_file)[0] , image_name)

        # 检查图片文件是否存在
        if os.path.isfile(image_path):
            # 上传图片并获取图床地址
            image_url = upload_image(image_path)
            # 只替换括号()内的内容
            new_tag = re.sub(r'\(.*?\)', f'({image_url})', tag)
            content = content.replace(tag, new_tag)
            if image_name.startswith('/images'):
                log(f"替换 cover 图片地址")
                content = content.replace('cover: ' + image_name, 'cover: ' + image_url)
            log(f"替换标签 {tag} 为 {new_tag}")
        else:
            print(f"图片文件不存在: {image_path}")

    # 保存修改后的Markdown文件到发布目录
    with open(publish_md_file, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    # 构建发布目录路径，确保它在source/_posts下
    publish_dir = os.path.join(base_dir, 'publish')
    # 确保发布目录存在
    os.makedirs(publish_dir, exist_ok=True)
    log(f"博客文章的基准目录：{base_dir}")

    # 初始化要处理的Markdown文件列表
    md_files_to_process = []

    if not args:
        # 处理所有Markdown文件
        md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的Markdown文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
        else:
            log(f"年份目录 {args[0]} 不存在。")
            return
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename, exclude_dir='publish')
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到Markdown文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return

    # 循环处理所有确定的Markdown文件
    for md_file in md_files_to_process:
        replace_image_tags_in_md(md_file, base_dir, publish_dir)

    log("==================图片上传完成==================")

if __name__ == "__main__":
    main()

```







## 文章处理

### 创建部署的文档

为什么要这么做



作为 Spring Boot 的老手, Hexo 和 Spring Boot 的配置文件情况差不多: 都是通过 yaml 加载配置且允许存在多个配置(`_config.yml` 和 `_config.[theme].yml`)  类似于 `application.yml` 和 `application-prod.yml`, 那么肯定会存在一个配置优先级以及配置合并的操作, 那么我们可不可以通过不同的配置来实现根据 **根据环境来选择不同的配置从而实现发布不同的博文**?

#### Hexo 配置

在翻看了 Hexo 的官方文档后, 跟我上面的猜想一样, 所以我们首先要了解一下 Hexo 如何加载配置以及配置的优先级.

#### 使用代替配置文件

<!-- 
https://hexo.io/zh-cn/docs/configuration#%E4%BD%BF%E7%94%A8%E4%BB%A3%E6%9B%BF%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6
-->

可以在 hexo-cli 中使用 `--config` 参数来指定自定义配置文件的路径。 你可以使用一个 YAML 或 JSON 文件的路径，也可以使用逗号分隔（无空格）的多个 YAML 或 JSON 文件的路径。

```
# use 'custom.yml' in place of '_config.yml'
$ hexo server --config custom.yml

# use 'custom.yml' & 'custom2.json', prioritizing 'custom2.json'
$ hexo server --config custom.yml,custom2.json
```

当你指定了多个配置文件以后，Hexo 会按顺序将这部分配置文件合并成一个 `_multiconfig.yml`。 后面的值优先。 这个原则适用于任意数量、任意深度的 YAML 和 JSON 文件。 请注意，**列表中不允许有空格**。

如果 `custom.yml` 中指定了 `foo: bar`，在 custom2.json 中指定了 `"foo": "dinosaur"`，那么在 `_multiconfig.yml` 中你会得到 `foo: dinosaur`。

#### 使用代替主题配置文件

通常情况下，Hexo 主题是一个独立的项目，并拥有一个独立的 `_config.yml` 配置文件。

除了自行维护独立的主题配置文件，你也可以在其它地方对主题进行配置。

**配置文件中的 `theme_config`**

> 该特性自 Hexo 2.8.2 起提供

```
# _config.yml
theme: "my-theme"
theme_config:
  bio: "My awesome bio"
  foo:
    bar: "a"
# themes/my-theme/_config.yml
bio: "Some generic bio"
logo: "a-cool-image.png"
  foo:
    baz: 'b'
```

最终主题配置的输出是：

```
{
  "bio": "My awesome bio",
  "logo": "a-cool-image.png",
  "foo": {
    "bar": "a",
    "baz": "b"
  }
}
```

**独立的 `_config.[theme].yml` 文件**

> 该特性自 Hexo 5.0.0 起提供

独立的主题配置文件应放置于站点根目录下，支持 `yml` 或 `json` 格式。 需要配置站点 `_config.yml` 文件中的 `theme` 以供 Hexo 寻找 `_config.[theme].yml` 文件。

```
# _config.yml
theme: "my-theme"
# _config.my-theme.yml
bio: "My awesome bio"
foo:
  bar: "a"
# themes/my-theme/_config.yml
bio: "Some generic bio"
logo: "a-cool-image.png"
  foo:
    baz: 'b'
```

最终主题配置的输出是：

```
{
  "bio": "My awesome bio",
  "logo": "a-cool-image.png",
  "foo": {
    "bar": "a",
    "baz": "b"
  }
}
```

> 我们强烈建议你将所有的主题配置集中在一处。 如果你不得不在多处配置你的主题，那么这些信息对你将会非常有用：Hexo 在合并主题配置时，Hexo 配置文件中的 `theme_config` 的优先级最高，其次是 `_config.[theme].yml` 文件。 最后是位于主题目录下的 `_config.yml` 文件。
>
> `_config.yml.theme_config > _config.[theme].yml > _config.yml`
>
> `hexo server --config _config.yml,_config.[theme].yml`



## 部署到本地服务器



```bash
#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")
# 切换到 Makefile 所在的工作目录 (即脚本所在目录的父目录)
cd "$SCRIPT_DIR/.." || exit 1

# 定义变量
REMOTE_HOST="m920x"
REMOTE_DIR="/opt/1panel/apps/openresty/openresty/www/sites/blog.dong4j.ink/index"
LOCAL_DIR="public" # 脚本同级目录下的 public

# 生成最新的文件
echo "正在执行 hexo clean && hexo g 以生成最新的文件..."
hexo clean && hexo recommend --config _config.yml,_config.anzhiyu.yml,_config.publish.yml && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

# 检查 public 目录是否生成成功
if [ ! -d "$LOCAL_DIR" ]; then
  echo "public 目录生成失败，请检查 Hexo 配置！"
  exit 1
fi

# 上传文件到远程并覆盖
echo "正在上传 public 目录下的所有文件到 $REMOTE_HOST:$REMOTE_DIR..."
rsync -ah --progress --delete \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '__MACOSX' \
  "$LOCAL_DIR/" "$REMOTE_HOST:$REMOTE_DIR" | tee /dev/null

# 检查上传是否成功
if [ $? -eq 0 ]; then
  echo "文件上传成功！"
else
  echo "文件上传失败，请检查连接或权限配置。"
  exit 1
fi
```





## 部署到 GitHub



```bash
# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  - type: git
    repo: https://github.com/dong4j/dong4j.github.io 
    branch: master
```



```bash
hexo deploy	
```



[在 GitHub Pages 上部署 Hexo](https://hexo.io/zh-cn/docs/github-pages)

[使用 Github Action 自动部署](https://blog.anheyu.com/posts/asdx.html)



## 备份



```bash
#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# 切换到 Makefile 所在的工作目录 (即脚本所在目录的父目录)
cd "$SCRIPT_DIR/.." || exit 1

# 使用第一个参数作为提交信息，如果未提供参数，则使用默认信息
COMMIT_MESSAGE=${1:-"摘要生成"}

# 执行 Git 操作
git add .
git commit -m "$COMMIT_MESSAGE"
git push -u github main
git push -u gitee main
#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# 切换到 Makefile 所在的工作目录 (即脚本所在目录的父目录)
cd "$SCRIPT_DIR/.." || exit 1

# 使用第一个参数作为提交信息，如果未提供参数，则使用默认信息
COMMIT_MESSAGE=${1:-"摘要生成"}

# 执行 Git 操作
git add .
git commit -m "$COMMIT_MESSAGE"
git push -u github main
git push -u gitee main
```





## 部署流程化





```bash
# 定义伪目标，避免与文件名冲突
.PHONY: clean_images convert_and_rename upload_images generate_summary_tags push deploy-m920x deploy-github clean

########## 需要终端在 hexo 顶层目录才能正常执行

# 默认目标
all: clean_images convert_and_rename upload_images generate_summary_tags push deploy-m920x deploy-github clean

# 本地运行
dev: 
	@echo "==================Step 5: Deploying application=================="
	hexo clean && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.local.yml && hexo server --config _config.yml,_config.anzhiyu.yml,_config.local.yml

# 删除未被引用的图片, 不传任何参数则全部处理, 传 2023 则只处理 2023 目录下的文件, 传 md 文件名, 则只处理这一个文件
clean_images:
	@echo "==================Step 1: Cleaning images=================="
	python script/clean_images.py

# 将图片转换为 webp 且重命名(年月日时分秒_8位随机字符串.webp)
convert_and_rename: 
	@echo "==================Step 2: Cleaning images=================="
	python script/convert_and_rename.py

# 上传图片
upload_images: 
	@echo "==================Step 3: Cleaning images=================="
	python script/upload_images.py

# 生成摘要和标签
generate_summary_tags: 
	@echo "==================Step 3: Cleaning images=================="
	python script/generate_summary_and_tags_and_replace.py 

# 执行 git-push.sh
push: generate_summary_tags
	@echo "==================Step 4: Pushing changes to Git=================="
	script/git-push.sh "删除重复的文章"

# 执行 deploy.sh
deploy-m920x: push
	@echo "==================Step 5: Deploying application=================="
	script/deploy.sh

# 发布到 github
deploy-github: push
	@echo "==================Step 6: Deploying Github=================="
	hexo deploy

clean:
	@echo "==================Step 7: Cleaning up=================="
	hexo clean && rm -rf .deploy_git
```


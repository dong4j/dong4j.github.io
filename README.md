# 播客

基于 hexo 的静态站点, 主题使用 [aurora](https://github.com/auroral-ui/hexo-theme-aurora), [auarora 文档](https://aurora.tridiamond.tech/cn).

## 搭建

[Mac OS 环境下使用 Hexo 搭建个人博客](https://blog.l3zc.com/2022/05/mac%E7%8E%AF%E5%A2%83%E4%B8%8B%E4%BD%BF%E7%94%A8hexo%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/)

```shell
nvm use 21
npm install -g hexo-cli
hexo init blog
cd blog
npm install
```

这条指令的作用是在你目前所在的目录下（默认是你的 home 目录）新建一个名为 `blog` 的文件夹（你可以将这条命令中的 `blog` 替换成任何你想要的名字），并在内初始化你的博客。  
之后所有的操作都在这个文件夹下进行，请确保在执行后文的操作前已经切换到了这个文件夹（cd blog）。

待初始化完成，切换到 `blog` 文件夹中，即可生成和预览博客。

目录结构:

```shell
.
├── _config.yml     # 全局配置文件
├── package.json    # 项目配置文件
├── scaffolds       # 模板文件夹
├── source          # 资源文件夹
|   ├── _drafts     # 草稿文件夹
|   └── _posts      # 文章文件夹
└── themes          # 主题文件夹
```

[\_config.yml](https://hexo.io/zh-cn/docs/configuration)

网站的 配置 文件。 您可以在此配置大部分的参数。

source

资源文件夹。 是存放用户资源的地方。 除 _posts 文件夹之外，开头命名为 _ (下划线) 的文件 / 文件夹和隐藏的文件将会被忽略。 Markdown 和 HTML 文件会被解析并放到 public 文件夹，而其他文件会被拷贝过去。

### hexo-server

Hexo 3.0 把服务器独立成了个别模块。 您必须先安装 hexo-server 才能使用。

```
$ npm install hexo-server --save
```

安装完成后，输入以下命令以启动服务器。 默认情况下，您的网站会在 <http://localhost:4000> 下启动。 在服务器启动期间，  
Hexo 会监视文件变动并自动更新，您无须重启服务器。

```
$ hexo server
```

如果您想要更改端口，或是在执行时遇到了 EADDRINUSE 错误，可以在执行时使用 -p 选项指定其他端口，如下：

```
$ hexo server -p 5000
```

静态模式  
在静态模式下，服务器只处理 public 文件夹中的文件，并且不会监视文件变化。 您必须在启动服务器之前运行 hexo generate。 通常用于生产环境。

```
$ hexo server -s
```

自定义 IP  
Hexo 服务器默认运行在 0.0.0.0。 您可以覆盖默认的 IP 设置。

```
$ hexo server -i 192.168.1.1
```

### 生成文件

使用 Hexo 生成静态文件快速而且简单。

```
$ hexo generate
```

### 监视文件变动

Hexo 能够监视文件变动并立即重新生成静态文件。 Hexo 在生成时会比对文件的 SHA1 checksum，只有变动的文件才会写入。

```
$ hexo generate --watch
```

### 完成后部署

您可执行下列的其中一个命令，让 Hexo 在生成完毕后自动部署网站。 两个命令的作用是相同的。

```
$ hexo generate --deploy
$ hexo deploy --generate
```

## Hexo 常用命令

```
#注意以下命令需要切换到blog文件夹(cd blog)执行

hexo n "文章名称"  => hexo new "文章名称"  #这两个都是创建新文章，前者是简写模式，下同，new后面加一个draft可以生成草稿
hexo p  => hexo publish  #发布草稿
hexo g  => hexo generate  #生成
hexo s  => hexo server  #启动服务预览
hexo d  => hexo deploy  #部署

hexo server   #Hexo 会监视文件变动并自动更新，无须重启服务器。
hexo server -s   #静态模式
hexo server -p 5000   #更改端口
hexo server -i 192.168.1.1   #自定义IP
hexo clean   #清除缓存，网页正常情况下可以忽略此条命令
```

## 配置

<https://hexo.io/zh-cn/docs/configuration>

## 部署

<https://hexo.io/zh-cn/docs/one-command-deployment>

## 备份

```
hexo clean & hexo g & hexo server
```

## Aurora 主题配置

1. 安装

```
cd hexo
yarn add hexo-theme-aurora hexo-plugin-aurora
```

2. 配置

```
# 在根目录的 _config.yml 文件中添加以下内容
theme: aurora
```

3. 设置 permalink

```
打开在 Hexo 根目录下的 _config.yml
修改 permalink 参数为 /post/:title.html

# URL
## Set your site url here. For example, if you use GitHub Page, set url as 'https://username.github.io/project'
url: https://tridiamond.tech
permalink: /post/:title.html
permalink_defaults:
pretty_urls:
  trailing_index: true # Set to false to remove trailing 'index.html' from permalinks
  trailing_html: true # Set to false to remove trailing '.html' from permalinks
```

5. 代码高亮

```
1. 需要禁用 _config.yml 中的 highlight 和 prismjs
2. 在主题配置文件中添加 highlight

shiki:
  enable: true
  backgroundColor: '#1a1a1a'
```

6. about 页面

```
hexo new page about
```

7. 启动

```
hexo c & hexo g & hexo s
```

## 图片设置

1. 显示图片: 图片放入与 md 文档同名的目录
2. 图片居中显示:

```css
.post-html img {
  margin: auto;
  cursor: zoom-in;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 0.15s;
}
```

# TODO

1. 文章元数据修改
2. 文章 banner
3. 检查图片链接
   1. 读取每一篇 md 文件, 解析文件中的 图片链接
   2. 在当前目录查找同名目录, 与文档中的图片链接进行对比
   3. 如果没有找到, 则输出文档完整路径和图片链接文本;
   4. 最后还要清理同名目录下未被引用的图片

# 安知鱼 标签体系

https://blog.anheyu.com/posts/d50a.html

---
title: 备忘录
date: 2020-06-07 22:17:49
type: "Others"
aside: false
top_img: false
---

## Note (Bootstrap Callout)

{% note default %} Content (md partial supported) {% endnote %}
{% note primary %} Content (md partial supported) {% endnote %}
{% note success %} Content (md partial supported) {% endnote %}
{% note info %} Content (md partial supported) {% endnote %}
{% note warning %} Content (md partial supported) {% endnote %}
{% note danger %} Content (md partial supported) {% endnote %}

## 版权

如果有文章（例如：转载文章）不需要显示版权，可以在文章 Front-matter 单独设置

```yaml
copyright: false
```

对单独文章设置版权信息，可以在文章 Front-matter 单独设置

```yaml
copyright_author: xxxx
copyright_author_href: https://xxxxxx.com
copyright_url: https://xxxxxx.com
copyright_info: 此文章版权归xxxxx所有，如有转载，请注明来自原作者
```

## 图标配置

AnZhiYu 支持 [阿里图标](https://www.iconfont.cn/collections/detail?cid=44481) (需配置自己的图标)，与 [font-awesome v6](https://fontawesome.com/icons?from=io) 图标(需开启`fontawesome`)，使用阿里图标需配置主题配置文件中`icon.ali_iconfont_js`字段，默认内置部分图标，修改主题配置文件，视频教程: [安知鱼主题社交图标配置](https://www.bilibili.com/video/BV1Cv4y1n7FW/?spm_id_from=333.999.0.0&vd_source=4d9717102296e4b7a60ecdfad55ae2dd)

```yaml
icons:
  ali_iconfont_js: # 阿里图标 symbol 引用链接，主题会进行加载 symbol 引用
  fontawesome: false #是否启用 fontawesome6 图标
  fontawesome_animation_css: #fontawesome_animation 如果有就会加载，示例值：https://npm.elemecdn.com/hexo-butterfly-tag-plugins-plus@1.0.17/lib/assets/font-awesome-animation.min.css
```

内置阿里图标库：https://www.iconfont.cn/collections/detail?cid=44481

使用方法，将图标库中的图标名复制，然后加上前缀`anzhiyu-icon-`即可，比如`github`图标，则为`anzhiyu-icon-github`。

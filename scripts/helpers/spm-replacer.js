"use strict";

// 将 https://api.dong4j.ink:1024/cover?spm={{spm}} 中的 {{spm}} 替换为随机字符串, 以处理进入 post 页面时头图不刷新的问题
hexo.extend.filter.register("before_post_render", function (data) {
  // 如果是 post 或 page，才处理
  if (data.source.startsWith("_drafts/") || data.layout === "post" || data.layout === "page") {
    // 正则匹配 {{spm}} 占位符
    const spmPattern = /{{spm}}/g;

    // 生成 8 位随机字符串
    const generateRandomString = () => {
      return Math.random().toString(36).substring(2, 10); // 基数 36，提取 8 个字符
    };

    // 替换 {{spm}} 为随机字符串
    if (spmPattern.test(data.content)) {
      data.content = data.content.replace(spmPattern, generateRandomString);
      // hexo.log.info("Replaced {{spm}} in %s", data.source);
    }
  }

  // 返回处理后的数据
  return data;
});

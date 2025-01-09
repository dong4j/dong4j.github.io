// 分享本页
function share() {
  let url = window.location.origin + window.location.pathname;
  new ClipboardJS(".share", {
    text: function () {
      return "标题：" + document.title + "\n链接：" + url;
    },
  });
  anzhiyu.snackbarShow("本页链接已复制到剪切板，快去分享吧.");
}

// hexo-blog-decrypt 解密之后重新刷新页面才能显示图片
function handleHexoBlogDecryptEvent() {
  // 刷新页面
  window.location.reload();
}

// 添加事件监听器
window.addEventListener("hexo-blog-decrypt", handleHexoBlogDecryptEvent);

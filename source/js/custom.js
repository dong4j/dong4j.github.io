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

function loadStylesheet(href) {
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = href;
  document.head.appendChild(link);
}

function loadScript(src, async = true) {
  const script = document.createElement('script');
  script.src = src;
  script.async = async;
  document.body.appendChild(script);
}

function isMobileDevice() {
  const userAgent = navigator.userAgent || navigator.vendor || window.opera;
  return /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(userAgent.toLowerCase());
}

if (!isMobileDevice()) {
  // 如果不是移动设备，动态加载CSS和JS文件
  loadStylesheet('https://cdn.dong4j.site/source/static/dify-chat.css');
  loadScript('https://cdn.dong4j.site/source/static/dify-chat.embed.min.js');
  loadScript('https://cdn.dong4j.site/source/static/dify-chat.js');
}

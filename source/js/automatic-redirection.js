// https://blog.meta-code.top/2024/10/27/2024-15/

function shouldRedirect(hostname) {
  var hostname0 = "localhost";
  var hostname1 = "127.0.0.1";
  var hostname2 = "dong4j.github.io";
  var hostname5 = "blog.dong4j.site";
  // var localNetworkByUnic = "192.168.21.";
  var localNetworkbyTele = "192.168.31.";

  // 检查主机名是否为本地局域网地址
  function isLocalNetwork(hostname) {
    return (
      hostname.startsWith(localNetworkbyTele)
    );
  }

  // 判断是否需要跳转
  if (
    hostname !== hostname0 &&
    hostname !== hostname1 &&
    hostname !== hostname2 &&
    hostname !== hostname5 &&
    !isLocalNetwork(hostname)
  ) {
    return true; // 需要跳转
  }
  return false; // 不需要跳转
}

// https://owo.wyc.rest/redirect/
function redirect() {
  // 获取当前网页的 URL
  var currentUrl = window.location.href;
  // 检查是否包含 "/index.html"
  if (currentUrl.includes("/index.html")) {
      // 定义重定向的目标 URL 格式
      var redirectTo = currentUrl.replace(/\/index\.html$/, '/');
      // 进行重定向
      window.location.replace(redirectTo);
  }
}

var hostnameNow = document.location.hostname;
if (shouldRedirect(hostnameNow)) {
  var sourceDomain = "https://blog.dong4j.site";
  window.location.href = sourceDomain + document.location.pathname;
}

redirect()
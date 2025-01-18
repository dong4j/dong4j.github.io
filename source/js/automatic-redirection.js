// https://blog.meta-code.top/2024/10/27/2024-15/

function shouldRedirect(hostname) {
  var hostname0 = "localhost";
  var hostname1 = "127.0.0.1";
  var hostname2 = "dong4j.github.io";
  var hostname5 = "blog.dong4j.site";
  var localNetworkPrefix1 = "192.168.21.";
  var localNetworkPrefix2 = "192.168.31.";

  // 检查主机名是否为本地局域网地址
  function isLocalNetwork(hostname) {
    return (
      hostname.startsWith(localNetworkPrefix1) ||
      hostname.startsWith(localNetworkPrefix2)
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

// 使用方法
var hostnameNow = document.location.hostname;
if (shouldRedirect(hostnameNow)) {
  var sourceDomain = "https://blog.dong4j.site";
  window.location.href = sourceDomain + document.location.pathname;
}

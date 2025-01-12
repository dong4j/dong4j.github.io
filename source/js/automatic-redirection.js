var hostname0 = "localhost";
var hostname1 = "127.0.0.1";
var hostname2 = "dong4j" + "." + "github" + "." + "io";
var hostname3 = "blog" + "." + "dong4j" + ".ink:1024";
var hostname4 = "blog" + "." + "dong4j" + ".ink";
var hostname5 = "blog" + "." + "dong4j" + ".site";
var hostname6 = "www" + "." + "dong4j" + ".site";
var hostname7 = "dong4j" + "." +  "site";
var hostnameNow = document.location.hostname;
var localNetworkPrefix1 = "192.168.21.";
var localNetworkPrefix2 = "192.168.31.";

// 检查当前主机名是否为本地局域网地址
function isLocalNetwork(hostname) {
  return (
    hostname.startsWith(localNetworkPrefix1) ||
    hostname.startsWith(localNetworkPrefix2)
  );
}

if (
  hostnameNow !== hostname0 &&
  hostnameNow !== hostname1 &&
  hostnameNow !== hostname2 &&
  hostnameNow !== hostname3 &&
  hostnameNow !== hostname4 &&
  hostnameNow !== hostname5 &&
  hostnameNow !== hostname6 &&
  hostnameNow !== hostname7 &&
  !isLocalNetwork(hostnameNow)
) {
  var sourceDomain = "https://" + hostname5;
  window.location.href = sourceDomain + document.location.pathname;
}

// https://blog.meta-code.top/2024/10/27/2024-15/

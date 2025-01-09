var hostname1 = 'dong4j' + '.' + 'github' + '.' + 'io';
var hostname2 = 'blog' + '.' + 'dong4j' + '.ink:1024';
var hostname3 = 'blog' + '.' + 'dong4j' + '.ink';
var hostname5 = 'blog' + '.' + 'dong4j' + '.site';
var hostname4 = 'localhost';
var hostnameNow = document.location.hostname;
var localNetworkPrefix1 = '192.168.21.';
var localNetworkPrefix2 = '192.168.31.';

// 检查当前主机名是否为本地局域网地址
function isLocalNetwork(hostname) {
  return hostname.startsWith(localNetworkPrefix1) || hostname.startsWith(localNetworkPrefix2);
}

if (hostnameNow !== hostname1 && hostnameNow !== hostname2 && hostnameNow !== hostname3 && hostnameNow !== hostname5 && hostnameNow !== hostname4 && !isLocalNetwork(hostnameNow)) {
  var sourceDomain = 'https://' + hostname1;
  window.location.href = sourceDomain + document.location.pathname;
}

// https://blog.meta-code.top/2024/10/27/2024-15/
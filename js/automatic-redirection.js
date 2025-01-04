var hostname1 = 'dong4j' + '.' + 'github' + '.' + 'io'
var hostname2 = 'blog' + '.' + 'dong4j' + '.ink:1024'
var hostname3 = 'blog' + '.' + 'dong4j' + '.ink'
var hostname4 = 'localhost'
var hostnameNow = document.location.hostname
if (hostnameNow !== hostname1 && hostnameNow !== hostname2 && hostnameNow !== hostname3 && hostnameNow !== hostname4) {
	var sourceDomain = 'https://' + hostname1
	window.location.href = sourceDomain + document.location.pathname
}

// https://blog.meta-code.top/2024/10/27/2024-15/
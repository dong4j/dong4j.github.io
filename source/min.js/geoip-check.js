var foreignTips=function(){var o=function(o){o.country.iso_code&&("cn"!=o.country.iso_code.toLowerCase()&&btf.snackbarShow("使用国外网络访问将无法访问文章图片，敬请谅解。If you use foreign network access, you will not be able to access articles and pictures."))},n=function(o){};return function(){geoip2.country(o,n)}}();foreignTips();
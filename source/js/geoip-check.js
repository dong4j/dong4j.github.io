// todo 未生效
var foreignTips = (function () {
    var onSuccess = function (geoipResponse) {
      if (!geoipResponse.country.iso_code) {
        return;
      }
      var code = geoipResponse.country.iso_code.toLowerCase();
      console.log('geoipResponse: ' + code)
      if (code != 'cn'){
        anzhiyu.snackbarShow('使用国外网络访问将无法访问文章图片，敬请谅解。If you use foreign network access, you will not be able to access articles and pictures.')
        window.open('/denyaccess/', '_blank', 'noopener,noreferrer');
      }
    };
    var onError = function (error) {
    };
    return function () {
      geoip2.country(onSuccess, onError);
    };
  }());
  foreignTips();
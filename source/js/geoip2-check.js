var foreignTips = (async function () {
  // 异步的成功处理函数
  var onSuccess = function (geoipResponse) {
    if (!geoipResponse.country_iso_code) {
      return;
    }
    var code = geoipResponse.country_iso_code.toLowerCase();
    console.log("geoipResponse: " + code);
    if (code !== "cn") {
    //   anzhiyu.snackbarShow(
    //     "使用国外网络访问将无法访问文章图片，敬请谅解。If you use foreign network access, you will not be able to access articles and pictures."
    //   );

      // todo 检查站点, 跳转到主站 dong4j.github.io
      // 使用方法
      if (shouldRedirect(document.location.hostname)) {
        window.location.href =
          "https://dong4j.github.io" + document.location.pathname;
      }
    } else {
      // todo 检查站点, 跳转到主站 blog.dong4j.site
      if (shouldRedirect(document.location.hostname)) {
        window.location.href =
          "https://blog.dong4j.site" + document.location.pathname;
      }
    }
  };

  // 错误处理函数
  var onError = function (error) {
    console.error("GeoIP API 请求失败:", error);
  };

  // 获取用户 IP 地址
  var ip = "113.68.255.182"; // 需要用实际的 IP 地址替换

  // 异步请求接口获取 GeoIP 信息
  try {
    const response = await fetch(`http://127.0.0.1:12341/ip/${ip}`);
    const geoipData = await response.json();
    onSuccess(geoipData); // 处理返回的数据
  } catch (error) {
    onError(error); // 如果请求失败，调用错误处理函数
  }
})();

// 注意：此代码不会阻塞其他 JavaScript 执行

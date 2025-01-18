var foreignTips = (async function () {
  // 异步的成功处理函数
  var onSuccess = function (geoipResponse) {
    if (!geoipResponse.country_iso_code) {
      return;
    }
    var code = geoipResponse.country_iso_code.toLowerCase();
    console.log("geoipResponse: " + code);
    if (code !== "cn") {
      if (shouldRedirect(document.location.hostname)) {
        anzhiyu.snackbarShow(
          "使用国外网络访问: 为你跳转到 Github Pages。If you use foreign network access, you will be redirected to Github Pages."
        );
        window.location.href =
          "https://dong4j.github.io" + document.location.pathname;
      }
    } else {
      if (shouldRedirect(document.location.hostname)) {
        anzhiyu.snackbarShow(
          "使用国内网络访问: 为你跳转到主站。If you use Chinese network access, you will be redirected to main site."
        );
        window.location.href =
          "https://blog.dong4j.site" + document.location.pathname;
      }
    }
  };

  // 错误处理函数
  var onError = function (error) {
    console.error("GeoIP API 请求失败:", error);
  };

  var ip = "";
  try {
    const ipData = await fetch("https://api.ipify.org?format=json");
    const ipJson = await ipData.json();
    var ip = ipJson.ip;
  } catch (error) {
    ip = "127.0.0.1";
  }
  // 异步请求接口获取 GeoIP 信息
  try {
    const response = await fetch(
      `https://api.dong4j.ink:1024/location?ip=${ip}`
    );
    const geoipData = await response.json();
    onSuccess(geoipData); // 处理返回的数据
  } catch (error) {
    onError(error); // 如果请求失败，调用错误处理函数
  }
})();

// 注意：此代码不会阻塞其他 JavaScript 执行

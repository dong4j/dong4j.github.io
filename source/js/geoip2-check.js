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

  // 尝试从本地存储获取 IP 地址
  var ip = localStorage.getItem("public_ip");
  // 如果本地存储中没有 IP 地址，则调用接口获取
  if (!ip) {
    try {
      const ipData = await fetch("https://api.ipify.org?format=json");
      const ipJson = await ipData.json();
      ip = ipJson.ip;
      // 将获取到的 IP 地址存储到本地存储中
      localStorage.setItem("public_ip", ip);
    } catch (error) {
      ip = "127.0.0.1";
    }
  }
  // 异步请求接口获取 GeoIP 信息
  try {
    const response = await fetch(
      `https://api.dong4j.ink:1024/location?ip=${ip}`
    );
    const geoipData = await response.json();
    onSuccess(geoipData); // 处理返回的数据
  } catch (error) {
    // 第一个接口调用失败，调用备用接口
    try {
      const ipinfoResponse = await fetch(
        `https://ipinfo.io/${ip}?token=46be037bff8c46`
      );
      const ipinfoData = await ipinfoResponse.json();

      // 将 country 字段重命名为 country_iso_code
      geoipData = {
        ...ipinfoData,
        country_iso_code: ipinfoData.country,
      };
    } catch (ipinfoError) {
      onError(error); // 如果请求失败，调用错误处理函数
    }
  }
})();

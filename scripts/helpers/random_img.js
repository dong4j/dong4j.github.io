"use strict";

hexo.extend.filter.register(
  "before_post_render",
  function (data) {
    const { config } = this;

    if (config.post_asset_folder) {
      const imgTestReg = /\.(png|jpe?g|gif|svg|webp)(\?.*)?$/;
      const topImg = data.top_img;
      const cover = data.cover;
      if (topImg && topImg.indexOf("/") === -1 && imgTestReg.test(topImg))
        data.top_img = data.path + topImg;
      if (cover && cover.indexOf("/") === -1) data.cover = data.path + cover;
    }

    if (data.cover === false) {
      data.randomcover = randomCover();
      return data;
    }
    data.cover = data.cover || randomCover();
    return data;
  },
  0
);

function randomCover() {
  const theme = hexo.theme.config;
  let cover;
  let num;

  if (theme.cover && theme.cover.default_cover) {
    if (!Array.isArray(theme.cover.default_cover)) {
      cover = theme.cover.default_cover;
    } else {
      num = Math.floor(Math.random() * theme.cover.default_cover.length);
      cover = theme.cover.default_cover[num];
    }
  } else {
    cover =
      theme.default_top_img ||
      "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
  }
  if (theme.cover.suffix) {
    if (theme.cover.suffix == 1)
      cover = cover + ("?" + Math.random().toString(36).substring(2, 10));
    else if (theme.cover.suffix == 2)
      cover = cover + ("&" + Math.random().toString(36).substring(2, 10));
  }
  // hexo.log.info("random cover:", cover);
  return cover;
}

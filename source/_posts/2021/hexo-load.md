---
title: 个性化加载动画，让你的 Hexo 博客更炫酷！
ai:
  - 本文介绍了如何在 anzhiyu 主题下添加和自定义加载动画。文章详细描述了如何创建不同的加载动画模板（如小汽车、旋转齿轮等），并通过配置文件选择相应的样式。此外，还提供了相关的代码示例，包括
    CSS 样式和 JavaScript 逻辑。最后，文章也提到了如何通过修改主题配置来切换加载动画的样式。
categories:
  - 经验分享
tags:
  - anzhiyu 主题
  - 自定义加载动画
  - Hexo博客
  - Butterfly主题
date: 2021-07-12 00:00:00
cover: /images/cover/20250103184959_iDTIF6Dq.webp
description: 本文介绍了如何在 anzhiyu 主题下添加和自定义加载动画。文章详细描述了如何创建不同的加载动画模板（如小汽车、旋转齿轮等），并通过配置文件选择相应的样式。此外，还提供了相关的代码示例，包括
  CSS 样式和 JavaScript 逻辑。最后，文章也提到了如何通过修改主题配置来切换加载动画的样式。
keywords:
  - anzhiyu 主题
  - 自定义加载动画
  - Hexo博客
  - Butterfly主题
---

![/images/cover/20250103184959_iDTIF6Dq.webp](/images/cover/20250103184959_iDTIF6Dq.webp)

参考 [【Hexo博客】自定义Butterfly主题 Loading 加载动画](https://blog.meta-code.top/2022/06/18/2022-73/) 和 [Hexo的Butterfly下自定义加载动画之小汽车动画的实现](https://blog.zhheo.com/p/32776e99.html) 实现了在 anzhiyu 主题下的自定义加载动画。

## 添加 loading 模版

新建目录: `themes/anzhiyu/layout/includes/loading/load_style`, 添加如下 pug:

{% tabs loading template %}

<!-- tab car.pug -->

```javascript
#loading-box
  .carplay

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)

  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})

  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab default.pug -->

```javascript
#loading-box
  .loading-left-bg
  .loading-right-bg
  .spinner-box
    .configure-border-1
      .configure-core
    .configure-border-2
      .configure-core
    .loading-word= _p('loading')

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab gear.pug -->

```javascript
#loading-box
  .gear-loader
    .gear-loader_overlay
    .gear-loader_cogs
      .gear-loader_cogs__top
        .gear-top_part
        .gear-top_part
        .gear-top_part
        .gear-top_hole
      .gear-loader_cogs__left
        .gear-left_part
        .gear-left_part
        .gear-left_part
        .gear-left_hole
      .gear-loader_cogs__bottom
        .gear-bottom_part
        .gear-bottom_part
        .gear-bottom_part
        .gear-bottom_hole

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab heo.pug -->

```javascript
- loading_img = theme.preloader.avatar ? theme.preloader.avatar : theme.avatar.img
#loading-box(onclick='document.getElementById("loading-box").classList.add("loaded")')
  .loading-bg
    img.loading-img(alt="加载头像" class='nolazyload' src=url_for(loading_img))
    .loading-image-dot
script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }
  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)

  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }

```

<!-- endtab -->

<!-- tab image.pug -->

```javascript
- var loadimage = theme.preloader.load_image ? theme.preloader.load_image : theme.error_img.post_page
#loading-box
  .loading-left-bg
  .loading-right-bg
  img.load-image(src=url_for(loadimage) alt='')

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab ironheart.pug -->

```javascript
#loading-box
  .loading-left-bg
  .loading-right-bg
  .iron-container.iron-circle
    .iron-box1.iron-circle.iron-center
    .iron-box2.iron-circle.iron-center
    .iron-box3.iron-circle.iron-center
    .iron-box4.iron-circle.iron-center
    .iron-box5.iron-circle.iron-center
    .iron-box6.iron-circle
      .iron-coil(style='--i: 0')
      .iron-coil(style='--i: 1')
      .iron-coil(style='--i: 2')
      .iron-coil(style='--i: 3')
      .iron-coil(style='--i: 4')
      .iron-coil(style='--i: 5')
      .iron-coil(style='--i: 6')
      .iron-coil(style='--i: 7')

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab pace.pug -->

```javascript
link(rel="stylesheet", href=url_for(theme.preloader.pace_css_url || theme.asset.pace_default_css))
script(async src=url_for(theme.asset.pace_js), data-pace-options='{ "restartOnRequestAfter":false,"eventLag":false}')
```

<!-- endtab -->

<!-- tab scarecrow.pug -->

```javascript
#loading-box
  .loading-left-bg
  .loading-right-bg
  .scarecrow
    .scarecrow__hat
      .scarecrow__ribbon
    .scarecrow__head
      .scarecrow__eye
      .scarecrow__eye
      .scarecrow__mouth
      .scarecrow__pipe
    .scarecrow__body
      .scarecrow__glove.scarecrow__glove--l
      .scarecrow__sleeve.scarecrow__sleeve--l
      .scarecrow__bow
      .scarecrow__shirt
      .scarecrow__coat
      .scarecrow__waistcoat
      .scarecrow__sleeve.scarecrow__sleeve--r
      .scarecrow__glove.scarecrow__glove--r
      .scarecrow__coattails
      .scarecrow__pants
    .scarecrow__arms
    .scarecrow__leg   

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab triangles.pug -->

```javascript
#loading-box
  .triangles-wrap
    .triangles-eiz
    .triangles-seiz
    .triangles-sei
    .triangles-fei
    .triangles-feir
    .triangles-trei
    .triangles-dvai
    .triangles-ein
    .triangles-zero


script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

<!-- tab wizard.pug -->

```javascript
#loading-box
  .loading-left-bg
  .loading-right-bg
  .wizard-scene
    .wizard-objects
      .wizard-square
      .wizard-circle
      .wizard-triangle
    .wizard
      .wizard-body
      .wizard-right-arm
        .wizard-right-hand
      .wizard-left-arm
        .wizard-left-hand
      .wizard-head
        .wizard-beard
        .wizard-face
          .wizard-adds
        .wizard-hat
          .wizard-hat-of-the-hat
          .wizard-four-point-star.--first
          .wizard-four-point-star.--second
          .wizard-four-point-star.--third

script.
  const preloader = {
    endLoading: () => {
      document.getElementById('loading-box').classList.add("loaded");
    },
    initLoading: () => {
      document.getElementById('loading-box').classList.remove("loaded")
    }
  }

  window.addEventListener('load',()=> { preloader.endLoading() })
  setTimeout(function(){preloader.endLoading();},10000)
  document.getElementById('loading-box').addEventListener('click',()=> {preloader.endLoading()})
  
  if (!{theme.pjax && theme.pjax.enable}) {
    document.addEventListener('pjax:send', () => { preloader.initLoading() })
    document.addEventListener('pjax:complete', () => { preloader.endLoading() })
  }
```

<!-- endtab -->

{% endtabs %}

## 修改 loading 配置

修改 `themes/anzhiyu/layout/includes/loading/index.pug`

```javascript
if theme.preloader.source === 'heo'
  include ./load_style/heo.pug
else if theme.preloader.source === 'car'
  include ./load_style/car.pug
else if theme.preloader.source === 'gear'
  include ./load_style/gear.pug
else if theme.preloader.source === 'ironheart'
  include ./load_style/ironheart.pug
else if theme.preloader.source === 'scarecrow'
  include ./load_style/scarecrow.pug
else if theme.preloader.source === 'triangles'
  include ./load_style/triangles.pug
else if theme.preloader.source === 'wizard'
  include ./load_style/wizard.pug
else if theme.preloader.source === 'image'
  include ./load_style/image.pug
else if theme.preloader.source === 'default'
  include ./load_style/default.pug
else
  include ./load_style/heo.pug

include ./load_style/pace.pug
```

## 添加 loading 样式模版

新建动画样式模板存放的文件夹，如无特别提示，所有动画样式均存放在 `themes/anzhiyu/layout/includes/loading/load_style` 目录下:

{% tabs loading style template %}

源文件来自于: [Hexo的Butterfly下自定义加载动画之小汽车动画的实现](https://blog.zhheo.com/p/32776e99.html), 不过做了相应适配, 可直接使用这里的样式.

<!-- tab car.css -->

```css
.carplay {
  box-sizing: border-box;

  --black: #1a1c20;
  --white: #fff;
  --green: #00c380;
  --d-green: #019b66;
  --gray: #c1c1c1;
  --l-gray: #c4c4c4;
  --m-gray: #373838;
  --d-gray: #282724;
  --d-blue: #202428;
  --orange: #ef6206;
  --yellow: #dfa500;
  --l-yellow: #deb953;
  --light: #fbfbfb;
  --n-road: -4em;
  --p-road: 7em;

  background-color: var(--green);
}

.carplay *,
.carplay *::before,
.carplay *::after {
  box-sizing: inherit;
}

.carplay::before,
.carplay::after {
  content: " ";
  position: absolute;
  z-index: 1002;
}

.carplay {
  margin: 0;
  height: 100vh;
  display: flex;
  overflow: hidden;
  position: relative;
  align-items: center;
  justify-content: center;
  background-repeat: no-repeat;
  animation: car 3.5s cubic-bezier(0.57, 0.63, 0.49, 0.65) infinite;

  background-image: 


    /* ===rubber-l */ radial-gradient(
      circle at 49% 117%,
      var(--black) 37%,
      transparent 38%
    ),
    radial-gradient(circle at -24% 50%, var(--white) 31%, transparent 49%),
    radial-gradient(2.95em 2.5em at 52% 1.2%, var(--black) 37%, transparent 38%),
    radial-gradient(2.95em 2.5em at 52% 1.2%, var(--black) 37%, transparent 38%),
    linear-gradient(var(--black) 100%, transparent 0),
    /* rubber-l=== */ /* ===rubber-r */
      radial-gradient(circle at 49% 117%, var(--black) 37%, transparent 38%),
    radial-gradient(circle at 124% 50%, var(--white) 31%, transparent 49%),
    radial-gradient(2.95em 2.5em at 48% 1.2%, var(--black) 37%, transparent 38%),
    radial-gradient(2.95em 2.5em at 48% 1.2%, var(--black) 37%, transparent 38%),
    linear-gradient(var(--black) 100%, transparent 0),
    /* rubber-r=== */ /* ===shadow */
      linear-gradient(var(--d-green) 100%, transparent 0);

  /* shadow=== */

  background-size: 


    /* ===rubber-l */ 2.5em 2.5em, 0.7em 0.6em, 2.5em 0.9em,
    2.5em 0.9em, 1.95em 3.9em, /* rubber-l=== */ /* ===rubber-r */ 2.5em 2.5em,
    0.7em 0.6em, 2.5em 0.9em, 2.5em 0.9em, 1.95em 3.9em,
    /* rubber-r=== */ /* ===shadow */ 13em 0.9em;

  /* shadow=== */

  background-position: 


    /* ===rubber-l */ calc(50% - 6.4em) calc(50% - 1.7em),
    calc(50% - 5.26em) calc(50% - -3.4em), calc(50% - 6.5em) calc(50% - -3.8em),
    calc(50% - 4.3em) calc(50% - -3.2em), calc(50% - 6.58em) calc(50% - -1.5em),
    /* rubber-l=== */ /* ===rubber-r */ calc(50% - -6.45em) calc(50% - 1.7em),
    calc(50% - -5.26em) calc(50% - -3.4em),
    calc(50% - -6.5em) calc(50% - -3.8em), calc(50% - -4.3em) calc(50% - -3.2em),
    calc(50% - -6.58em) calc(50% - -1.5em),
    /* rubber-r=== */ /* ===shadow */ center calc(50% - -3.8em);

  /* shadow=== */
}

.carplay::before {
  width: 15.5em;
  height: 62.9em;
  top: calc(50% - 26.2em);
  background-size: 24.6% 491%;
  background-repeat: no-repeat;
  background-position: center 0;
  animation: line 1.5s infinite linear, move-road 3.5s infinite linear;
  transform: perspective(311px) rotateX(83deg)
    translate3d(var(--n-road), -11.975em, 0);
  background-image: repeating-linear-gradient(
    to top,
    var(--white),
    var(--white) 4.6%,
    transparent 0,
    transparent 13.01%
  );
}

.carplay::after {
  width: 15.2em;
  height: 13.2em;
  top: calc(50% - 8.8em);
  left: calc(50% - 7.55em);
  background-repeat: no-repeat;
  animation: light 1s linear infinite, shake 3.5s linear infinite;

  background-image: 

    /* ===ceiling */ radial-gradient(
      58em 20em at 50% 215%,
      transparent 20%,
      var(--white) 20.5%,
      var(--white) 20.8%,
      var(--green) 21.5%
    ),
    /* ceiling=== */ /* ===antenna */
      radial-gradient(circle at center 100%, var(--black) 30%, transparent 0),
    /* antenna=== */ /* ===antenna */
      linear-gradient(var(--white) 100%, transparent 0),
    /* antenna=== */ /* ===glass-l */
      radial-gradient(
        17.8em 37em at 70% 240%,
        var(--black) 30%,
        transparent 30.5%
      ),
    /* glass-l=== */ /* ===glass-r */
      radial-gradient(
        17.8em 37em at 31% 240%,
        var(--black) 30%,
        transparent 30.5%
      ),
    /* glass-r=== */ /* ===light */
      radial-gradient(
        circle,
        var(--light) 48%,
        var(--black) 52%,
        var(--black) 59%,
        transparent 62%
      ),
    /* light=== */ /* ===light */
      radial-gradient(
        circle,
        var(--light) 48%,
        var(--black) 52%,
        var(--black) 59%,
        transparent 62%
      ),
    /* light=== */ /* ===hood-ro */
      radial-gradient(1em 1em at 102% 100%, var(--m-gray) 28%, #f3f3f3 30%),
    /* hood-ro=== */ /* ===hood-ro */
      radial-gradient(1em 1em at 97% -7%, var(--m-gray) 28%, var(--l-gray) 30%),
    /* hood-ro=== */ /* ===hood-ro */
      radial-gradient(1em 1em at -6% 102%, var(--m-gray) 28%, #efefef 30%),
    /* hood-ro=== */ /* ===hood-ro */
      radial-gradient(1em 1em at -6% -1%, var(--m-gray) 28%, var(--l-gray) 30%),
    /* hood-ro=== */ /* ===hood-f */
      linear-gradient(
        to top,
        var(--m-gray) 50%,
        var(--d-gray) 0,
        var(--d-gray) 58%,
        var(--m-gray) 0
      ),
    /* hood-f=== */ /* ===hood-e */
      linear-gradient(
        to top,
        var(--l-gray) 30%,
        var(--white) 100%,
        transparent 0
      ),
    /* hood-e=== */ /* ===hood-l */
      radial-gradient(
        16.4em 30.1em at 209% 333%,
        var(--white) 30%,
        transparent 30.2%
      ),
    /* hood-l=== */ /* ===hood-r */
      radial-gradient(
        16.4em 30.1em at -109% 333%,
        var(--white) 30%,
        transparent 30.2%
      ),
    /* hood-r=== */ /* ===hood-o */
      linear-gradient(var(--gray) 100%, transparent 0),
    /* hood-o=== */ /* ===hood */
      linear-gradient(var(--white) 100%, transparent 0),
    /* hood=== */ /* ===mirror */
      radial-gradient(6.7em 2.5em at 154% 8%, var(--black) 30%, transparent 33%),
    /* mirror=== */ /* ===mirror */
      radial-gradient(6.7em 2.5em at -53% 8%, var(--black) 30%, transparent 33%),
    /* mirror=== */ /* ===guide-l */
      linear-gradient(var(--orange) 100%, transparent 0),
    /* guide-l=== */ /* ===guide-r */
      linear-gradient(var(--orange) 100%, transparent 0),
    /* guide-r=== */ /* ===plaque */
      linear-gradient(var(--yellow) 100%, transparent 0),
    /* plaque=== */ /* ===plaque */
      linear-gradient(var(--l-yellow) 100%, transparent 0),
    /* plaque=== */ /* ===bumper */
      linear-gradient(var(--d-blue) 100%, transparent 0),
    /* bumper=== */ /* ===bumper-l */
      radial-gradient(circle at 124% 39%, var(--d-blue) 60%, transparent 64%),
    /* bumper-l=== */ /* ===bumper-r */
      radial-gradient(circle at -44% 39%, var(--d-blue) 60%, transparent 64%),
    /* bumper-r=== */ /* ===bumper-d */
      radial-gradient(
        13.2em 2em at 50% 59%,
        var(--l-gray) 96%,
        transparent 100%
      ),
    /* bumper-d=== */ /* ===bumper-l */
      radial-gradient(
        1.6em 1.6em at 75% -9%,
        var(--l-gray) 60%,
        transparent 64%
      ),
    /* bumper-l=== */ /* ===bumper-r */
      radial-gradient(
        1.6em 1.6em at 15% -9%,
        var(--l-gray) 60%,
        transparent 64%
      ),
    /* bumper-r=== */ /* ===floor */
      linear-gradient(var(--d-blue) 100%, transparent 0),
    /* floor=== */ /* ===floor-l */
      radial-gradient(
        6.9em 4.6em at 295% 3%,
        var(--d-blue) 30%,
        transparent 31%
      ),
    /* floor-l=== */ /* ===floor-r */
      radial-gradient(
        6.9em 4.6em at -189% 3%,
        var(--d-blue) 30%,
        transparent 31%
      );

  /* floor-r=== */

  background-size: 

    /*=== ceiling */ 61.5% 20%,
    /* ceiling=== */ /* ===antenna */ 5% 6%,
    /* antenna=== */ /*=== antenna */ 0.4% 39%,
    /* antenna=== */ /* ===glass-l */ 60% 30%,
    /* glass-l=== */ /* ===glass-r */ 60% 30%,
    /* glass-r=== */ /* ===light */ 16% 16%,
    /* light=== */ /* ===light */ 16% 16%,
    /* light=== */ /* ===hood-ro */ 2.4% 2%,
    /* hood-ro=== */ /* ===hood-ro */ 2.4% 2.3%,
    /* hood-ro=== */ /* ===hood-ro */ 2.4% 2.3%,
    /* hood-ro=== */ /* ===hood-ro */ 2.4% 2.3%,
    /* hood-ro=== */ /* ===hood-f */ 91% 12%,
    /* hood-f=== */ /* ===hood-e */ 93.9% 17%,
    /* hood-e=== */ /* ===hood-l */ 12% 17.5%,
    /* hood-l=== */ /* ===hood-r */ 12% 17.5%,
    /* hood-r=== */ /* ===hood-o */ 38% 1.1%,
    /* hood-o=== */ /* ===hood */ 77% 25%, /* hood=== */ /* ===mirror */ 9% 30%,
    /* mirror=== */ /* ===mirror */ 9% 30%,
    /* mirror=== */ /* ===guide-l */ 8.4% 3%,
    /* guide-l=== */ /* ===guide-r */ 8.4% 3%,
    /* guide-r=== */ /* ===plaque */ 33% 6.5%,
    /* plaque=== */ /* ===plaque */ 36% 9%,
    /* plaque=== */ /* ===bumper */ 87% 30%,
    /* bumper=== */ /* ===bumper-l */ 10% 12%,
    /* bumper-l=== */ /* ===bumper-r */ 10% 12%,
    /* bumper-r=== */ /* ===bumper-d */ 78% 35%,
    /* bumper-d=== */ /* ===bumper-l */ 11% 8%,
    /* bumper-l=== */ /* ===bumper-r */ 11% 8%,
    /* bumper-r=== */ /* ===floor */ 68% 8%,
    /* floor=== */ /* ===floor-l */ 5% 7%,
    /* floor-l=== */ /* ===floor-r */ 5% 7%;

  /* floor-r=== */

  background-position: 


    /*=== ceiling */ 50.5% 0,
    /* ceiling=== */ /* ===antenna */ 90% 37%,
    /* antenna=== */ /*=== antenna */ 88% 1.2%,
    /* antenna=== */ /* ===glass-l */ 0 11.7%,
    /* glass-l=== */ /* ===glass-r */ 100% 11.7%,
    /* glass-r=== */ /* ===light */ 5% 63%,
    /* light=== */ /* ===light */ 95% 63%,
    /* light=== */ /* ===hood-ro */ 4.1% 55.7%,
    /* hood-ro=== */ /* ===hood-ro */ 4.1% 65.9%,
    /* hood-ro=== */ /* ===hood-ro */ 95.8% 55.7%,
    /* hood-ro=== */ /* ===hood-ro */ 95.8% 65.8%,
    /* hood-ro=== */ /* ===hood-f */ center 62%,
    /* hood-f=== */ /* ===hood-e */ 49% 63.6%,
    /* hood-e=== */ /* ===hood-l */ 3.4% 46.2%,
    /* hood-l=== */ /* ===hood-r */ 96.5% 46.2%,
    /* hood-r=== */ /* ===hood-o */ center 40.9%,
    /* hood-o=== */ /* ===hood */ center 50.3%,
    /* hood=== */ /* ===mirror */ 5.7% 48.6%,
    /* mirror=== */ /* ===mirror */ 95% 48.6%,
    /* mirror=== */ /* ===guide-l */ 5% 75.2%,
    /* guide-l=== */ /* ===guide-r */ 95% 75.2%,
    /* guide-r=== */ /* ===plaque */ 51% 86%,
    /* plaque=== */ /* ===plaque */ 51.5% 87.3%,
    /* plaque=== */ /* ===bumper */ center 71.9%,
    /* bumper=== */ /* ===bumper-l */ -0.8% 77.8%,
    /* bumper-l=== */ /* ===bumper-r */ 101.7% 77.8%,
    /* bumper-r=== */ /* ===bumper-d */ center 80.2%,
    /* bumper-d=== */ /* ===bumper-l */ 4% 85.9%,
    /* bumper-l=== */ /* ===bumper-r */ 97% 85.9%,
    /* bumper-r=== */ /* ===floor */ center 92.5%,
    /* floor=== */ /* ===floor-l */ 11.7% 92.6%,
    /* floor-l=== */ /* ===floor-r */ 88.3% 92.6%;
}

@keyframes line {
  100% {
    background-position: center 100%;
  }
}

@keyframes car {
  15%,
  23% {
    transform: translate3d(-2.3em, 0, 0);
  }

  36%,
  42% {
    transform: translate3d(-0.8em, 0, 0);
  }

  61%,
  71.5% {
    transform: translate3d(2.8em, 0, 0);
  }

  81%,
  88% {
    transform: translate3d(1.5em, 0, 0);
  }
}

@keyframes move-road {
  5.5% {
    transform: perspective(311px) rotateX(83deg)
      translate3d(var(--n-road), -11.975em, 0);
  }

  27%,
  51% {
    transform: perspective(311px) rotateX(83deg)
      translate3d(var(--p-road), -11.975em, 0);
  }

  73%,
  100% {
    transform: perspective(311px) rotateX(83deg)
      translate3d(var(--n-road), -11.975em, 0);
  }
}

@keyframes light {
  0%,
  37% {
    --light: #fbfbfb;
  }

  50% {
    --light: #f1f1f1;
  }

  62% {
    --light: #fbfbfb;
  }

  65% {
    --light: #f1f1f1;
  }

  95% {
    --light: #fbfbfb;
  }

  100% {
    --light: #f1f1f1;
  }
}

@keyframes shake {
  5%,
  26% {
    transform: rotate(-1.5deg);
  }

  33%,
  41% {
    transform: rotate(-0.5deg);
  }

  48%,
  69% {
    transform: rotate(1.5deg);
  }

  80%,
  95% {
    transform: rotate(0.5deg);
  }
}

```

<!-- endtab -->

<!-- tab car.styl-->

```css
if hexo-config('preloader')
  .carplay
    display: flex;
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 1001;
    opacity: 1;
    overflow: hidden;
    transition: 0.2s;
    &::-webkit-scrollbar 
      display: none; 

  #loading-box
    user-select none
    &.loaded
      .carplay
        display: none

  @keyframes loadingAction
    0% {
        opacity: 1;
    }

    100% {
        opacity: .4;
    }

```

<!-- endtab -->

<!-- tab default.styl -->

```css
.loading-bg
  position fixed
  z-index 1000
  width 50%
  height 100%
  background var(--preloader-bg)
#loading-box
  .loading-left-bg
    @extend .loading-bg
    left 0
  .loading-right-bg
    @extend .loading-bg
    right 0
  &.loaded
    z-index -1000
    .loading-left-bg
      transition all 1.0s
      transform translate(-100%, 0)
    .loading-right-bg
      transition all 1.0s
      transform translate(100%, 0)
#loading-box
  .spinner-box
    position fixed
    z-index 1001
    display flex
    justify-content center
    align-items center
    width 100%
    height 100vh

    .configure-border-1
      position absolute
      padding 3px
      width 115px
      height 115px
      background #ffab91
      animation configure-clockwise 3s ease-in-out 0s infinite alternate

    .configure-border-2
      left -115px
      padding 3px
      width 115px
      height 115px
      background rgb(63, 249, 220)
      transform rotate(45deg)
      animation configure-xclockwise 3s ease-in-out 0s infinite alternate

    .loading-word
      position absolute
      color var(--preloader-color)
      font-size 16px

    .configure-core
      width 100%
      height 100%
      background-color var(--preloader-bg)

  &.loaded
    .spinner-box
      display none

@keyframes configure-clockwise
  0%
    transform rotate(0)

  25%
    transform rotate(90deg)

  50%
    transform rotate(180deg)

  75%
    transform rotate(270deg)

  100%
    transform rotate(360deg)

@keyframes configure-xclockwise
  0%
    transform rotate(45deg)

  25%
    transform rotate(-45deg)

  50%
    transform rotate(-135deg)

  75%
    transform rotate(-225deg)

  100%
    transform rotate(-315deg)

```

<!-- endtab -->

<!-- tab gear.styl -->

```css
#loading-box
  position fixed
  z-index 1000
  width 100vw
  height 100vh
  overflow hidden
  text-align center
  &.loaded
    z-index -1000
    .gear-loader
      display none
  .gear-loader
    height 100%
    position relative
    margin auto
    width 400px
  .gear-loader_overlay
    width 150px
    height 150px
    background transparent
    box-shadow 0px 0px 0px 1000px rgba(255, 255, 255, 0.67), 0px 0px 19px 0px rgba(0, 0, 0, 0.16) inset
    border-radius 100%
    z-index -1
    position absolute
    left 0
    right 0
    top 0
    bottom 0
    margin auto
  .gear-loader_cogs
    z-index -2
    width 100px
    height 100px
    top -120px !important
    position absolute
    left 0
    right 0
    top 0
    bottom 0
    margin auto
  .gear-loader_cogs__top
    position relative
    width 100px
    height 100px
    transform-origin 50px 50px
    -webkit-animation rotate 10s infinite linear
    animation rotate 10s infinite linear
    div
      &:nth-of-type(1)
        transform rotate(30deg)
      &:nth-of-type(2)
        transform rotate(60deg)
      &:nth-of-type(3)
        transform rotate(90deg)
      &.gear-top_part
        width 100px
        border-radius 10px
        position absolute
        height 100px
        background #f98db9
      &.gear-top_hole
        width 50px
        height 50px
        border-radius 100%
        background white
        position absolute
        position absolute
        left 0
        right 0
        top 0
        bottom 0
        margin auto
  .gear-loader_cogs__left
    position relative
    width 80px
    transform rotate(16deg)
    top 28px
    transform-origin 40px 40px
    animation rotate_left 10s 0.1s infinite reverse linear
    left -24px
    height 80px
    div
      &:nth-of-type(1)
        transform rotate(30deg)
      &:nth-of-type(2)
        transform rotate(60deg)
      &:nth-of-type(3)
        transform rotate(90deg)
      &.gear-left_part
        width 80px
        border-radius 6px
        position absolute
        height 80px
        background #97ddff
      &.gear-left_hole
        width 40px
        height 40px
        border-radius 100%
        background white
        position absolute
        position absolute
        left 0
        right 0
        top 0
        bottom 0
        margin auto
  .gear-loader_cogs__bottom
    position relative
    width 60px
    top -65px
    transform-origin 30px 30px
    -webkit-animation rotate_left 10.2s 0.4s infinite linear
    animation rotate_left 10.2s 0.4s infinite linear
    transform rotate(4deg)
    left 79px
    height 60px
    div
      &:nth-of-type(1)
        transform rotate(30deg)
      &:nth-of-type(2)
        transform rotate(60deg)
      &:nth-of-type(3)
        transform rotate(90deg)
      &.gear-bottom_part
        width 60px
        border-radius 5px
        position absolute
        height 60px
        background #ffcd66
      &.gear-bottom_hole
        width 30px
        height 30px
        border-radius 100%
        background white
        position absolute
        position absolute
        left 0
        right 0
        top 0
        bottom 0
        margin auto



/* Animations */
@-webkit-keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes rotate_left {
  from {
    transform: rotate(16deg);
  }
  to {
    transform: rotate(376deg);
  }
}
@keyframes rotate_left {
  from {
    transform: rotate(16deg);
  }
  to {
    transform: rotate(376deg);
  }
}
@-webkit-keyframes rotate_right {
  from {
    transform: rotate(4deg);
  }
  to {
    transform: rotate(364deg);
  }
}
@keyframes rotate_right {
  from {
    transform: rotate(4deg);
  }
  to {
    transform: rotate(364deg);
  }
}

```

<!-- endtab -->

<!-- tab heo.styl -->

```css
if hexo-config('preloader')
  .loading-bg
    display: flex;
    width: 100%;
    height: 100%;
    position: fixed;
    background: var(--anzhiyu-card-bg);
    z-index: 1001;
    opacity: 1;
    overflow: hidden;
    transition: 0.2s;
    animation: showLoading 0.3s 0s backwards;
    &::-webkit-scrollbar 
      display: none

  #loading-box
    user-select none
    .loading-img
      width: 100px;
      height: 100px;
      border-radius: 50%;
      margin: auto;
      border: 4px solid #f0f0f2;
      animation-duration: 0.2s;
      animation-name: loadingAction;
      animation-iteration-count: infinite;
      animation-direction: alternate;
    .loading-image-dot
      width: 30px;
      height: 30px;
      background: #6bdf8f;
      position: absolute;
      border-radius: 50%;
      border: 6px solid #fff;
      top: 50%;
      left: 50%;
      transform: translate(18px, 24px);
    &.loaded
      .loading-bg
        opacity: 0;
        z-index: -1000;

  @keyframes loadingAction
    0% {
        opacity: 1;
    }

    100% {
        opacity: .4;
    }
```

<!-- endtab -->

<!-- tab image.styl -->

```css
.loading-bg
  position fixed
  z-index 1000
  width 50%
  height 100%
  background var(--preloader-bg)
#loading-box
  .loading-left-bg
    @extend .loading-bg
    left 0
  .loading-right-bg
    @extend .loading-bg
    right 0
  &.loaded
    z-index -1000
    .loading-left-bg
      transition all 1.0s
      transform translate(-100%, 0)
    .loading-right-bg
      transition all 1.0s
      transform translate(100%, 0)
#loading-box
  position fixed
  z-index 1000
  display -webkit-box
  display flex
  -webkit-box-align center
  align-items center
  -webkit-box-pack center
  justify-content center
  -webkit-box-orient vertical
  -webkit-box-direction normal
  flex-direction column
  flex-wrap wrap
  width 100vw
  height 100vh
  overflow hidden

  .load-image
    position fixed
    z-index 1001
    display flex

  &.loaded
    .load-image
      display none

```

<!-- endtab -->

<!-- tab ironheart.styl -->

```css
.loading-bg
  position fixed
  z-index 1000
  width 50%
  height 100%
  background var(--preloader-bg)
#loading-box
  .loading-left-bg
    @extend .loading-bg
    left 0
  .loading-right-bg
    @extend .loading-bg
    right 0
  &.loaded
    z-index -1000
    .loading-left-bg
      transition all 1.0s
      transform translate(-100%, 0)
    .loading-right-bg
      transition all 1.0s
      transform translate(100%, 0)
#loading-box
  position fixed
  z-index 1000
  display -webkit-box
  display flex
  -webkit-box-align center
  align-items center
  -webkit-box-pack center
  justify-content center
  -webkit-box-orient vertical
  -webkit-box-direction normal
  flex-direction column
  flex-wrap wrap
  width 100vw
  height 100vh
  overflow hidden

  &.loaded
    .iron-container
      display none

  .iron-circle
    border-radius 50%

  .iron-center
    position absolute
    top 50%
    left 50%
    transform translate(-50%, -50%)

  .iron-container
    z-index 1001
    position relative
    width 300px
    height 300px
    border 1px solid rgb(18, 20, 20)
    background-color #384c50
    box-shadow 0 0 32px 8px rgb(18, 20, 20), 0 0 4px 1px rgb(18, 20, 20) inset
    .iron-box1
      width 238px
      height 238px
      background-color rgb(22, 26, 27)
      box-shadow 0 0 4px 1px #52fefe
    .iron-box2
      width 220px
      height 220px
      background-color #fff
      box-shadow 0 0 5px 1px #52fefe, 0 0 5px 4px #52fefe inset
    .iron-box3
      width 180px
      height 180px
      background-color #073c4b
      box-shadow 0 0 5px 4px #52fefe, 0 0 6px 2px #52fefe inset
    .iron-box4
      width 120px
      height 120px
      border 1px solid #52fefe
      background-color #fff
      box-shadow 0 0 2px 1px #52fefe, 0 0 10px 5px #52fefe inset
    .iron-box5
      width 70px
      height 70px
      border 5px solid #1b4e5f
      box-shadow 0 0 7px 5px #52fefe, 0 0 10px 10px #52fefe inset
    .iron-box6
      position relative
      width 100%
      height 100%
      animation ironrotate 3s linear infinite
      .iron-coil
        position absolute
        width 30px
        height 20px
        top calc(50% - 110px)
        left calc(50% - 15px)
        background-color #073c4b
        box-shadow 0 0 5px #52fefe inset
        transform rotate(calc(var(--i) * 45deg))
        transform-origin center 110px
@keyframes ironrotate
  0%
    transform rotate(0)
  100%
    transform rotate(360deg)
```

<!-- endtab -->

<!-- tab scarecrow.styl -->

```css
.loading-bg
  position fixed
  z-index 1000
  width 50%
  height 100%
  background var(--preloader-bg)
#loading-box
  .loading-left-bg
    @extend .loading-bg
    left 0
  .loading-right-bg
    @extend .loading-bg
    right 0
  &.loaded
    z-index -1000
    .loading-left-bg
      transition all 1.0s
      transform translate(-100%, 0)
    .loading-right-bg
      transition all 1.0s
      transform translate(100%, 0)

#loading-box
  position fixed
  z-index 1000
  display -webkit-box
  display flex
  -webkit-box-align center
  align-items center
  -webkit-box-pack center
  justify-content center
  -webkit-box-orient vertical
  -webkit-box-direction normal
  flex-direction column
  flex-wrap wrap
  width 100vw
  height 100vh
  overflow hidden
  &.loaded
    .scarecrow
      display none
  .scarecrow
    z-index 1001
    position relative
    animation hop 0.2s ease-in alternate infinite

  .scarecrow__hat
    position relative
    border-top-left-radius 5px
    border-top-right-radius 5px
    border-top 45px solid #515559
    border-left 1px solid transparent
    border-right 1px solid transparent
    width 55px
    margin 0 auto -3px
    z-index 1
    &:before
      content ""
      position absolute
      top -87px
      right -23px
      background-color #515559
      width 9px
      height 55px
      border-radius 100%
      transform rotate(50deg)
    &:after
      content ""
      position absolute
      top 12px
      left -15px
      background-color #515559
      width 85px
      height 10px
      border-radius 40% 40% 70% 70%

  .scarecrow__ribbon
    width 55px
    height 12px
    background-color #d996b5
    margin 0 auto

  .scarecrow__head
    position relative
    background-color #f2f2f2
    width 70px
    height 55px
    margin 0 auto
    border-radius 50%
    display flex
    justify-content space-around
    flex-flow row wrap

  .scarecrow__eye
    width 6px
    height 6px
    background-color #000
    border-radius 50%
    margin 20px 5px 0

  .scarecrow__mouth
    width 45px
    height 15px
    background-color #fff
    border-radius 50%

  .scarecrow__pipe
    position absolute
    top 40px
    left 60px
    width 40px
    height 2px
    background-color #8c8070
    &:before
      content ""
      position absolute
      width 9px
      height 17px
      background-color #8c8070
      border-radius 3px
      left 40px
      top -7px

  .scarecrow__body
    position relative
    width 250px
    z-index 1

  .scarecrow__coat
    position absolute
    top 15px
    left 0
    right 0
    margin-left auto
    margin-right auto
    border-top 100px solid #515559
    border-left 5px solid transparent
    border-right 5px solid transparent
    width 75px

  .scarecrow__bow
    position absolute
    top 20px
    left 0
    right 0
    margin-left auto
    margin-right auto
    background-color #3a485d
    width 10px
    height 10px
    z-index 3
    border-radius 2px
    &:before
      content ""
      position absolute
      top -10px
      left -25px
      width 0
      height 10px
      border-top 10px solid transparent
      border-left 25px solid #5a6b8c
      border-bottom 10px solid transparent
      border-radius 8px
    &:after
      content ""
      position absolute
      top -10px
      right -25px
      width 0
      height 10px
      border-top 10px solid transparent
      border-right 25px solid #5a6b8c
      border-bottom 10px solid transparent
      border-radius 8px

  .scarecrow__shirt
    position absolute
    top 8px
    left 0
    right 0
    margin-left auto
    margin-right auto
    width 30px
    height 35px
    z-index 2
    &:before
      content ""
      position absolute
      top 0
      left -5px
      height 100%
      width 70%
      background-color #dbb2c2
      transform skew(1deg, 35deg)
      border-bottom-left-radius 90px
      border-top-left-radius 15px
      border-bottom-right-radius 15px
      border-top-right-radius 10px
    &:after
      content ""
      position absolute
      top 0
      right -5px
      height 100%
      width 70%
      background-color #dbb2c2
      transform skew(-1deg, -35deg)
      border-top-right-radius 15px
      border-bottom-right-radius 90px
      border-bottom-left-radius 15px
      border-top-left-radius 10px

  .scarecrow__waistcoat
    position absolute
    top 15px
    left -1px
    right 0
    margin-left auto
    margin-right auto
    width 35px
    height 50px
    &:before
      content ""
      position absolute
      top 0
      left -4px
      height 100%
      width 65%
      background-color #83a6bc
      transform skew(0deg, 40deg)
      border-bottom-left-radius 90px
      border-top-left-radius 90px
      border-bottom-right-radius 15px
    &:after
      content ""
      position absolute
      top 0
      right -5px
      height 100%
      width 65%
      background-color #83a6bc
      transform skew(0deg, -40deg)
      border-top-right-radius 90px
      border-bottom-right-radius 90px
      border-bottom-left-radius 15px

  .scarecrow__coattails
    position absolute
    top 105px
    left 0
    right 0
    margin-left auto
    margin-right auto
    width 75px
    height 120px
    z-index 1
    &:before
      content ""
      position absolute
      top 0
      left 8px
      height 100%
      width 60%
      background-color #515559
      transform-origin top
      transform skew(-25deg, 30deg) rotate(0deg)
      border-bottom-left-radius 50px
      border-bottom-right-radius 5px
      animation coattails-left 0.2s ease-in alternate infinite
    &:after
      content ""
      position absolute
      top 0
      right 8px
      height 100%
      width 60%
      background-color #515559
      transform-origin top
      transform skew(25deg, -30deg) rotate(0deg)
      border-bottom-right-radius 50px
      border-bottom-left-radius 5px
      animation coattails-right 0.2s ease-in alternate infinite

  .scarecrow__pants
    position absolute
    top 115px
    left 0
    right 0
    margin-left auto
    margin-right auto
    width 50px
    height 150px
    &:before
      content ""
      position absolute
      top 0
      left -8px
      height 100%
      width 60%
      background-color #393c3e
      transform rotate(0deg)
      transform-origin top
      animation pants 0.5s linear alternate infinite
    &:after
      content ""
      position absolute
      top 0
      right -8px
      height 100%
      width 60%
      background-color #393c3e
      transform rotate(0deg)
      transform-origin top
      animation pants 0.3s linear alternate infinite

  .scarecrow__sleeve
    position absolute
    top 15px
    background-color #515559
    width 80px
    height 25px

  .scarecrow__sleeve--l
    left 10px
    &:before
      content ""
      position absolute
      top -3px
      left -22px
      width 0
      height 25px
      border-top 3px solid transparent
      border-left 25px solid #515559
      border-bottom 3px solid transparent
      border-radius 3px

  .scarecrow__sleeve--r
    right 10px
    &:before
      content ""
      position absolute
      top -3px
      right -22px
      width 0
      height 25px
      border-top 3px solid transparent
      border-right 25px solid #515559
      border-bottom 3px solid transparent
      border-radius 3px

  .scarecrow__glove
    position absolute
    top 12px
    width 0px
    height 12px
    &:before
      content ""
      position absolute
      top -7px
      border-radius 100%
      background-color #f2f2f2
      width 35px
      height 15px

  .scarecrow__glove--l
    border-top 3px solid transparent
    border-right 20px solid #f2f2f2
    border-bottom 3px solid transparent
    left -50px
    &:before
      transform-origin right
      left -30px
      transform rotate(0deg)
      animation glove-l 0.2s linear alternate infinite

  .scarecrow__glove--r
    border-top 3px solid transparent
    border-left 20px solid #f2f2f2
    border-bottom 3px solid transparent
    right -50px
    &:before
      transform-origin left
      right -30px
      transform rotate(0deg)
      animation glove-r 0.2s linear alternate infinite

  .scarecrow__arms
    position absolute
    left 50%
    transform translate(-50%, -50%)
    background-color #8c8070
    width 350px
    height 8px
    border-radius 5px
    margin 20px auto

  .scarecrow__leg
    position relative
    background-color #8c8070
    width 8px
    height 380px
    border-bottom-left-radius 5px
    border-bottom-right-radius 5px
    margin 0 auto

@keyframes hop
  0%
    transform translateY(-10px)
  100%
    transform translateY(10px)

@keyframes coattails-left
  0%
    transform skew(-25deg, 30deg) rotate(-3deg)
  100%
    transform skew(-25deg, 30deg) rotate(3deg)

@keyframes coattails-right
  0%
    transform skew(25deg, -30deg) rotate(3deg)
  100%
    transform skew(25deg, -30deg) rotate(-3deg)

@keyframes pants
  0%
    transform rotate(3deg)
  100%
    transform rotate(-3deg)

@keyframes glove-l
  0%
    transform rotate(-50deg)
  100%
    transform rotate(-30deg)

@keyframes glove-r
  0%
    transform rotate(50deg)
  100%
    transform rotate(30deg)

```

<!-- endtab -->

<!-- tab triangles.styl -->

```css
#loading-box
  position fixed
  z-index 1000
  width 100vw
  height 100vh
  overflow hidden
  &.loaded
    z-index -1000
    .triangles-wrap
      display none

.triangles-wrap
  position absolute
  top 50%
  left 50%
  transform translate(-50%,-66.6666666666666666%)
  -ms-transform translate(-50%,-66.6666666666666666%)
  -webkit-transform translate(-50%,-66.6666666666666666%)
  -webkit-animation animascale 2s linear alternate infinite
  animation animascale 2s linear alternate both infinite



.triangles-zero, .triangles-ein, .triangles-dvai, .triangles-trei, .triangles-feir, .triangles-fei, .triangles-sei, .triangles-seiz, .triangles-eiz
  width 0px
  height 0px
  position absolute
  top 50%
  left 50%
  transform translate(-50%,-66.6666666666666666%)
  -ms-transform translate(-50%,-66.6666666666666666%)
  -webkit-transform translate(-50%,-66.6666666666666666%)

.triangles-zero
  border-style solid
  border-width 0 5px 8.7px 5px
  border-color transparent transparent #1274b6 transparent
  -webkit-animation anima 2s linear reverse both infinite 4s, animacolorzero 2s linear alternate both infinite
  animation anima 2s linear reverse both infinite 4s, animacolorzero 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-ein
  border-style solid
  border-width 0 10px 17.3px 10px
  border-color transparent transparent #167bbf transparent
  -webkit-animation anima 2s linear both infinite 4.2s, animacolorein 2s linear alternate both infinite
  animation anima 2s linear both infinite 4.2s, animacolorein 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-dvai
  border-style solid
  border-width 0 20px 34.6px 20px
  border-color transparent transparent #1b82c8 transparent
  -webkit-animation anima 2s linear reverse both infinite 4.4s, animacolordvai 2s linear alternate both infinite
  animation anima 2s linear reverse both infinite 4.4s, animacolordvai 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-trei
  border-style solid
  border-width 0 40px 69.3px 40px
  border-color transparent transparent #228bd2 transparent
  -webkit-animation anima 2s linear  both infinite 4.6s, animacolortrei 2s linear alternate both infinite
  animation anima 2s linear  both infinite 4.6s, animacolortrei 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-feir
  border-style solid
  border-width 0 80px 138.6px 80px
  border-color transparent transparent #2992d9 transparent
  -webkit-animation anima 2s linear reverse  both infinite 4.8s, animacolorfeir 2s linear alternate both infinite
  animation anima 2s linear reverse  both infinite 4.8s, animacolorfeir 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-fei
  border-style solid
  border-width 0 160px 277.1px 160px
  border-color transparent transparent #3498db transparent
  -webkit-animation anima 2s linear  both infinite 5s, animacolorfei 2s linear alternate both infinite
  animation anima 2s linear  both infinite 5s, animacolorfei 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-sei
  border-style solid
  border-width 0 320px 554.3px 320px
  border-color transparent transparent #3f9edd transparent
  -webkit-animation anima 2s linear reverse  both infinite 5.2s, animacolorsei 2s linear alternate both infinite
  animation anima 2s linear reverse  both infinite 5.2s, animacolorsei 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-seiz
  border-style solid
  border-width 0 640px 1108.5px 640px
  border-color transparent transparent #48a2de transparent
  -webkit-animation anima 2s linear  both infinite 5.4s, animacolorseiz 2s linear alternate both infinite
  animation anima 2s linear  both infinite 5.4s, animacolorseiz 2s linear alternate both infinite
  -webkit-transform-origin top left

.triangles-eiz
  border-style solid
  border-width 0 1280px 2217.0px 1280px
  border-color transparent transparent #59aae0 transparent
  -webkit-animation anima 2s linear reverse  both infinite 5.6s, animacoloreiz 2s linear alternate both infinite
  animation anima 2s linear reverse  both infinite 5.6s, animacoloreiz 2s linear alternate both infinite
  -webkit-transform-origin top left


@-webkit-keyframes anima
  from
    -webkit-transform: rotate(0deg) translate(-50%,-66.6666666666666666%)
  to
    -webkit-transform: rotate(360deg) translate(-50%,-66.6666666666666666%)


@keyframes anima
    from
      transform rotate(0deg) translate(-50%,-66.6666666666666666%)
    to
      transform rotate(360deg) translate(-50%,-66.6666666666666666%)

@-webkit-keyframes animacolorzero
{
0%{border-color: transparent transparent #1274b6 transparent;}
12.5%{border-color: transparent transparent #167bbf transparent;}
25%{border-color: transparent transparent #1b82c8 transparent;}
37.5%{border-color: transparent transparent #228bd2 transparent;}
50%{border-color: transparent transparent #2992d9 transparent;}
62.5%{border-color: transparent transparent #3498db transparent;}
75%{border-color: transparent transparent #3f9edd transparent;}
87.5%{border-color: transparent transparent #48a2de transparent;}
100%{border-color: transparent transparent #59aae0 transparent;}
}

@keyframes animacolorzero
{
0%{border-color: transparent transparent #1274b6 transparent;}
12.5%{border-color: transparent transparent #167bbf transparent;}
25%{border-color: transparent transparent #1b82c8 transparent;}
37.5%{border-color: transparent transparent #228bd2 transparent;}
50%{border-color: transparent transparent #2992d9 transparent;}
62.5%{border-color: transparent transparent #3498db transparent;}
75%{border-color: transparent transparent #3f9edd transparent;}
87.5%{border-color: transparent transparent #48a2de transparent;}
100%{border-color: transparent transparent #59aae0 transparent;}
}

@-webkit-keyframes animacolorein
{
0%{border-color: transparent transparent #167bbf transparent;}
12.5%{border-color: transparent transparent #1b82c8 transparent;}
25%{border-color: transparent transparent #228bd2 transparent;}
37.5%{border-color: transparent transparent #2992d9 transparent;}
50%{border-color: transparent transparent #3498db transparent;}
62.5%{border-color: transparent transparent #3f9edd transparent;}
75%{border-color: transparent transparent #48a2de transparent;}
87.5%{border-color: transparent transparent #59aae0 transparent;}
100%{border-color: transparent transparent #1274b6 transparent;}
}

@keyframes animacolorein
{
0%{border-color: transparent transparent #167bbf transparent;}
12.5%{border-color: transparent transparent #1b82c8 transparent;}
25%{border-color: transparent transparent #228bd2 transparent;}
37.5%{border-color: transparent transparent #2992d9 transparent;}
50%{border-color: transparent transparent #3498db transparent;}
62.5%{border-color: transparent transparent #3f9edd transparent;}
75%{border-color: transparent transparent #48a2de transparent;}
87.5%{border-color: transparent transparent #59aae0 transparent;}
100%{border-color: transparent transparent #1274b6 transparent;}
}

@-webkit-keyframes animacolordvai
{
0%{border-color: transparent transparent #1b82c8 transparent;}
12.5%{border-color: transparent transparent #228bd2 transparent;}
25%{border-color: transparent transparent #2992d9 transparent;}
37.5%{border-color: transparent transparent #3498db transparent;}
50%{border-color: transparent transparent #3f9edd transparent;}
62.5%{border-color: transparent transparent #48a2de transparent;}
75%{border-color: transparent transparent #59aae0 transparent;}
87.5%{border-color: transparent transparent #1274b6 transparent;}
100%{border-color: transparent transparent #167bbf transparent;}
}

@keyframes animacolordvai
{
0%{border-color: transparent transparent #1b82c8 transparent;}
12.5%{border-color: transparent transparent #228bd2 transparent;}
25%{border-color: transparent transparent #2992d9 transparent;}
37.5%{border-color: transparent transparent #3498db transparent;}
50%{border-color: transparent transparent #3f9edd transparent;}
62.5%{border-color: transparent transparent #48a2de transparent;}
75%{border-color: transparent transparent #59aae0 transparent;}
87.5%{border-color: transparent transparent #1274b6 transparent;}
100%{border-color: transparent transparent #167bbf transparent;}
}

@-webkit-keyframes animacolortrei
{
0%{border-color: transparent transparent #228bd2 transparent;}
12.5%{border-color: transparent transparent #2992d9 transparent;}
25%{border-color: transparent transparent #3498db transparent;}
37.5%{border-color: transparent transparent #3f9edd transparent;}
50%{border-color: transparent transparent #48a2de transparent;}
62.5%{border-color: transparent transparent #59aae0 transparent;}
75%{border-color: transparent transparent #1274b6 transparent;}
87.5%{border-color: transparent transparent #167bbf transparent;}
100%{border-color: transparent transparent #1b82c8 transparent;}
}

@keyframes animacolortrei
{
0%{border-color: transparent transparent #228bd2 transparent;}
12.5%{border-color: transparent transparent #2992d9 transparent;}
25%{border-color: transparent transparent #3498db transparent;}
37.5%{border-color: transparent transparent #3f9edd transparent;}
50%{border-color: transparent transparent #48a2de transparent;}
62.5%{border-color: transparent transparent #59aae0 transparent;}
75%{border-color: transparent transparent #1274b6 transparent;}
87.5%{border-color: transparent transparent #167bbf transparent;}
100%{border-color: transparent transparent #1b82c8 transparent;}
}

@-webkit-keyframes animacolorfeir
{
0%{border-color: transparent transparent #2992d9 transparent;}
12.5%{border-color: transparent transparent #3498db transparent;}
25%{border-color: transparent transparent #3f9edd transparent;}
37.5%{border-color: transparent transparent #48a2de transparent;}
50%{border-color: transparent transparent #59aae0 transparent;}
62.5%{border-color: transparent transparent #1274b6 transparent;}
75%{border-color: transparent transparent #167bbf transparent;}
87.5%{border-color: transparent transparent #1b82c8 transparent;}
100%{border-color: transparent transparent #228bd2 transparent;}
}

@keyframes animacolorfeir
{
0%{border-color: transparent transparent #2992d9 transparent;}
12.5%{border-color: transparent transparent #3498db transparent;}
25%{border-color: transparent transparent #3f9edd transparent;}
37.5%{border-color: transparent transparent #48a2de transparent;}
50%{border-color: transparent transparent #59aae0 transparent;}
62.5%{border-color: transparent transparent #1274b6 transparent;}
75%{border-color: transparent transparent #167bbf transparent;}
87.5%{border-color: transparent transparent #1b82c8 transparent;}
100%{border-color: transparent transparent #228bd2 transparent;}
}

@-webkit-keyframes animacolorfei
{
0%{border-color: transparent transparent #3498db transparent;}
12.5%{border-color: transparent transparent #3f9edd transparent;}
25%{border-color: transparent transparent #48a2de transparent;}
37.5%{border-color: transparent transparent #59aae0 transparent;}
50%{border-color: transparent transparent #1274b6 transparent;}
62.5%{border-color: transparent transparent #167bbf transparent;}
75%{border-color: transparent transparent #1b82c8 transparent;}
87.5%{border-color: transparent transparent #228bd2 transparent;}
100%{border-color: transparent transparent #2992d9 transparent;}
}

@keyframes animacolorfei
{
0%{border-color: transparent transparent #3498db transparent;}
12.5%{border-color: transparent transparent #3f9edd transparent;}
25%{border-color: transparent transparent #48a2de transparent;}
37.5%{border-color: transparent transparent #59aae0 transparent;}
50%{border-color: transparent transparent #1274b6 transparent;}
62.5%{border-color: transparent transparent #167bbf transparent;}
75%{border-color: transparent transparent #1b82c8 transparent;}
87.5%{border-color: transparent transparent #228bd2 transparent;}
100%{border-color: transparent transparent #2992d9 transparent;}
}

@-webkit-keyframes animacolorsei
{
0%{border-color: transparent transparent #3f9edd transparent;}
12.5%{border-color: transparent transparent #48a2de transparent;}
25%{border-color: transparent transparent #59aae0 transparent;}
37.5%{border-color: transparent transparent #1274b6 transparent;}
50%{border-color: transparent transparent #167bbf transparent;}
62.5%{border-color: transparent transparent #1b82c8 transparent;}
75%{border-color: transparent transparent #228bd2 transparent;}
87.5%{border-color: transparent transparent #2992d9 transparent;}
100%{border-color: transparent transparent #3498db transparent;}
}

@keyframes animacolorsei
{
0%{border-color: transparent transparent #3f9edd transparent;}
12.5%{border-color: transparent transparent #48a2de transparent;}
25%{border-color: transparent transparent #59aae0 transparent;}
37.5%{border-color: transparent transparent #1274b6 transparent;}
50%{border-color: transparent transparent #167bbf transparent;}
62.5%{border-color: transparent transparent #1b82c8 transparent;}
75%{border-color: transparent transparent #228bd2 transparent;}
87.5%{border-color: transparent transparent #2992d9 transparent;}
100%{border-color: transparent transparent #3498db transparent;}
}

@-webkit-keyframes animacolorseiz
{
0%{border-color: transparent transparent #48a2de transparent;}
12.5%{border-color: transparent transparent #59aae0 transparent;}
25%{border-color: transparent transparent #1274b6 transparent;}
37.5%{border-color: transparent transparent #167bbf transparent;}
50%{border-color: transparent transparent #1b82c8 transparent;}
62.5%{border-color: transparent transparent #228bd2 transparent;}
75%{border-color: transparent transparent #2992d9 transparent;}
87.5%{border-color: transparent transparent #3498db transparent;}
100%{border-color: transparent transparent #3f9edd transparent;}
}

@keyframes animacolorseiz
{
0%{border-color: transparent transparent #48a2de transparent;}
12.5%{border-color: transparent transparent #59aae0 transparent;}
25%{border-color: transparent transparent #1274b6 transparent;}
37.5%{border-color: transparent transparent #167bbf transparent;}
50%{border-color: transparent transparent #1b82c8 transparent;}
62.5%{border-color: transparent transparent #228bd2 transparent;}
75%{border-color: transparent transparent #2992d9 transparent;}
87.5%{border-color: transparent transparent #3498db transparent;}
100%{border-color: transparent transparent #3f9edd transparent;}
}

@-webkit-keyframes animacoloreiz
{
0%{border-color: transparent transparent #59aae0 transparent;}
12.5%{border-color: transparent transparent #1274b6 transparent;}
25%{border-color: transparent transparent #167bbf transparent;}
37.5%{border-color: transparent transparent #1b82c8 transparent;}
50%{border-color: transparent transparent #228bd2 transparent;}
62.5%{border-color: transparent transparent #2992d9 transparent;}
75%{border-color: transparent transparent #3498db transparent;}
87.5%{border-color: transparent transparent #3f9edd transparent;}
100%{border-color: transparent transparent #48a2de transparent;}
}

@keyframes animacoloreiz
{
0%{border-color: transparent transparent #59aae0 transparent;}
12.5%{border-color: transparent transparent #1274b6 transparent;}
25%{border-color: transparent transparent #167bbf transparent;}
37.5%{border-color: transparent transparent #1b82c8 transparent;}
50%{border-color: transparent transparent #228bd2 transparent;}
62.5%{border-color: transparent transparent #2992d9 transparent;}
75%{border-color: transparent transparent #3498db transparent;}
87.5%{border-color: transparent transparent #3f9edd transparent;}
100%{border-color: transparent transparent #48a2de transparent;}
}

@-webkit-keyframes animascale
{
0%{-webkit-transform: scale(1);}
100%{-webkit-transform: scale(1.2);}
}

@keyframes animascale
{
0%{-webkit-transform: scale(1);}
100%{-webkit-transform: scale(1.2);}
}

```

<!-- endtab -->

<!-- tab wizard.styl -->

```css
.loading-bg
  position fixed
  z-index 1000
  width 50%
  height 100%
  background var(--preloader-bg)
#loading-box
  .loading-left-bg
    @extend .loading-bg
    left 0
  .loading-right-bg
    @extend .loading-bg
    right 0
  &.loaded
    z-index -1000
    .loading-left-bg
      transition all 1.0s
      transform translate(-100%, 0)
    .loading-right-bg
      transition all 1.0s
      transform translate(100%, 0)
#loading-box
  position fixed
  z-index 1000
  display -webkit-box
  display flex
  -webkit-box-align center
  align-items center
  -webkit-box-pack center
  justify-content center
  -webkit-box-orient vertical
  -webkit-box-direction normal
  flex-direction column
  flex-wrap wrap
  width 100vw
  height 100vh
  overflow hidden

  &.loaded
    .wizard-scene
      display none

.wizard-scene
  position fixed
  z-index 1001
  display -webkit-box
  display flex

.wizard
  position relative
  width 190px
  height 240px

.wizard-body
  position absolute
  bottom 0
  left 68px
  height 100px
  width 60px
  background #3f64ce
  &::after
    content ""
    position absolute
    bottom 0
    left 20px
    height 100px
    width 60px
    background #3f64ce
    -webkit-transform skewX(14deg)
    transform skewX(14deg)

.wizard-right-arm
  position absolute
  bottom 74px
  left 110px
  height 44px
  width 90px
  background #3f64ce
  border-radius 22px
  -webkit-transform-origin 16px 22px
  transform-origin 16px 22px
  -webkit-transform rotate(70deg)
  transform rotate(70deg)
  -webkit-animation right_arm 10s ease-in-out infinite
  animation right_arm 10s ease-in-out infinite
  .right-hand
    position absolute
    right 8px
    bottom 8px
    width 30px
    height 30px
    border-radius 50%
    background #f1c5b4
    -webkit-transform-origin center center
    transform-origin center center
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)
    -webkit-animation right_hand 10s ease-in-out infinite
    animation right_hand 10s ease-in-out infinite
  .wizard-right-hand
    &::after
      content ""
      position absolute
      right 0px
      top -8px
      width 15px
      height 30px
      border-radius 10px
      background #f1c5b4
      -webkit-transform translateY(16px)
      transform translateY(16px)
      -webkit-animation right_finger 10s ease-in-out infinite
      animation right_finger 10s ease-in-out infinite

.wizard-left-arm
  position absolute
  bottom 74px
  left 26px
  height 44px
  width 70px
  background #3f64ce
  border-bottom-left-radius 8px
  -webkit-transform-origin 60px 26px
  transform-origin 60px 26px
  -webkit-transform rotate(-70deg)
  transform rotate(-70deg)
  -webkit-animation left_arm 10s ease-in-out infinite
  animation left_arm 10s ease-in-out infinite
  .wizard-left-hand
    position absolute
    left -18px
    top 0
    width 18px
    height 30px
    border-top-left-radius 35px
    border-bottom-left-radius 35px
    background #f1c5b4
    &::after
      content ""
      position absolute
      right 0
      top 0
      width 30px
      height 15px
      border-radius 20px
      background #f1c5b4
      -webkit-transform-origin right bottom
      transform-origin right bottom
      -webkit-transform scaleX(0)
      transform scaleX(0)
      -webkit-animation left_finger 10s ease-in-out infinite
      animation left_finger 10s ease-in-out infinite

.wizard-head
  position absolute
  top 0
  left 14px
  width 160px
  height 210px
  -webkit-transform-origin center center
  transform-origin center center
  -webkit-transform rotate(-3deg)
  transform rotate(-3deg)
  -webkit-animation head 10s ease-in-out infinite
  animation head 10s ease-in-out infinite
  .wizard-beard
    position absolute
    bottom 0
    left 38px
    height 106px
    width 80px
    border-bottom-right-radius 55%
    background #ffffff
    &::after
      content ""
      position absolute
      top 16px
      left -10px
      width 40px
      height 20px
      border-radius 20px
      background #ffffff
  .wizard-face
    position absolute
    bottom 76px
    left 38px
    height 30px
    width 60px
    background #f1c5b4
    &::before
      content ""
      position absolute
      top 0px
      left 40px
      width 20px
      height 40px
      border-bottom-right-radius 20px
      border-bottom-left-radius 20px
      background #f1c5b4
    &::after
      content ""
      position absolute
      top 16px
      left -10px
      width 50px
      height 20px
      border-radius 20px
      border-bottom-right-radius 0px
      background #ffffff
    .wizard-adds
      position absolute
      top 0px
      left -10px
      width 40px
      height 20px
      border-radius 20px
      background #f1c5b4
      &::after
        content ""
        position absolute
        top 5px
        left 80px
        width 15px
        height 20px
        border-bottom-right-radius 20px
        border-top-right-radius 20px
        background #f1c5b4
  .wizard-hat
    position absolute
    bottom 106px
    left 0
    width 160px
    height 20px
    border-radius 20px
    background #3f64ce
    &::before
      content ""
      position absolute
      top -70px
      left 50%
      -webkit-transform translatex(-50%)
      transform translatex(-50%)
      width 0
      height 0
      border-style solid
      border-width 0 34px 70px 50px
      border-color transparent transparent #3f64ce transparent
    &::after
      content ""
      position absolute
      top 0
      left 0
      width 160px
      height 20px
      background #3f64ce
      border-radius 20px
    .wizard-hat-of-the-hat
      position absolute
      bottom 78px
      left 79px
      width 0
      height 0
      border-style solid
      border-width 0 25px 25px 19px
      border-color transparent transparent #3f64ce transparent
      &::after
        content ""
        position absolute
        top 6px
        left -4px
        width 35px
        height 10px
        border-radius 10px
        border-bottom-left-radius 0px
        background #3f64ce
        -webkit-transform rotate(40deg)
        transform rotate(40deg)
    .wizard-four-point-star
      position absolute
      width 12px
      height 12px
      &::after
        -webkit-transform rotate(156.66deg) skew(45deg)
        transform rotate(156.66deg) skew(45deg)
      &.--first
        bottom 28px
        left 46px
      &.--second
        bottom 40px
        left 80px
      &.--third
        bottom 15px
        left 108px

.wizard-head .wizard-hat .wizard-four-point-star::after, .wizard-head .wizard-hat .wizard-four-point-star::before
  content ""
  position absolute
  background #ffffff
  display block
  left 0
  width 141.4213%
  top 0
  bottom 0
  border-radius 10%
  -webkit-transform rotate(66.66deg) skewX(45deg)
  transform rotate(66.66deg) skewX(45deg)

.wizard-objects
  position relative
  width 200px
  height 240px

.wizard-square
  position absolute
  bottom -60px
  left -5px
  width 120px
  height 120px
  border-radius 50%
  -webkit-transform rotate(-360deg)
  transform rotate(-360deg)
  -webkit-animation path_square 10s ease-in-out infinite
  animation path_square 10s ease-in-out infinite
  &::after
    content ""
    position absolute
    top 10px
    left 0
    width 50px
    height 50px
    background #9ab3f5

.wizard-circle
  position absolute
  bottom 10px
  left 0
  width 100px
  height 100px
  border-radius 50%
  -webkit-transform rotate(-360deg)
  transform rotate(-360deg)
  -webkit-animation path_circle 10s ease-in-out infinite
  animation path_circle 10s ease-in-out infinite
  &::after
    content ""
    position absolute
    bottom -10px
    left 25px
    width 50px
    height 50px
    border-radius 50%
    background #c56183

.wizard-triangle
  position absolute
  bottom -62px
  left -10px
  width 110px
  height 110px
  border-radius 50%
  -webkit-transform rotate(-360deg)
  transform rotate(-360deg)
  -webkit-animation path_triangle 10s ease-in-out infinite
  animation path_triangle 10s ease-in-out infinite
  &::after
    content ""
    position absolute
    top 0
    right -10px
    width 0
    height 0
    border-style solid
    border-width 0 28px 48px 28px
    border-color transparent transparent #89beb3 transparent


/** 10s animation - 10% = 1s */
@-webkit-keyframes right_arm
  0%
    -webkit-transform rotate(70deg)
    transform rotate(70deg)
  10%
    -webkit-transform rotate(8deg)
    transform rotate(8deg)
  15%
    -webkit-transform rotate(20deg)
    transform rotate(20deg)
  20%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  25%
    -webkit-transform rotate(26deg)
    transform rotate(26deg)
  30%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  35%
    -webkit-transform rotate(28deg)
    transform rotate(28deg)
  40%
    -webkit-transform rotate(9deg)
    transform rotate(9deg)
  45%
    -webkit-transform rotate(28deg)
    transform rotate(28deg)
  50%
    -webkit-transform rotate(8deg)
    transform rotate(8deg)
  58%
    -webkit-transform rotate(74deg)
    transform rotate(74deg)
  62%
    -webkit-transform rotate(70deg)
    transform rotate(70deg)

@keyframes right_arm
  0%
    -webkit-transform rotate(70deg)
    transform rotate(70deg)
  10%
    -webkit-transform rotate(8deg)
    transform rotate(8deg)
  15%
    -webkit-transform rotate(20deg)
    transform rotate(20deg)
  20%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  25%
    -webkit-transform rotate(26deg)
    transform rotate(26deg)
  30%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  35%
    -webkit-transform rotate(28deg)
    transform rotate(28deg)
  40%
    -webkit-transform rotate(9deg)
    transform rotate(9deg)
  45%
    -webkit-transform rotate(28deg)
    transform rotate(28deg)
  50%
    -webkit-transform rotate(8deg)
    transform rotate(8deg)
  58%
    -webkit-transform rotate(74deg)
    transform rotate(74deg)
  62%
    -webkit-transform rotate(70deg)
    transform rotate(70deg)

@-webkit-keyframes left_arm
  0%
    -webkit-transform rotate(-70deg)
    transform rotate(-70deg)
  10%
    -webkit-transform rotate(6deg)
    transform rotate(6deg)
  15%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  20%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  25%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  30%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  35%
    -webkit-transform rotate(-17deg)
    transform rotate(-17deg)
  40%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  45%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  50%
    -webkit-transform rotate(6deg)
    transform rotate(6deg)
  58%
    -webkit-transform rotate(-74deg)
    transform rotate(-74deg)
  62%
    -webkit-transform rotate(-70deg)
    transform rotate(-70deg)

@keyframes left_arm
  0%
    -webkit-transform rotate(-70deg)
    transform rotate(-70deg)
  10%
    -webkit-transform rotate(6deg)
    transform rotate(6deg)
  15%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  20%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  25%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  30%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  35%
    -webkit-transform rotate(-17deg)
    transform rotate(-17deg)
  40%
    -webkit-transform rotate(5deg)
    transform rotate(5deg)
  45%
    -webkit-transform rotate(-18deg)
    transform rotate(-18deg)
  50%
    -webkit-transform rotate(6deg)
    transform rotate(6deg)
  58%
    -webkit-transform rotate(-74deg)
    transform rotate(-74deg)
  62%
    -webkit-transform rotate(-70deg)
    transform rotate(-70deg)

@-webkit-keyframes right_hand
  0%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)
  10%
    -webkit-transform rotate(-20deg)
    transform rotate(-20deg)
  15%
    -webkit-transform rotate(-5deg)
    transform rotate(-5deg)
  20%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  25%
    -webkit-transform rotate(0deg)
    transform rotate(0deg)
  30%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  35%
    -webkit-transform rotate(0deg)
    transform rotate(0deg)
  40%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)
  45%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  50%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  60%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)


@keyframes right_hand
  0%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)
  10%
    -webkit-transform rotate(-20deg)
    transform rotate(-20deg)
  15%
    -webkit-transform rotate(-5deg)
    transform rotate(-5deg)
  20%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  25%
    -webkit-transform rotate(0deg)
    transform rotate(0deg)
  30%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  35%
    -webkit-transform rotate(0deg)
    transform rotate(0deg)
  40%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)
  45%
    -webkit-transform rotate(-60deg)
    transform rotate(-60deg)
  50%
    -webkit-transform rotate(10deg)
    transform rotate(10deg)
  60%
    -webkit-transform rotate(-40deg)
    transform rotate(-40deg)

@-webkit-keyframes right_finger
  0%
    -webkit-transform translateY(16px)
    transform translateY(16px)
  10%
    -webkit-transform none
    transform none
  50%
    -webkit-transform none
    transform none
  60%
    -webkit-transform translateY(16px)
    transform translateY(16px)

@keyframes right_finger
  0%
    -webkit-transform translateY(16px)
    transform translateY(16px)
  10%
    -webkit-transform none
    transform none
  50%
    -webkit-transform none
    transform none
  60%
    -webkit-transform translateY(16px)
    transform translateY(16px)

@-webkit-keyframes left_finger
  0%
    -webkit-transform scaleX(0)
    transform scaleX(0)
  10%
    -webkit-transform scaleX(1) rotate(6deg)
    transform scaleX(1) rotate(6deg)
  15%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  20%
    -webkit-transform scaleX(1) rotate(8deg)
    transform scaleX(1) rotate(8deg)
  25%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  30%
    -webkit-transform scaleX(1) rotate(7deg)
    transform scaleX(1) rotate(7deg)
  35%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  40%
    -webkit-transform scaleX(1) rotate(5deg)
    transform scaleX(1) rotate(5deg)
  45%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  50%
    -webkit-transform scaleX(1) rotate(6deg)
    transform scaleX(1) rotate(6deg)
  58%
    -webkit-transform scaleX(0)
    transform scaleX(0)

@keyframes left_finger
  0%
    -webkit-transform scaleX(0)
    transform scaleX(0)
  10%
    -webkit-transform scaleX(1) rotate(6deg)
    transform scaleX(1) rotate(6deg)
  15%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  20%
    -webkit-transform scaleX(1) rotate(8deg)
    transform scaleX(1) rotate(8deg)
  25%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  30%
    -webkit-transform scaleX(1) rotate(7deg)
    transform scaleX(1) rotate(7deg)
  35%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  40%
    -webkit-transform scaleX(1) rotate(5deg)
    transform scaleX(1) rotate(5deg)
  45%
    -webkit-transform scaleX(1) rotate(0deg)
    transform scaleX(1) rotate(0deg)
  50%
    -webkit-transform scaleX(1) rotate(6deg)
    transform scaleX(1) rotate(6deg)
  58%
    -webkit-transform scaleX(0)
    transform scaleX(0)

@-webkit-keyframes head
  0%
    -webkit-transform rotate(-3deg)
    transform rotate(-3deg)
  10%
    -webkit-transform translatex(10px) rotate(7deg)
    transform translatex(10px) rotate(7deg)
  50%
    -webkit-transform translatex(0px) rotate(0deg)
    transform translatex(0px) rotate(0deg)
  56%
    -webkit-transform rotate(-3deg)
    transform rotate(-3deg)

@keyframes head
  0%
    -webkit-transform rotate(-3deg)
    transform rotate(-3deg)
  10%
    -webkit-transform translatex(10px) rotate(7deg)
    transform translatex(10px) rotate(7deg)
  50%
    -webkit-transform translatex(0px) rotate(0deg)
    transform translatex(0px) rotate(0deg)
  56%
    -webkit-transform rotate(-3deg)
    transform rotate(-3deg)
/** 10s animation - 10% = 1s */
@-webkit-keyframes path_circle
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-100px) rotate(-5deg)
    transform translateY(-100px) rotate(-5deg)
  55%
    -webkit-transform translateY(-100px) rotate(-360deg)
    transform translateY(-100px) rotate(-360deg)
  58%
    -webkit-transform translateY(-100px) rotate(-360deg)
    transform translateY(-100px) rotate(-360deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

@keyframes path_circle
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-100px) rotate(-5deg)
    transform translateY(-100px) rotate(-5deg)
  55%
    -webkit-transform translateY(-100px) rotate(-360deg)
    transform translateY(-100px) rotate(-360deg)
  58%
    -webkit-transform translateY(-100px) rotate(-360deg)
    transform translateY(-100px) rotate(-360deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

@-webkit-keyframes path_square
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(10deg)
    transform translateY(-155px) translatex(-15px) rotate(10deg)
  55%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(-350deg)
    transform translateY(-155px) translatex(-15px) rotate(-350deg)
  57%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(-350deg)
    transform translateY(-155px) translatex(-15px) rotate(-350deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

@keyframes path_square
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(10deg)
    transform translateY(-155px) translatex(-15px) rotate(10deg)
  55%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(-350deg)
    transform translateY(-155px) translatex(-15px) rotate(-350deg)
  57%
    -webkit-transform translateY(-155px) translatex(-15px) rotate(-350deg)
    transform translateY(-155px) translatex(-15px) rotate(-350deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

@-webkit-keyframes path_triangle
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-10deg)
    transform translateY(-172px) translatex(10px) rotate(-10deg)
  55%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-365deg)
    transform translateY(-172px) translatex(10px) rotate(-365deg)
  58%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-365deg)
    transform translateY(-172px) translatex(10px) rotate(-365deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

@keyframes path_triangle
  0%
    -webkit-transform translateY(0)
    transform translateY(0)
  10%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-10deg)
    transform translateY(-172px) translatex(10px) rotate(-10deg)
  55%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-365deg)
    transform translateY(-172px) translatex(10px) rotate(-365deg)
  58%
    -webkit-transform translateY(-172px) translatex(10px) rotate(-365deg)
    transform translateY(-172px) translatex(10px) rotate(-365deg)
  63%
    -webkit-transform rotate(-360deg)
    transform rotate(-360deg)

```

<!-- endtab -->

{% endtabs %}

## 修改 loading.styl

文件路径为: `themes/anzhiyu/source/css/_global/loading.styl`, 修改为根据配置加载对应的样式文件:


```css
if hexo-config('preloader.enable')
  if hexo-config('preloader.source') == 'car'
    @import '../_layout/_load_style/car.css'
    @import '../_layout/_load_style/car'
  else if hexo-config('preloader.source') == 'heo'
    @import '../_layout/_load_style/heo'
  else if hexo-config('preloader.source') == 'gear'
    @import '../_layout/_load_style/gear'
  else if hexo-config('preloader.source') == 'ironheart'
    @import '../_layout/_load_style/ironheart'
  else if hexo-config('preloader.source') == 'scarecrow'
    @import '../_layout/_load_style/scarecrow'
  else if hexo-config('preloader.source') == 'triangles'
    @import '../_layout/_load_style/triangles'
  else if hexo-config('preloader.source') == 'wizard'
    @import '../_layout/_load_style/wizard'
  else if hexo-config('preloader.source') == 'image'
    @import '../_layout/_load_style/image'
  else if hexo-config('preloader.source') == 'default'
    @import '../_layout/_load_style/default'
  else
    @import '../_layout/_load_style/heo'
```

## 修改主题配置

```yaml
# Loading Animation (加载动画)
preloader:
  enable: true
  # load_style：控制加载动画的样式
  # car 小汽车
  # heo heo张洪同款
  # default 是主题原版的盒子加载动画
  # gear 是旋转齿轮加载动画
  # ironheart 是钢铁侠核心加载动画
  # scarecrow 是稻草人跳动加载动画
  # triangles 是旋转三角加载动画
  # wizard 是巫师施法加载动画
  # image 为自定义添加静态图片或gif作为加载动画
  # https://blog.anheyu.com/posts/52d8.html https://blog.zhheo.com/p/32776e99.html https://blog.meta-code.top/2022/06/18/2022-73/
  source: car
  # pace theme (see https://codebyzach.github.io/pace/)
  pace_css_url: 
  avatar: # 自定加载动画义头像, heo 动画使用
  load_color: '#37474f'
  load_image: https://images.unsplash.com/photo-1572666341285-c8cb9790ca50?q=80&w=6000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D # image 动画使用
```

**配置项参数说明**:

- enable： 控制加载动画的开关，取值有true和false，true开启，false关闭。
- load_color： 该配置项为自定义加载动画背景颜色。默认值为 `#37474f`,使用时注意用单引号''包起来，不然会被识别成注释符。这个配置项最大的作用是配合load_image使用的图片的背景色，可以用取色器提取自定义图片的主要色调，以达到图片和背景融为一体的效果。
- source： 控制加载动画的样式:
  - car: 小汽车
  - heo: heo张洪同款
  - default: 是主题原版的盒子加载动画
  - gear: 是旋转齿轮加载动画
  - ironheart: 是钢铁侠核心加载动画
  - scarecrow: 是稻草人跳动加载动画
  - triangles: 是旋转三角加载动画
  - wizard: 是巫师施法加载动画
  - image: 为自定义添加静态图片或gif作为加载动画。
- load_image：该配置项的生效前提是 load_style 设置为 image,内容填写图床链接或者本地相对地址。

## 问题参考

按照上述配置完成后, 只需要修改主题配置即可方便切换 loading 动画样式.

上述除了 car loading 动画跟原博客有差异外(主要是做了主题适配), 其他配置项跟 [【Hexo博客】自定义Butterfly主题 Loading 加载动画](https://blog.meta-code.top/2022/06/18/2022-73/) 完全一致(除了文件路径).

其他问题可参考原博客:

{% link 【Hexo博客】自定义Butterfly主题 Loading 加载动画, 百里飞洋 Barry-Flynn, https://blog.meta-code.top/2022/06/18/2022-73/ %}

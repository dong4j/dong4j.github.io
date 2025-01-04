var posts=["posts/7e89/","posts/5f5/","posts/598d/","posts/394d/","posts/b051/","posts/3c58/","posts/5f6/","posts/8d9a/","posts/260b/","posts/20ab66ff/","posts/7774f295/","posts/f3b0024e/","posts/3a683908/","posts/5e9872c3/","posts/8dc39439/","posts/1fd7702b/","posts/a31e50a5/","posts/c1e0543/","posts/ca466aa0/","posts/22b8af79/","posts/6c5526f1/","posts/77edbced/","posts/33f5/","posts/82bb/","posts/c294/","posts/ee6d/","posts/564b/","posts/321ba84a/","posts/84ce/","posts/1f53/","posts/d5e1/","posts/3b36/","posts/6dfe/","posts/2739/","posts/cc96/","posts/ff21/","posts/7a6d/","posts/dde3/","posts/462b/","posts/44d3ec9b/","posts/278e3e03/","posts/f50183c1/","posts/6dc04ed2/","posts/ea742350/","posts/9c7f49a2/","posts/8366ec74/","posts/9fb70690/","posts/56e5b99c/","posts/c9eda116/","posts/50e2e964/","posts/5649be19/","posts/ac0a5116/","posts/a42dfdd6/","posts/345a28fd/","posts/3b7cca00/","posts/a2959ba3/","posts/b3fe09a9/","posts/286572f8/","posts/205ef910/","posts/81cae783/","posts/8872e19a/","posts/95aea2e1/","posts/a87e6e25/","posts/a65dfb13/","posts/a29c1a98/","posts/c43d4ea4/","posts/70b9e46a/","posts/62ae7a01/","posts/ff561974/","posts/b2f99cee/","posts/2c5b3e3a/","posts/d16c10eb/","posts/79fceeeb/","posts/22c0ef08/","posts/d03a684c/","posts/b0674c16/","posts/9cba1244/","posts/7ef4d1ad/","posts/d8c7081e/","posts/53d86ec9/","posts/e5eb73b9/","posts/8f42e00b/","posts/b158ae75/","posts/747eedc9/","posts/36b6823d/","posts/ffbf019e/","posts/508e9afc/","posts/a69881a6/","posts/d2f9713d/","posts/7dc8ea5f/","posts/ffa1ef45/","posts/4fa65dbc/","posts/9659e30c/","posts/4550261/","posts/958ae77b/","posts/91ad9ce3/","posts/f1601c3e/","posts/9b7d6e62/","posts/48598499/","posts/7244523f/","posts/6b3bea20/","posts/f20ffdb/","posts/f56310d4/","posts/8b9030ff/","posts/24a1ab9d/","posts/1553cb8c/","posts/5981a792/","posts/1bdd319f/","posts/205d1f36/","posts/845cfa4f/","posts/5f2cc770/","posts/958f9ffe/","posts/32516dfc/","posts/cd5f7bae/","posts/4d06da5c/","posts/603b8025/","posts/442823ed/","posts/31d0a22c/","posts/a5564900/","posts/f1e67b7e/","posts/c7d0ca57/","posts/29d7a15f/","posts/8705625e/","posts/d3a1d32e/","posts/42f151c0/","posts/71aa5641/","posts/ef65c071/","posts/88c12565/","posts/711ab194/","posts/23cbb67c/","posts/d9e151a4/","posts/350ed0bd/","posts/6dad3a8f/","posts/6bf37004/","posts/eb599575/","posts/72a223e0/","posts/4453ea00/","posts/79a8d4c5/","posts/fa8faa2e/","posts/6961d5gq/","posts/4f5fa1df/","posts/6961d5da/","posts/166cf996/","posts/a6380364/","posts/85a56b56/","posts/d2b51e2a/","posts/b533df62/","posts/5a428776/","posts/10ce2820/","posts/a886bfdb/","posts/692bb3c4/","posts/7f48a7fb/","posts/64d008b/","posts/b3298821/","posts/c8f7e252/","posts/21944767/","posts/569377f1/","posts/b89d16dd/","posts/6952e88b/","posts/858a1037/","posts/ab98e58e/","posts/28ed4a7f/","posts/8d8f656a/","posts/d73767c3/","posts/ac8eb277/","posts/10f60db1/","posts/f2cb7e19/","posts/da43da6e/","posts/d6e26bb5/","posts/ae39e951/","posts/d9189394/","posts/19e627d5/","posts/44bde9f9/","posts/ae6109b1/","posts/1fce8c1c/","posts/25473362/","posts/f335982/","posts/18363420/","posts/499585b/","posts/aca063f7/","posts/954087b4/","posts/a13702d6/","posts/22eab19d/","posts/7bb33d78/","posts/66515f3d/","posts/2a833323/","posts/68dfa52e/","posts/535f8b87/","posts/f0fe1ae8/","posts/aab1eaf1/","posts/90f41285/","posts/e954a744/","posts/ab083149/","posts/90881fe0/","posts/f1119903/","posts/348a7282/","posts/59843415/","posts/1556580b/","posts/570ace06/","posts/779e9fe6/","posts/6c8ae0af/","posts/53cebd27/","posts/ac4909f7/","posts/441dc39d/","posts/24294e79/","posts/390ff665/","posts/27c94bc/","posts/697d5753/","posts/f9bb212c/","posts/c3ab3ba4/","posts/329422b3/","posts/c89e3217/","posts/220ed6be/","posts/eee067eb/","posts/d366874c/","posts/64ccc6a0/","posts/ac4294eb/","posts/11d8b32d/","posts/d60eb45/","posts/5d1ffcf3/","posts/58a301ae/","posts/28877bf/","posts/fe7c7d2d/","posts/f941d9b7/","posts/b0abc087/","posts/2363f1e9/","posts/c8b315d3/","posts/aa0f783a/","posts/340249a9/","posts/c69e2769/","posts/3daa4bf4/","posts/ff9e7ddd/","posts/ca7b1ce7/","posts/b5d8b5d5/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };var friend_link_list=[{"name":"Hexo","link":"https://hexo.io/zh-tw/","avatar":"https://d33wubrfki0l68.cloudfront.net/6657ba50e702d84afb32fe846bed54fba1a77add/827ae/logo.svg","descr":"快速、简单且强大的网站框架"},{"name":"anzhiyu主题","link":"https://blog.anheyu.com/","avatar":"https://npm.elemecdn.com/anzhiyu-blog-static@1.0.4/img/avatar.jpg","descr":"生活明朗，万物可爱","siteshot":"https://npm.elemecdn.com/anzhiyu-theme-static@1.1.6/img/blog.anheyu.com.jpg"},{"name":"安知鱼","link":"https://anzhiy.cn/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/15/63232b7d91d22.jpg","descr":"生活明朗，万物可爱","siteshot":"https://npm.elemecdn.com/anzhiyu-blog@1.1.6/img/post/common/anzhiy.cn.jpg"},{"name":"Akilarの糖果屋","link":"https://akilar.top/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311fc9de6507.webp","descr":"期待您的光临！","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311fc39c5966.webp"},{"name":"张洪Heo","link":"https://blog.zhheo.com/","avatar":"https://zhheo.com/img/avatar.jpg","descr":"分享设计与科技生活","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311fc3959f82.webp"},{"name":"Leonus","link":"https://blog.leonus.cn/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/16/6324505c9890a.jpeg","descr":"进一寸有进一寸的欢喜。","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/09/16/6324505c98fae.jpg"},{"name":"山岳库博","link":"https://kmar.top/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/10/06/633e9c4c2786f.png","descr":"开发学习启发性二刺螈","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/10/06/633e9c4c3460b.jpg"},{"name":"Tianli","link":"https://tianli-blog.club","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/11/11/636db0d451fd0.webp","descr":"惟其不可能，所以才相信。","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/11/07/6368520c9e4e7.webp"},{"name":"Ariasaka","link":"https://yisous.xyz","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/12/11/6395bcc946fc9.png","descr":"人有悲欢离合 月有阴晴圆缺","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/12/11/6395bcc1502e5.png"},{"name":"杜老师说","link":"https://dusays.com","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/12/21/63a2acb9c07d0.png!linkavatar","descr":"师者，传道，授业，解惑！","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/12/21/63a2acb9c07d0.webp"},{"name":"凌冬","link":"https://lyr-2000.github.io","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311fd474e3dd.png!linkavatar","descr":"过去不优秀，不代表未来不精彩","siteshot":"https://image.thum.io/get/width/400/crop/800/allowJPG/wait/20/anzhiy.cn/https://lyr-2000.github.io"},{"name":"Fomalhaut🥝","link":"https://www.fomal.cc/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311ff42df52e.webp!linkavatar","descr":"Welcome to Fomalhaut🥝のTiny Home","siteshot":"https://img02.anzhiy.cn/thumbnails/303c9346ba832c2ea658a9048391ea47.png"},{"name":"Vinson","link":"https://sakura520.co/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311ff0644d0e.webp!linkavatar","descr":"梦想是一个天真的词，实现梦想是一个残酷的词","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311ff0719a8e.webp"},{"name":"小明","link":"https://xiaomingwy.com/","avatar":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311ff06570ae.webp!linkavatar","descr":"很多关系到最后不过是相识一场。","siteshot":"https://img02.anzhiy.cn/adminuploads/1/2022/09/02/6311ff068e51c.webp"}];
    var refreshNum = 1;
    function friendChainRandomTransmission() {
      const randomIndex = Math.floor(Math.random() * friend_link_list.length);
      const { name, link } = friend_link_list.splice(randomIndex, 1)[0];
      Snackbar.show({
        text:
          "点击前往按钮进入随机一个友链，不保证跳转网站的安全性和可用性。本次随机到的是本站友链：「" + name + "」",
        duration: 8000,
        pos: "top-center",
        actionText: "前往",
        onActionClick: function (element) {
          element.style.opacity = 0;
          window.open(link, "_blank");
        },
      });
    }
    function addFriendLinksInFooter() {
      var footerRandomFriendsBtn = document.getElementById("footer-random-friends-btn");
      if(!footerRandomFriendsBtn) return;
      footerRandomFriendsBtn.style.opacity = "0.2";
      footerRandomFriendsBtn.style.transitionDuration = "0.3s";
      footerRandomFriendsBtn.style.transform = "rotate(" + 360 * refreshNum++ + "deg)";
      const finalLinkList = [];
  
      let count = 0;

      while (friend_link_list.length && count < 3) {
        const randomIndex = Math.floor(Math.random() * friend_link_list.length);
        const { name, link, avatar } = friend_link_list.splice(randomIndex, 1)[0];
  
        finalLinkList.push({
          name,
          link,
          avatar,
        });
        count++;
      }
  
      let html = finalLinkList
        .map(({ name, link }) => {
          const returnInfo = "<a class='footer-item' href='" + link + "' target='_blank' rel='noopener nofollow'>" + name + "</a>"
          return returnInfo;
        })
        .join("");
  
      html += "<a class='footer-item' href='/link/'>更多</a>";

      document.getElementById("friend-links-in-footer").innerHTML = html;

      setTimeout(()=>{
        footerRandomFriendsBtn.style.opacity = "1";
      }, 300)
    };
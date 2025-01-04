(()=>{const t={API_URL:"https://twikoo.dong4j.ink:1024",ADMIN_EMAIL_MD5:"3435c7a74ba1cad3f5d57b0b61b9b25cee221b97599c47b32edbdb36038c5411",PAGE_SIZE:5,LOADING_GIF:"/images/loading.gif",async fetchComments(){const t=new AbortController,e=setTimeout((()=>t.abort()),5e3);try{const e=await fetch(this.API_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({event:"GET_RECENT_COMMENTS",includeReply:!0,pageSize:this.PAGE_SIZE}),signal:t.signal}),{data:n}=await e.json();return n}catch(t){return console.error("获取评论出错:",t),null}finally{clearTimeout(e)}},formatTimeAgo(t){const e=Math.floor((Date.now()-new Date(t))/1e3);return e<60?"刚刚":e<3600?`${Math.floor(e/60)}分钟前`:e<86400?`${Math.floor(e/3600)}小时前`:e<604800?`${Math.floor(e/86400)}天前`:new Date(t).toLocaleDateString("zh-CN",{month:"numeric",day:"numeric"})+"日"},formatContent:t=>t?t.replace(/<pre><code>[\s\S]*?<\/code><\/pre>/g,"[代码块]").replace(/<code>([^<]{4,})<\/code>/g,"[代码]").replace(/<code>([^<]{1,3})<\/code>/g,"$1").replace(/<img[^>]*>/g,"[图片]").replace(/<a[^>]*?>[\s\S]*?<\/a>/g,"[链接]").replace(/<[^>]+>/g,"").replace(/&(gt|lt|amp|quot|#39|nbsp);/g,(t=>({">":">","<":"<","&":"&",quot:'"',"#39":"'",nbsp:" "}[t.slice(1,-1)]))).replace(/\s+/g," ").trim():"",generateCommentHTML(t){const{created:e,comment:n,url:i,avatar:a,nick:o,mailMd5:s,id:r}=t,l=this.formatTimeAgo(e),c=this.formatContent(n);return`\n          <div class="aside-list-item" title="${c}" onclick="pjax.loadUrl('${i}#${r}')">\n            <div class="thumbnail">\n              <img class="aside-list-avatar" src="${a}" alt="avatar">\n            </div>\n            <div class="content">\n              <div class="aside-list-author">\n                ${o} ${s===this.ADMIN_EMAIL_MD5?'\n          <svg t="1731283534336" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="29337" width="22" height="22"><path d="M512 0C230.4 0 0 230.4 0 512s230.4 512 512 512 512-230.4 512-512S793.6 0 512 0z m291.84 366.08c-46.08 0-79.36 23.04-92.16 66.56l-163.84 358.4h-66.56L312.32 435.2c-17.92-46.08-46.08-71.68-89.6-71.68v-35.84H512v35.84h-40.96c-25.6 2.56-30.72 23.04-12.8 61.44l102.4 225.28 89.6-199.68c25.6-56.32 2.56-84.48-71.68-89.6v-35.84h225.28v40.96z" fill="#06c013" p-id="29338" data-spm-anchor-id="a313x.search_index.0.i73.2b2d3a81BgxnVW" class=""></path></svg>':""}\n                <span class="aside-list-date">${l}</span>\n              </div>\n              <div class="aside-list-content">${c}</div>\n            </div>\n          </div>\n        `},getErrorTemplate:(t,e)=>`\n          <div style="min-height: 346px;display: flex;padding: 20px;text-align: center;justify-content: center;align-items: center;flex-direction: column;">\n            <i class="fas fa-${t}" style="font-size: 2rem; color: ${"exclamation-circle"===t?"#ff6b6b":"#999"}; margin-bottom: 10px;"></i>\n            <p style="color: #666;margin: 0;">${e}</p>\n          </div>\n        `,async insertComponent(){const t=document.getElementById("latest-comments");if(!t)return;t.innerHTML=`<div style="display: flex; justify-content: center; align-items: center; background-color: #f9f9f9; border-radius: 8px; overflow: hidden; width: 100%; max-width: 300px; max-height: 300px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);"><img src="${this.LOADING_GIF}" style="width: auto; height: 100%; object-fit: contain;"></div>`;const e=await this.fetchComments();let n;n=null===e?this.getErrorTemplate("exclamation-circle","评论加载失败，请稍后再试"):0===e.length?this.getErrorTemplate("comment-slash","还没有评论呢~ 快来抢沙发吧！"):e.map(this.generateCommentHTML.bind(this)).join(""),t.style.opacity="0",t.innerHTML=n,requestAnimationFrame((()=>{t.style.transition="opacity 0.3s ease-in",t.style.opacity="1"}))}};["DOMContentLoaded","pjax:success"].forEach((e=>document.addEventListener(e,(()=>{(()=>{const t=document.createElement("style");t.textContent="\n        .card-latest-comments .item-headline i {\n          color: var(--anzhiyu-main);\n        }\n  \n        .card-latest-comments .headline-right {\n          position: absolute;\n          right: 24px;\n          top: 20px;\n          transition: all 0.3s;\n          opacity: 0.6;\n        }\n  \n        .card-latest-comments .headline-right:hover {\n          color: var(--anzhiyu-main);\n          opacity: 1;\n          transform: rotate(90deg);\n        }\n  \n        .aside-list-author {\n          display: flex;\n          align-items: center;\n          font-weight: bold;\n          height: 22px;\n          gap: 5px;\n        }\n  \n        .aside-list-date {\n          font-size: 0.7rem;\n          font-weight: normal;\n          margin-left: auto;\n        }\n  \n        .aside-list-content {\n          font-size: 0.9rem;\n          overflow: hidden;\n          text-overflow: ellipsis;\n          white-space: nowrap;\n          text-decoration: none;\n          line-height: 1.2;\n        }\n  \n        .aside-list-item:last-child {\n          margin-bottom: 0!important;\n        }\n  \n        [data-theme='dark'] .aside-list-item-right {\n          filter: brightness(0.95);\n        }\n      ",document.head.appendChild(t)})(),t.insertComponent()}))))})();
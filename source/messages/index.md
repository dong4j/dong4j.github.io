---
title: 最新评论
aside: false
comments: false
---

<div class="author-content author-content-item single" style="background:url(https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/comments.webp) center /cover no-repeat!important">
    <div class="card-content">
        <div class="author-content-item-tips">速览</div>
        <span class="author-content-item-title">最新评论</span>
        <div class="content-bottom">
            <div class="tips">快速预览本站最新评论</div>
        </div>
        <div class="banner-button-group">
            <a class="banner-button" style="padding: 8px 12px;color: var(--anzhiyu-white);" onclick="pjax.loadUrl(&quot;/about&quot;)" data-pjax-state="">
                <i class="anzhiyufont anzhiyu-icon-arrow-circle-right" style="font-size:22px;margin-right:.25rem"></i>
                <span class="banner-button-text">关于本人</span>
            </a>
        </div>
    </div>
</div>

<div id="comments-page">
    <img src="/images/loading.gif">
</div>

<style>
/* 全局样式 */
h1 {
    display: none;
}

div#page {
    background: none !important;
    box-shadow: none;
    padding: 0;
    border: none;
}

/* 评论页面容器 */
#comments-page {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    width: 100%;
    margin-top: 1.5rem;
    justify-content: center;
}

/* 评论卡片基础样式 */
.comment-card {
    position: relative;
    width: calc(100% / 4 - 9px);
    border-radius: 12px;
    border: 1px solid var(--anzhiyu-card-border);
    padding: 14px;
    overflow: hidden;
    box-shadow: var(--anzhiyu-shadow-border);
    animation: slide-in .6s .4s backwards;
    background-color: var(--anzhiyu-card-bg);
    transition: all .3s ease-in-out;
}

.comment-card:hover {
    border: 1px solid var(--anzhiyu-main);
}

/* 评论信息区域 */
.comment-info {
    padding-bottom: 5px;
    border-bottom: 2px dashed var(--anzhiyu-theme-op);
}

.comment-information {
    display: flex;
    flex-direction: column;
}

.comment-user {
    font-weight: bold;
}

.comment-time {
    font-size: 12px;
    color: var(--anzhiyu-secondtext);
}

/* 评论内容 */
.comment-content {
    position: relative;
    z-index: 3;
    overflow: hidden;
    padding-top: 5px;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

/* 头像样式 */
.avatar-wrapper {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    width: 100px;
    height: 100px;
    border-radius: 50%;
    opacity: 0.4;
    transition: all 0.3s ease-in-out;
    filter: blur(3px);
    background-size: cover;
    background-position: center;
}

.comment-card:hover .avatar-wrapper {
    transform: translateY(-50%) scale(1.1);
    opacity: 0.6;
}

/* 响应式布局 */
@media (max-width: 1024px) {
    .comment-card {
        width: calc(100% / 2 - 6px);
    }
}

@media (max-width: 768px) {
    .comment-card {
        width: 100%;
    }
    .banner-button-group {
        display: none;
    }
}
</style>
<script>
(() => {
  const MessageComments = {
    API_URL: 'https://twikoo.dong4j.ink:1024', // 这里填入你的Twikoo服务器地址
    ADMIN_EMAIL_MD5: '3435c7a74ba1cad3f5d57b0b61b9b25cee221b97599c47b32edbdb36038c5411', // 这里填入你的邮箱md5值
    PAGE_SIZE: 100, // 显示的评论数量 好像最多也就100个

    async fetchComments() {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 5000);

      try {
        const response = await fetch(this.API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            event: 'GET_RECENT_COMMENTS',
            includeReply: true,
            pageSize: this.PAGE_SIZE
          }),
          signal: controller.signal
        });

        const { data } = await response.json();
        return data;
      } catch (error) {
        console.error('获取评论出错:', error);
        return null;
      } finally {
        clearTimeout(timeoutId);
      }
    },

    formatTimeAgo(timestamp) {
      const diff = Math.floor((Date.now() - new Date(timestamp)) / 1000);
      if (diff < 60) return '刚刚';
      if (diff < 3600) return `${Math.floor(diff / 60)}分钟前`;
      if (diff < 86400) return `${Math.floor(diff / 3600)}小时前`;
      if (diff < 604800) return `${Math.floor(diff / 86400)}天前`;

      return new Date(timestamp).toLocaleDateString('zh-CN', { month: 'numeric', day: 'numeric' }) + '日';
    },

    formatContent(content) {
      if (!content) return '';
      
      return content
        .replace(/<pre><code>[\s\S]*?<\/code><\/pre>/g, '[代码块]')
        .replace(/<code>([^<]{4,})<\/code>/g, '[代码]')
        .replace(/<code>([^<]{1,3})<\/code>/g, '$1')
        .replace(/<img[^>]*>/g, '[图片]')
        .replace(/<a[^>]*?>[\s\S]*?<\/a>/g, '[链接]')
        .replace(/<[^>]+>/g, '')
        .replace(/&(gt|lt|amp|quot|#39|nbsp);/g, m => 
          ({'>':'>', '<':'<', '&':'&', 'quot':'"', '#39':"'", 'nbsp':' '})[m.slice(1,-1)])
        .replace(/\s+/g, ' ')
        .trim();
    },

    generateCommentHTML(comment) {
      const { created, comment: content, url, avatar, nick, mailMd5, id } = comment;
      const timeAgo = this.formatTimeAgo(created);
      const formattedContent = this.formatContent(content);
      const adminBadge = mailMd5 === this.ADMIN_EMAIL_MD5 ? '<i class="fa fa-check-circle" style="color: #57bd6a; margin-left: 5px;"></i>' : '';

      return `
        <div class="comment-card" onclick="pjax.loadUrl('${url}#${id}')" title="点击查看评论">
          <div class="avatar-wrapper" style="background-image: url('${avatar}');"></div>
          <div class="comment-info">
            <div class="comment-information">
              <span class="comment-user">
                ${nick} ${adminBadge}
              </span>
              <span class="comment-time">${timeAgo}</span>
            </div>
          </div>
          <div class="comment-content">${formattedContent}</div>
        </div>
      `;
    },

    getErrorTemplate(message) {
      return `<p style="text-align: center; color: #666;">${message}</p>`;
    },

    async init() {
      const container = document.querySelector('#comments-page');
      if (!container) return;

      const comments = await this.fetchComments();
      let content;

      if (comments === null) {
        content = this.getErrorTemplate('加载评论时出错，请稍后再试');
      } else if (comments.length === 0) {
        content = this.getErrorTemplate('没有找到相关评论');
      } else {
        content = comments.map(this.generateCommentHTML.bind(this)).join('');
      }

      container.innerHTML = content;

      requestAnimationFrame(() => {
        container.querySelectorAll('.comment-card').forEach(el => {
          el.style.opacity = '1';
        });
      });
    }
  };

  ['DOMContentLoaded', 'pjax:success'].forEach(event => 
    document.addEventListener(event, () => MessageComments.init())
  );
})();
</script>

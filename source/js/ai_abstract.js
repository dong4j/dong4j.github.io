(function () {
    const {
      randomNum,
      basicWordCount,
      btnLink,
      key: AIKey,
      Referer: AIReferer,
      gptName,
      switchBtn,
      mode: initialMode,
    } = GLOBAL_CONFIG.postHeadAiDescription;
  
    const { title, postAI, pageFillDescription } = GLOBAL_CONFIG_SITE;
  
    let lastAiRandomIndex = -1;
    let animationRunning = true;
    let mode = initialMode;
    let refreshNum = 0;
    let prevParam;
    let audio = null;
    let isPaused = false;
    let summaryID = null;
  
    const post_ai = document.querySelector(".post-ai-description");
    const aiTitleRefreshIcon = post_ai.querySelector(".ai-title .anzhiyufont.anzhiyu-icon-arrow-rotate-right");
    let aiReadAloudIcon = post_ai.querySelector(".anzhiyu-icon-circle-dot");
    const explanation = post_ai.querySelector(".ai-explanation");
  
    let aiStr = "";
    let aiStrLength = "";
    let delayInit = 600;
    let indexI = 0;
    let indexJ = 0;
    let timeouts = [];
    let elapsed = 0;
  
    const observer = createIntersectionObserver();
    const aiFunctions = [introduce, aiTitleRefreshIconClick, aiRecommend, aiGoHome, subscribe];
  
    const aiBtnList = post_ai.querySelectorAll(".ai-btn-item");
    const filteredHeadings = Array.from(aiBtnList).filter(heading => heading.id !== "go-tianli-blog").filter(heading => heading.id !== "go-comment");
    filteredHeadings.forEach((item, index) => {
      item.addEventListener("click", () => {
        aiFunctions[index]();
      });
    });
  
    document.getElementById("ai-tag").addEventListener("click", onAiTagClick);
    aiTitleRefreshIcon.addEventListener("click", onAiTitleRefreshIconClick);
    document.getElementById("go-tianli-blog").addEventListener("click", () => {
      window.open(btnLink, "_blank");
    });
    document.getElementById("go-comment").addEventListener("click", () => {
        anzhiyu.scrollToDest(document.body.scrollHeight, 500)
    });
    aiReadAloudIcon.addEventListener("click", readAloud);
  
    async function readAloud() {
      if (!summaryID) {
        anzhiyu.snackbarShow("摘要还没加载完呢，请稍后。。。");
        return;
      }
      aiReadAloudIcon = post_ai.querySelector(".anzhiyu-icon-circle-dot");
      aiReadAloudIcon.style.opacity = "0.2";
      if (audio && !isPaused) {
        audio.pause();
        isPaused = true;
        aiReadAloudIcon.style.opacity = "1";
        aiReadAloudIcon.style.animation = "";
        aiReadAloudIcon.style.cssText = "animation: ''; opacity: 1;cursor: pointer;";
        return;
      }
  
      if (audio && isPaused) {
        audio.play();
        isPaused = false;
        aiReadAloudIcon.style.cssText = "animation: breathe .5s linear infinite; opacity: 0.2;cursor: pointer";
        return;
      }
  
      const options = {
        key: AIKey,
        Referer: AIReferer,
      };
      const requestParams = new URLSearchParams({
        key: options.key,
        id: summaryID,
      });
  
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Referer: options.Referer,
        },
      };
  
      try {
        const response = await fetch(`https://summary.tianli0.top/audio?${requestParams}`, requestOptions);
        if (response.status === 403) {
          console.error("403 refer与key不匹配。");
        } else if (response.status === 500) {
          console.error("500 系统内部错误");
        } else {
          const audioBlob = await response.blob();
          const audioURL = URL.createObjectURL(audioBlob);
          audio = new Audio(audioURL);
          audio.play();
          aiReadAloudIcon.style.cssText = "animation: breathe .5s linear infinite; opacity: 0.2;cursor: pointer";
          audio.addEventListener("ended", () => {
            audio = null;
            aiReadAloudIcon.style.opacity = "1";
            aiReadAloudIcon.style.animation = "";
          });
        }
      } catch (error) {
        console.error("请求发生错误❎");
      }
    }
    if (switchBtn) {
      document.getElementById("ai-Toggle").addEventListener("click", changeShowMode);
    }
  
    aiAbstract();
    showAiBtn();
  
    function createIntersectionObserver() {
      return new IntersectionObserver(
        entries => {
          let isVisible = entries[0].isIntersecting;
          animationRunning = isVisible;
          if (animationRunning) {
            delayInit = indexI === 0 ? 200 : 20;
            timeouts[1] = setTimeout(() => {
              if (indexJ) {
                indexI = 0;
                indexJ = 0;
              }
              if (indexI === 0) {
                explanation.innerHTML = aiStr.charAt(0);
              }
              requestAnimationFrame(animate);
            }, delayInit);
          }
        },
        { threshold: 0 }
      );
    }
  
    function animate(timestamp) {
      if (!animationRunning) {
        return;
      }
      if (!animate.start) animate.start = timestamp;
      elapsed = timestamp - animate.start;
      if (elapsed >= 20) {
        animate.start = timestamp;
        if (indexI < aiStrLength - 1) {
          let char = aiStr.charAt(indexI + 1);
          let delay = /[,.，。!?！？]/.test(char) ? 150 : 20;
          if (explanation.firstElementChild) {
            explanation.removeChild(explanation.firstElementChild);
          }
          explanation.innerHTML += char;
          let div = document.createElement("div");
          div.className = "ai-cursor";
          explanation.appendChild(div);
          indexI++;
          if (delay === 150) {
            post_ai.querySelector(".ai-explanation .ai-cursor").style.opacity = "0.2";
          }
          if (indexI === aiStrLength - 1) {
            observer.disconnect();
            explanation.removeChild(explanation.firstElementChild);
          }
          timeouts[0] = setTimeout(() => {
            requestAnimationFrame(animate);
          }, delay);
        }
      } else {
        requestAnimationFrame(animate);
      }
    }
  
    function clearTimeouts() {
      if (timeouts.length) {
        timeouts.forEach(item => {
          if (item) {
            clearTimeout(item);
          }
        });
      }
    }
  
    function startAI(str, df = true) {
      indexI = 0;
      indexJ = 1;
      clearTimeouts();
      animationRunning = false;
      elapsed = 0;
      observer.disconnect();
      explanation.innerHTML = df ? "生成中. . ." : "请等待. . .";
      aiStr = str;
      aiStrLength = aiStr.length;
      observer.observe(post_ai);
    }
  
    async function aiAbstract(num = basicWordCount) {
      if (mode === "tianli") {
        await aiAbstractTianli(num);
      } else {
        aiAbstractLocal();
      }
    }
  
    async function aiAbstractTianli(num) {
      indexI = 0;
      indexJ = 1;
      clearTimeouts();
      animationRunning = false;
      elapsed = 0;
      observer.disconnect();
  
      num = Math.max(10, Math.min(2000, num));
      const options = {
        key: AIKey,
        Referer: AIReferer,
      };
      const truncateDescription = (title + pageFillDescription).trim().substring(0, num);
  
      const url = new URL(location.href);
      const pathSegments = url.pathname.split('/').filter(Boolean); // 过滤掉空字符串
      const id = pathSegments[pathSegments.length - 1]; // 获取最后一个部分
  
      const requestBody = {
        key: options.key,
        content: truncateDescription,
        url: id,
      };
  
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Referer: options.Referer,
        },
        body: JSON.stringify(requestBody),
      };
      console.info(truncateDescription.length);
      try {
        let animationInterval = null;
        let summary;
        if (animationInterval) clearInterval(animationInterval);
        animationInterval = setInterval(() => {
          const animationText = "生成中" + ".".repeat(indexJ);
          explanation.innerHTML = animationText;
          indexJ = (indexJ % 3) + 1;
        }, 500);
        const response = await fetch(`https://summary.dong4j.ink:1024/summary`, requestOptions);
        let result;
        if (response.status === 403) {
          result = {
            summary: "403 refer与key不匹配。",
          };
        } else if (response.status === 500) {
          result = {
            summary: "500 系统内部错误",
          };
        } else {
          result = await response.json();
        }
  
        summary = result.summary.trim();
        summaryID = result.id;
  
        setTimeout(() => {
          aiTitleRefreshIcon.style.opacity = "1";
        }, 300);
        if (summary) {
          startAI(summary);
        } else {
          startAI("摘要获取失败!!!请检查Tianli服务是否正常!!!");
        }
        clearInterval(animationInterval);
      } catch (error) {
        console.error(error);
        explanation.innerHTML = "发生异常" + error;
      }
    }
  
    function aiAbstractLocal() {
      const strArr = postAI.split(",").map(item => item.trim());
      if (strArr.length !== 1) {
        let randomIndex = Math.floor(Math.random() * strArr.length);
        while (randomIndex === lastAiRandomIndex) {
          randomIndex = Math.floor(Math.random() * strArr.length);
        }
        lastAiRandomIndex = randomIndex;
        startAI(strArr[randomIndex]);
      } else {
        startAI(strArr[0]);
      }
      setTimeout(() => {
        aiTitleRefreshIcon.style.opacity = "1";
      }, 600);
    }
  
    function aiRecommend() {
      indexI = 0;
      indexJ = 1;
      clearTimeouts();
      animationRunning = false;
      elapsed = 0;
      explanation.innerHTML = "生成中. . .";
      aiStr = "";
      aiStrLength = "";
      observer.disconnect();
      timeouts[2] = setTimeout(() => {
        explanation.innerHTML = recommendList();
      }, 600);
    }
  
    function recommendList() {
      let thumbnail = document.querySelectorAll(".relatedPosts-list a");
      if (!thumbnail.length) {
        const cardRecentPost = document.querySelector(".card-widget.card-recent-post");
        if (!cardRecentPost) return "";
  
        thumbnail = cardRecentPost.querySelectorAll(".aside-list-item a");
  
        let list = "";
        for (let i = 0; i < thumbnail.length; i++) {
          const item = thumbnail[i];
          list += `<div class="ai-recommend-item"><span class="index">${
            i + 1
          }：</span><a href="javascript:;" onclick="pjax.loadUrl('${item.href}')" title="${
            item.title
          }" data-pjax-state="">${item.title}</a></div>`;
        }
  
        return `很抱歉，无法找到类似的文章，你也可以看看本站最新发布的文章：<br /><div class="ai-recommend">${list}</div>`;
      }
  
      let list = "";
      for (let i = 0; i < thumbnail.length; i++) {
        const item = thumbnail[i];
        list += `<div class="ai-recommend-item"><span>推荐${
          i + 1
        }：</span><a href="javascript:;" onclick="pjax.loadUrl('${item.href}')" title="${
          item.title
        }" data-pjax-state="">${item.title}</a></div>`;
      }
  
      return `推荐文章：<br /><div class="ai-recommend">${list}</div>`;
    }
  
    function aiGoHome() {
      startAI("正在前往博客主页...", false);
      timeouts[2] = setTimeout(() => {
        if (window.pjax) {
          pjax.loadUrl("/");
        } else {
          location.href = location.origin;
        }
      }, 1000);
    }

    function subscribe() {
        startAI("正在前往订阅页面...", false);
        timeouts[2] = setTimeout(() => {
            if (window.pjax) {
              pjax.loadUrl("/subscribe/");
            } else {
              location.href = location.origin;
            }
          }, 1000);
      }
  
    function introduce() {
      if (mode == "tianli") {
        startAI("我是文章辅助AI: SummaryGPT，点击下方的按钮，让我生成本文简介、推荐相关文章等。");
      } else {
        startAI(`我是文章辅助AI: ${gptName}GPT，点击下方的按钮，让我生成本文简介、推荐相关文章等。`);
      }
    }
  
    function aiTitleRefreshIconClick() {
      aiTitleRefreshIcon.click();
    }
  
    function onAiTagClick() {
      if (mode === "tianli") {
        post_ai.querySelectorAll(".ai-btn-item").forEach(item => (item.style.display = "none"));
        document.getElementById("go-tianli-blog").style.display = "block";
        startAI(
          "你好 🎉！我是 dong4j 博客的 AI 文章摘要生成助理 SummaryGPT，一款基于本地部署的大型语言模型提供的生成式 AI 服务。我的主要职责是预生成和展示文章摘要。请注意，你无法直接与我交流。如果你也想拥有一个这样的文章摘要助手，请查阅下方的详细部署指南。"
        );
      } else {
        post_ai.querySelectorAll(".ai-btn-item").forEach(item => (item.style.display = "block"));
        document.getElementById("go-tianli-blog").style.display = "none";
        startAI(
          `你好 🎉，我是本站文章摘要生成助理 ${gptName}GPT，使用了预先生成的文章摘要。我在这里只负责摘要的显示，你无法与我直接沟通。`
        );
      }
    }
  
    function onAiTitleRefreshIconClick() {
      const truncateDescription = (title + pageFillDescription).trim().substring(0, basicWordCount);
  
      aiTitleRefreshIcon.style.opacity = "0.2";
      aiTitleRefreshIcon.style.transitionDuration = "0.3s";
      aiTitleRefreshIcon.style.transform = "rotate(" + 360 * refreshNum + "deg)";
      if (truncateDescription.length <= basicWordCount) {
        let param = truncateDescription.length - Math.floor(Math.random() * randomNum);
        while (param === prevParam || truncateDescription.length - param === prevParam) {
          param = truncateDescription.length - Math.floor(Math.random() * randomNum);
        }
        prevParam = param;
        aiAbstract(param);
      } else {
        let value = Math.floor(Math.random() * randomNum) + basicWordCount;
        while (value === prevParam || truncateDescription.length - value === prevParam) {
          value = Math.floor(Math.random() * randomNum) + basicWordCount;
        }
        aiAbstract(value);
      }
      refreshNum++;
    }
  
    function changeShowMode() {
      mode = mode === "tianli" ? "local" : "tianli";
      if (mode === "tianli") {
        document.getElementById("ai-tag").innerHTML = "SummaryGPT";
  
        aiReadAloudIcon.style.opacity = "1";
        aiReadAloudIcon.style.cursor = "pointer";
      } else {
        aiReadAloudIcon.style.opacity = "0";
        aiReadAloudIcon.style.cursor = "auto";
        if ((document.getElementById("go-tianli-blog").style.display = "block")) {
          document.querySelectorAll(".ai-btn-item").forEach(item => (item.style.display = "block"));
          document.getElementById("go-tianli-blog").style.display = "none";
        }
        document.getElementById("ai-tag").innerHTML = gptName + " GPT";
      }
      aiAbstract();
    }
  
    function showAiBtn() {
      if (mode === "tianli") {
        document.getElementById("ai-tag").innerHTML = "SummaryGPT";
      } else {
        document.getElementById("ai-tag").innerHTML = gptName + " GPT";
      }
    }
  })();
  
const vh=1*window.innerHeight;document.documentElement.style.setProperty("--vh",`${vh}px`),window.addEventListener("resize",(()=>{let e=1*window.innerHeight;document.documentElement.style.setProperty("--vh",`${e}px`)})),document.addEventListener("DOMContentLoaded",(e=>{const t=new URLSearchParams(window.location.search).get("replyText");t?(document.getElementById("wechat-need-reply").style.display="flex",document.getElementById("wechat-need-reply-text").textContent=t):document.getElementById("wechat-need-reply").style.display="none",document.getElementById("wechat-need-reply-copybtn").addEventListener("click",(function(){var e=document.getElementById("wechat-need-reply-text").innerText;navigator.clipboard.writeText(e).then((function(){console.log("Text copied to clipboard");var e=document.getElementById("wechat-need-reply-back");e.innerText="复制成功",e.style.color="green"})).catch((function(e){console.error("Could not copy text: ",e)}))}))}));
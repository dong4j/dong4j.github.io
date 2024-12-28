const oa_name = "Deo.典";
const oa_description = "分享设计与科技生活";
const web_beian = "蜀ICP备xxxxxx号";

function replaceText(elementId, newText) {
  var element = document.getElementById(elementId);
  if (element) {
      element.innerText = newText;
  } else {
      console.log("Element with ID '" + elementId + "' not found.");
  }
}

replaceText('wechatoa-name', oa_name);
replaceText('wechatoa-description', oa_description)
replaceText('web-beian', web_beian)
// 监听开发者工具打开事件
window.addEventListener('devtoolschange', function(event) {
    // 如果开发者工具已打开，进入无限调试模式
    if (event.detail.isOpen) {
      // 不断触发断点
      while (true) {
        debugger;
      }
      
      // 或者抛出异常
      throw new Error('Debug mode is not allowed!');
    }
  });
  
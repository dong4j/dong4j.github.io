// 彩带效果
function firework() {
  const duration = 30 * 1000; // 烟花效果持续时间（毫秒）
  const animationEnd = Date.now() + duration;
  const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 9999 };

  function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
  }

  const interval = setInterval(() => {
    const timeLeft = animationEnd - Date.now();

    if (timeLeft <= 0) {
      return clearInterval(interval);
    }

    const particleCount = 50 * (timeLeft / duration);
    // 使用 confetti 创建烟花效果
    confetti(
      Object.assign({}, defaults, {
        particleCount,
        origin: {
          x: randomInRange(0.1, 0.9),
          y: randomInRange(0.1, 0.5),
        },
      })
    );
  }, 250);
}

// 检查是否为特定日期范围或特定日期
// 检查是否为特定日期或日期范围
function isSpecialDay() {
  const specialDays = [
    '01-01', // 元旦
    '01-26:02-04', // 春节（范围示例）
    '10-01', // 国庆节
    '12-20:12-31', // 新年假期（示例）
    '01-26', // 手动添加测试日期
  ];

  const today = new Date();
  const formattedDate = `${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;

  for (const day of specialDays) {
    if (day.includes(':')) {
      // 处理日期范围
      const [start, end] = day.split(':');
      if (isDateInRange(formattedDate, start, end)) {
        return true;
      }
    } else if (day === formattedDate) {
      // 处理特定日期
      return true;
    }
  }

  return false;
}

// 检查当前日期是否在范围内
function isDateInRange(date, start, end) {
  const dateNum = parseInt(date.replace('-', ''), 10); // 转换成整数格式 MMDD
  const startNum = parseInt(start.replace('-', ''), 10);
  const endNum = parseInt(end.replace('-', ''), 10);
  return dateNum >= startNum && dateNum <= endNum;
}

const isHomePage = window.location.pathname === '/'; // 判断是否为首页
if (isHomePage && isSpecialDay()) {
  firework();
}


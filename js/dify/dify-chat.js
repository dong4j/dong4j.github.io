
window.difyChatbotConfig = {
    // 必填项，由 Dify 自动生成
    token: 'cDGYLPH6hn7yXsK9',
    // 可选项，默认为 false
    isDev: true,
    // 可选项，当 isDev 为 true 时，默认为 '[https://dev.udify.app](https://dev.udify.app)'，否则默认为 '[https://udify.app](https://udify.app)'
    baseUrl: 'http://127.0.0.1',
    // 可选项，可以接受除 `id` 以外的任何有效的 HTMLElement 属性，例如 `style`、`className` 等
    containerProps: {
        style: {
            backgroundColor: '#ABCDEF',
            width: '60px',
            height: '60px',
            borderRadius: '30px',
        },
    },
    // 可选项，是否允许拖动按钮，默认为 `false`
    draggable: true,
    // 可选项，允许拖动按钮的轴，默认为 `both`，可以是 `x`、`y`、`both`
    dragAxis: 'both',
    // 可选项，在 dify 聊天机器人中设置的输入对象
    inputs: {
        // 键是变量名
        // 例如：
        // name: "NAME"
    }
};
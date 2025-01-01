from pydantic import BaseModel
import unittest
import json
from utils import clean_md_whitespace
from openaiapi.client import generate as client_openaiapi
from ollama.client import generate as client_ollama

class Document(BaseModel):
    title: list[str]

def generate(content, type="openaiapi"):
    prompt = f"""
    请为以下博客内容生成多个有吸引力的标题，用于吸引读者点击阅读。标题应简洁、生动、有创意，并能准确概括文章的核心内容。
    附加说明：
    1. 尽量生成 10 个不同风格的标题，覆盖技术性、趣味性和通俗性。
    2. 如果内容中包含 HTML 标签，请忽略这些标签，仅提取文本内容进行分析。
    3. 标题不能包含 HTML 标签和 Markdown 相关的语法标签。
    4. 你必须以JSON格式响应，返回一个列表, 列表中包含多个标题，每个标题是一个字符串。
    5. 列表中每个标题的长度不能超过30个字符。
    6. 你需要从以下标题中学习待生成的标题的风格:
        1. 一文看懂通行密钥：无密码、更安全的未来，你该如何登录？
        2. 从被动接收到主动参与：我的 AI 辅助学习方法论 
        3. 新年记录新生活：我的手账体系给你参考
        4. 本地大模型之路（一）：大模型的是什么、为什么以及怎么选
        5. 新面孔背后的老故事：watchOS 表盘背后的秘密
        6. 教程，5分钟让你变内存超频高手，简单轻松又安全，技嘉篇
        7. 5分钟搞定！小米官方HomeAssistant插件安装教程与实测
        8. 微信推送NAS预警消息！免费快速搭建攻略
        9. 我的技嘉酷睿i5 13400F组装主机初体验
        10. Docker实战：轻松部署SurveyKing与考试系统
        11. 从零打造高效的浏览器书签系统
        12. 让 AI 给新闻把把关：基于 Tasker 的资讯过滤与播报
        13. 如何用 AI 重塑我们的信息获取流程？
        14. 我们需要怎样的 AI 内容总结助手？
        15. 从零开始认识 API，把网页信息化为己用
        16. 如何用 Make 自动化将即刻动态同步到 Notion
        17. 规划库存、减少浪费：以 Grocy 为数据库的物品管理方案
        18. 如何利用可视化来辅助个人知识管理——Obsidian 实践
        19. 有人的地方就有江湖，聊聊我眼中的「价值」与「人脉」
        20. 想写就写，灵思无疆：用自动化部署让写作更得心应手
        21. 大厂程序员都在用什么工具绘图？Handraw: 支持中文手写效果的 Excalidraw
        22. 基于 n8n 的开源自动化：以滴答清单同步 Notion 为例
        23. 微信把文件都改成了只读，我找 ChatGPT 问到了药方
        24. 从「是什么」到「怎么做」，一口气入门快捷指令
    """

    if type == "openaiapi":
        return client_openaiapi(prompt, content, response_format=Document)
    elif type == "ollama":
        prompt = prompt + f"""
        请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本

        CONTENT START HERE

        {content}

        CONTENT END HERE
        你必须以JSON格式响应，键为'title'，值是字符串标签的数组。
        """
        return client_ollama(prompt)

class TestMathFunctions(unittest.TestCase):
    def test_generate(self):
        blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")

        # 调用 generate 函数
        result_ollama = generate(blog_content, type="ollama")
        result_openai = generate(blog_content, type="openaiapi")

        # 验证返回结果是否是 JSON 对象
        for result in [result_ollama, result_openai]:
            # 如果返回的是 JSON 格式字符串，则需要解析
            if isinstance(result, str):
                result = json.loads(result)

            # 打印返回数据
            print("Generated result:", result)

            self.assertIn("title", result, "Result does not contain 'title' field.")
            self.assertIsInstance(result["title"], list, "'title' is not a list.")

if __name__ == "__main__":
    unittest.main()



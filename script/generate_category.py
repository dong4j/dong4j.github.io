# Example: reuse your existing OpenAI setup
from openai import OpenAI
from pydantic import BaseModel
import json
import re
from utils import clean_md_whitespace

class Docment(BaseModel):
    title: list[str]

def generate(content, usemodel="default"):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # 构造 prompt
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
    """

    completion = client.beta.chat.completions.parse(
        model=usemodel,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ],
        temperature=0.7,  # 您可以根据需要调整这个参数
        response_format=Docment,
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2020/homelab-upgrade-to-10g.md")
    # print(blog_content)
    titles = generate(blog_content, usemodel="glm-4-9b-chat-1m")
    
    if titles:
        results = json.loads(titles)
        print(json.dumps(results, indent=2,ensure_ascii=False))
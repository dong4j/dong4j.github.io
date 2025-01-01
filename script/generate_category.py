# Example: reuse your existing OpenAI setup
from openai import OpenAI
from pydantic import BaseModel
import json
import re
from utils import clean_md_whitespace,log

class Docment(BaseModel):
    recommend: str
    options: list[str]

def generate(content, usemodel="default", auto_replace=True):
    categories ={
        "options": [
            "新时代码农",
            "HomeLab:中年男人的快乐源泉",
            "AI:人工智能",
            "生活:生下来活下去",
            "转载内容",
            "经验分享",
            "我的项目",
            "闲聊杂谈",
            "软件推荐",
            "好物推荐",
            "翻译内容"
        ]
    }
    if not auto_replace:
        return json.dumps(categories)

    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # 构造 prompt
    prompt = f"""
    请根据我提供给你的博客内容的黑心主题为其选择一个最合适的文章分类。
    附加说明：
    1. 生成的分类必须是我给定的一下几个选项之一:
        {categories['options']}
    2. 如果涉及到编程与开发相关的关键字, 比如 Java, Spring, Redis, Rabbitmq, SQL, MySQL, JVM等, 全部划分到 '新时代码农' 这个分类。
    2. 将推荐的分类写入到 key 为 'recommend'，值为字符串格式的分类, 将我给的几个选项放入到 key 为 'options' 的列表中。
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
    blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")
    # print(blog_content)
    categories = generate(blog_content, usemodel="glm-4-9b-chat-1m", auto_replace=True)
    
    if categories:
        results = json.loads(categories)
        print(json.dumps(results, indent=2,ensure_ascii=False))
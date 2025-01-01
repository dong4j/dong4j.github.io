# Example: reuse your existing OpenAI setup
from openai import OpenAI
from pydantic import BaseModel
import json
import re
from utils import clean_md_whitespace

class Docment(BaseModel):
    category: str

def generate(content, usemodel="default"):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # 构造 prompt
    prompt = f"""
    请根据我提供给你的博客内容的黑心主题为其选择一个最合适的文章分类。
    附加说明：
    1. 生成的分类必须是我给定的一下几个选项之一:
        技术
        生活
        阅读
        情感
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
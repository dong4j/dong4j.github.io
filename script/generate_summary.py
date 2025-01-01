import requests
import re
from utils import clean_md_whitespace
from ollama.client import generate as client

def generate(content):
    # 构造 prompt
    prompt = f"""
    你是一个专业的内容总结生成助手。你的任务是为给定的博客内容进行总结, 字数在 100 字内。
    请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本，以下是规则：
    1. 仅返回一个完整的总结，不要添加额外的信息。
    2. 如果内容中包含 HTML 标签，请忽略这些标签，仅提取文本内容进行分析。
    3. 总结内容不能包含 HTML 标签和 Markdown 相关的语法标签。

    以下是需要处理的博客内容：

    CONTENT START HERE

    {content}

    CONTENT END HERE

    你必须以JSON格式响应，键为'summary'，值是字符串格式的总结内容。
    """

    return client(prompt)

if __name__ == "__main__":
    blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")
    result = generate(blog_content)
    if result:
        print(result)
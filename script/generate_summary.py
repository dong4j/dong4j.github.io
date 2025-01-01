import requests
import re
from utils import clean_md_whitespace

def generate(content, model="default"):
    """
    调用 Ollama API 生成博客摘要。
    
    :param content: 博客内容 (字符串)
    :param model: 使用的 Ollama 模型 (默认是 'default')
    :return: 生成的摘要 (字符串)
    """

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

    # print(blog_content)
    
    # 设置 Ollama API 的 URL
    url = f"http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "format": "json",
        "stream": False
    }
    
    # 发送 POST 请求到 Ollama API
    try:
        response = requests.post(url, json=data, stream=False)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        # 提取生成的摘要
        if "response" in data:
            return data["response"]
        else:
            print("没有从响应中获取到摘要内容！")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

if __name__ == "__main__":
    # 输入博客内容
    # blog_content = """
    # 标题：Ollama 模型的使用方法
    # 内容：Ollama 是一个强大的语言模型框架，可以用于生成内容、总结文档等。它支持多种模型类型，
    # 并且可以通过简单的 API 调用来实现复杂的文本生成任务。
    # 在这篇博客中，我们将介绍如何使用 Ollama，以及如何通过 Python 调用其 API 来生成内容。
    # """
    
    blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2020/homelab-upgrade-to-10g.md")
    result = generate(blog_content, model="qwen2")
    if result:
        print(result)
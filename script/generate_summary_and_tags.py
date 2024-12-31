import requests
import json
import re

def generate_summary(content, model="default"):
    """
    调用 Ollama API 生成博客摘要。
    
    :param content: 博客内容 (字符串)
    :param model: 使用的 Ollama 模型 (默认是 'default')
    :return: 生成的摘要 (字符串)
    """

    # 构造 prompt
    prompt = f"""
    你是一个专业的内容总结生成助手。你的任务是为给定的博客内容进行总结以及帮助进行自动生成标签。
    请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本，以下是总结规则：
    1. 生成的总结内容，长度在 100 到 300 字符之间。
    2. 仅返回一个完整的总结，不要添加额外的信息。
    3. 如果内容中包含 HTML 标签，请忽略这些标签，仅提取文本内容进行分析。
    4. 总结内容不能包含 HTML 标签和 Markdown 相关的语法标签。
    下面是标签生成规则:
    - 目标是多种多样的标签，包括广泛类别、特定关键词和潜在的子类别。
    - 标签语言必须为中文。
    - 标签最好是文案中的词, 比如 HomeLab, Java 等, 这些应该按照原文中出现的词来生成。
    - 如果是著名网站，你也可以为该网站添加一个标签。如果标签不够通用，不要包含它。
    - 内容可能包括cookie同意和隐私政策的文本，在标签时请忽略这些。
    - 目标是3-5个标签。
    - 如果没有好的标签，请留空数组。

    以下是需要处理的博客内容：

    CONTENT START HERE

    {content}

    CONTENT END HERE

    你必须以JSON格式响应，键为'summary'，值是字符串格式的总结内容, 键为'tags'，值是字符串标签的数组。
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
    
    with open("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2020/homelab-upgrade-to-10g.md", "r", encoding="utf-8") as file:
        blog_content = file.read()

    # 删除多余空行，但保留段落间的分隔
    blog_content = re.sub(r'\n\s*\n', '\n', blog_content)
    # 删除每行行首和行尾的多余空白符
    blog_content = "\n".join(line.strip() for line in blog_content.splitlines())
    # 生成摘要
    summary = generate_summary(blog_content, model="qwen2")
    
    # 输出摘要
    if summary:
        print(summary)
import os
import sys
import requests
import re
from io import StringIO
from ruamel.yaml import YAML
import json
import re
from datetime import datetime

"""
将指定目录下的所有 Markdown 文件中的 AI 标签替换为 AI 模型名称。
"""

def log(message):
    """
    打印日志信息，包含时间戳。
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# 自定义 YAML Dump 函数，保持缩进和格式
def dump_yaml(data):
    yaml = YAML()
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    # 使用 StringIO 来捕获输出
    stream = StringIO()
    yaml.dump(data, stream)
    
    # 获取字符串值并返回
    return stream.getvalue()

def get_all_md_files(directory, exclude_dir=None):
    """
    遍历指定目录，获取所有 Markdown 文件（排除指定目录）。
    """
    md_files = []
    for root, dirs, files in os.walk(directory):
        # 排除指定的目录s
        if exclude_dir and os.path.abspath(exclude_dir) in os.path.abspath(root):
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def find_md_file(base_dir, filename, exclude_dir=None):
    """
    在指定目录中查找特定的 Markdown 文件（排除指定目录）。
    """
    for root, dirs, files in os.walk(base_dir):
        # 排除指定的目录
        if exclude_dir and os.path.abspath(exclude_dir) in os.path.abspath(root):
            continue
        for file in files:
            if file == filename:
                return os.path.join(root, file)
    return None

def replace_ai_tags_in_md(md_file, base_dir, publish_dir):
    """
    替换 Markdown 文件中的 `ai` 标签，并保存到发布目录。
    """
    log(f"开始处理文件: {md_file}")
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取 Front-matter 部分
    front_matter_pattern = r"---\n(.*?)\n---\n"
    match = re.match(front_matter_pattern, content, re.DOTALL)
    
    if not match:
        log(f"文件 {md_file} 不包含有效的 Front-matter，跳过处理。")
        return

    front_matter = match.group(1)
    body = content[match.end():]  # Markdown 正文内容

    # 使用 YAML 解析 Front-matter
    data = YAML().load(front_matter)

    # 检查 ai 标签
    ai_tag = data.get('ai')
    description_tag = data.get('description')
    # 判断是否需要生成摘要
    need_generate_summary = not isinstance(ai_tag, list) or not description_tag

    if need_generate_summary:
        # 替换 `ai` 标签内容
        ai_summary = generate_summary(body)  # 调用摘要生成函数
        if ai_summary:
            if not isinstance(ai_tag, list):
                data['ai'] = [ai_summary]  # 设置或替换 ai 标签
                log(f"文件 {md_file} 生成 ai 摘要")
            if not description_tag:
                data['description'] = ai_summary  # 设置或替换 description 标签
                log(f"文件 {md_file} 生成 description 标签")

            # 将更新后的 Front-matter 转换回 YAML 格式
            updated_front_matter = dump_yaml(data)
            updated_content = f"---\n{updated_front_matter}---\n{body}"

            # 保存更新后的内容到原文件
            with open(md_file, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            log(f"已直接更新文件: {md_file}")
        else:
            log(f"未获取摘要，跳过文件")

def generate_summary(content):
    # 删除多余空行，但保留段落间的分隔
    content = re.sub(r'\n\s*\n', '\n', content)
    # 删除每行行首和行尾的多余空白符
    content = "\n".join(line.strip() for line in content.splitlines())
    # 生成摘要
    summary = generate_summary_from_ai(content, model="qwen2")
    # 解析 JSON 格式字符串，提取 summary 的值
    try:
        summary_data = json.loads(summary)
        summary = summary_data.get("summary", "").strip()
        if not summary:
            log("JSON 数据中没有找到 'summary' 字段或值为空。")
            return ''
    except json.JSONDecodeError as e:
        log(f"解析 JSON 数据失败: {e}")
        return ''
    
    log(f"生成摘要: {summary}")
    # 这里只是示例，替换为实际的摘要生成逻辑
    return summary

def generate_summary_from_ai(content, model="default"):
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

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    publish_dir = os.path.join(base_dir, 'publish')

    # 初始化要处理的 Markdown 文件列表
    md_files_to_process = []

    if not args:
        # 处理所有 Markdown 文件
        md_files_to_process = get_all_md_files(base_dir, exclude_dir=publish_dir)
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的 Markdown 文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(year_dir, exclude_dir=publish_dir)
        else:
            log(f"年份目录 {args[0]} 不存在。")
            return
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的 Markdown 文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename, exclude_dir=publish_dir)
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到 Markdown 文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return

    # 循环处理所有确定的 Markdown 文件
    for md_file in md_files_to_process:
        replace_ai_tags_in_md(md_file, base_dir, publish_dir)

if __name__ == "__main__":
    main()
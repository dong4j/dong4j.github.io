import os
import sys
import requests
import re
import json
import re
from utils import log, get_all_md_files, find_md_file, split_md, dump_md_yaml, clean_content_whitespace
from generate_summary_and_tags import generate as generate_summary_from_ai

"""
生成标签和总结并替换原文本的内容
"""


def replace_ai_tags_in_md(md_file, base_dir, publish_dir):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)

    if not result:
        return
    
    data = result['data']
    body = result['body']

    # 检查 ai 标签
    md_ai_tag = data.get('ai')
    description_tag = data.get('description')
    # 判断是否需要生成摘要
    need_generate_summary = not isinstance(md_ai_tag, list) or not description_tag

    need_update =False
    if need_generate_summary:
        # 替换 `ai` 标签内容
        ai_data = generate_summary_and_tags(body)  # 调用摘要生成函数
        summary = ai_data.get("summary", "").strip()
        if summary:
            if not isinstance(md_ai_tag, list):
                data['ai'] = [summary]  # 设置或替换 ai 标签
                log(f"文件 {md_file} 生成 ai 摘要")
            if not description_tag:
                data['description'] = summary  # 设置或替换 description 标签
                log(f"文件 {md_file} 生成 description 标签")
            need_update = True
        else:
            log(f"未获取摘要，跳过文件")

    md_tags = data.get('tags')
    if not isinstance(md_tags, list):
        # 替换 `tags` 标签内容
        ai_data = generate_summary_and_tags(body)  # 调用摘要生成函数
        tags = ai_data.get("tags", "")
        if tags:
            data['tags'] = tags
            log(f"文件 {md_file} 生成 tags")
            need_update = True
        else:
            log(f"未获取 tags，跳过文件")

    if need_update:
        dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body
    else:
        log(f"不需要更新文件")

def generate_summary_and_tags(content):
     # 删除多余空行，但保留段落间的分隔
    content = clean_content_whitespace(content)
    # 生成摘要
    summary = generate_summary_from_ai(content, model="qwen2")
    # 解析 JSON 格式字符串，提取 summary 的值
    try:
        return json.loads(summary)
    except json.JSONDecodeError as e:
        log(f"解析 JSON 数据失败: {e}")
        return ''

# def generate_summary_from_ai(content, model="default"):
#     """
#     调用 Ollama API 生成博客摘要。
    
#     :param content: 博客内容 (字符串)
#     :param model: 使用的 Ollama 模型 (默认是 'default')
#     :return: 生成的摘要 (字符串)
#     """

#     # 构造 prompt
#     prompt = f"""
#     你是一个专业的内容总结生成助手。你的任务是为给定的博客内容进行总结以及帮助进行自动生成标签。
#     请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本，以下是总结规则：
#     1. 生成的总结内容，长度在 100 到 300 字符之间。
#     2. 仅返回一个完整的总结，不要添加额外的信息。
#     3. 如果内容中包含 HTML 标签，请忽略这些标签，仅提取文本内容进行分析。
#     4. 总结内容不能包含 HTML 标签和 Markdown 相关的语法标签。
#     下面是标签生成规则:
#     - 目标是多种多样的标签，包括广泛类别、特定关键词和潜在的子类别。
#     - 标签语言必须为中文。
#     - 标签最好是文案中的词, 比如 HomeLab, Java 等, 这些应该按照原文中出现的词来生成。
#     - 如果是著名网站，你也可以为该网站添加一个标签。如果标签不够通用，不要包含它。
#     - 内容可能包括cookie同意和隐私政策的文本，在标签时请忽略这些。
#     - 目标是3-5个标签。
#     - 如果没有好的标签，请留空数组。

#     以下是需要处理的博客内容：

#     CONTENT START HERE

#     {content}

#     CONTENT END HERE

#     你必须以JSON格式响应，键为'summary'，值是字符串格式的总结内容, 键为'tags'，值是字符串标签的数组。
#     """

#     # print(blog_content)
    
#     # 设置 Ollama API 的 URL
#     url = f"http://localhost:11434/api/generate"
#     data = {
#         "model": model,
#         "prompt": prompt,
#         "format": "json",
#         "stream": False
#     }
    
#     # 发送 POST 请求到 Ollama API
#     try:
#         response = requests.post(url, json=data, stream=False)
#         response.raise_for_status()  # 检查请求是否成功
#         data = response.json()
#         # 提取生成的摘要
#         if "response" in data:
#             return data["response"]
#         else:
#             print("没有从响应中获取到摘要内容！")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"请求失败: {e}")
#         return None

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    publish_dir = os.path.join(base_dir, 'publish')

    # 初始化要处理的 Markdown 文件列表
    md_files_to_process = []

    """
    1. 不传任何参数, 则处理 source/_posts 下所有的文档(不包括 publish 目录);
    2. 传入年份参数，则处理指定年份的 Markdown 文件(不包括 publish 目录);
    3. 传入 Markdown 文件名，则处理指定的 Markdown (文件不包括 publish 目录);
    """
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
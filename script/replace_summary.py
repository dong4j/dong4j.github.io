import os
import sys
import json

from utils import log, get_process_md_files, dump_md_yaml, split_md, clean_content_whitespace, save_processed_file, load_processed_files
from generate_summary import generate as generate_summary_from_ai

"""
将 ai 和 description 字段替换为 AI 生成的摘要
"""

# 配置路径
PROCESSED_FILE = os.path.join(os.path.dirname(__file__), "processed_summary_files.txt")   # 已处理的文件记录

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

def replace_ai_tags_in_md(md_file):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)
    if not result:
        return
    
    data = result['data']
    body = result['body']
    
    # 替换 `ai` 标签内容
    ai_summary = generate_summary(body)  # 调用摘要生成函数
    if ai_summary:
        data['ai'] = [ai_summary]  # 设置或替换 ai 标签
        log(f"文件 {md_file} 生成 ai 摘要")
        data['description'] = ai_summary  # 设置或替换 description 标签
        log(f"文件 {md_file} 生成 description 标签")
        dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body
        save_processed_file(md_file, PROCESSED_FILE)
    else:
        log(f"未获取摘要，跳过文件")

def generate_summary(content):
    # 删除多余空行，但保留段落间的分隔
    content = clean_content_whitespace(content)
    # 生成摘要
    summary = generate_summary_from_ai(content)
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

def main():
    dicts = get_process_md_files(sys.argv[1:])

    md_files_to_process = dicts.get('files')

    # 加载已处理文件
    processed_files = load_processed_files(PROCESSED_FILE)

    # 获取所有 Markdown 文件
    md_files_to_process = [f for f in md_files_to_process if f not in processed_files]

    # 检查是否有未处理的文件
    if not md_files_to_process:
        log("没有需要处理的 Markdown 文件。")
        return

    # 循环处理所有确定的 Markdown 文件
    for md_file in md_files_to_process:
        replace_ai_tags_in_md(md_file, dicts.get('base_dir'), dicts.get('publish_dir'))
    log("==================摘要和标签生成完成==================")

if __name__ == "__main__":
    main()
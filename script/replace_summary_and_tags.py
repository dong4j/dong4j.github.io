import os
import sys
import json
import re
from utils import log, split_md, dump_md_yaml, clean_content_whitespace, get_process_md_files, save_processed_file, load_processed_files
from generate_summary_and_tags import generate as generate_summary_and_tags_from_ai

"""
1. 将 ai 和 description 字段替换为 AI 生成的摘要
2. 将 tags 和 keywords 字段替换为 AI 生成的标签
"""

# 配置路径
PROCESSED_FILE = "./processed_summary_files.txt"  # 已处理的文件记录

def replace_summary_and_tags_in_md(md_file):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)

    if not result:
        return
    
    data = result['data']
    body = result['body']

    need_update =False
    # 替换 `ai` 标签内容
    ai_data = generate_summary_and_tags(body)  # 调用摘要生成函数
    summary = ai_data.get("summary", "").strip()
    if summary:
        data['ai'] = [summary]  # 设置或替换 ai 标签
        log(f"{md_file} 替换 AI 摘要")
        data['description'] = summary  # 设置或替换 description 标签
        log(f"{md_file} 替换 description")
        need_update = True
    else:
        log(f"未获取摘要，跳过文件")

    tags = ai_data.get("tags", [])
    if tags:
        data['tags'] = tags
        log(f"{md_file} 替换 tags")
        # 不要直接使用 data['keywords'] = tags, 会直接生成 yaml 的锚点:
        # tags: &id001
        #   - AI模型
        # keywords: *id001
        data['keywords'] = list(tags)
        log(f"{md_file} 替换 keywords")
        need_update = True
    else:
        log(f"未获取 tags，跳过文件")

    if need_update:
        dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body
        save_processed_file(md_file, PROCESSED_FILE)
    else:
        log(f"不需要更新文件")

def generate_summary_and_tags(content):
     # 删除多余空行，但保留段落间的分隔
    content = clean_content_whitespace(content)
    result = generate_summary_and_tags_from_ai(content)
    # 解析 JSON 格式字符串，提取 summary 的值
    try:
        return json.loads(result)
    except json.JSONDecodeError as e:
        log(f"解析 JSON 数据失败: {e}")
        return ''

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
        replace_summary_and_tags_in_md(md_file)
    log("==================摘要和标签生成完成==================")


if __name__ == "__main__":
    main()
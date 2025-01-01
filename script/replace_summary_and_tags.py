import os
import sys
import json
import re
from utils import log, get_all_md_files, find_md_file, split_md, dump_md_yaml, clean_content_whitespace, get_process_md_files
from generate_summary_and_tags import generate as generate_summary_from_ai

"""
生成标签和总结并替换原文本的内容
"""


def replace_summary_and_tags_in_md(md_file, base_dir, publish_dir):
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
            # 不要直接使用 data['keywords'] = tags, 会直接生成 yaml 的锚点:
            # tags: &id001
            #   - AI模型
            # keywords: *id001
            data['keywords'] = list(tags)
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
    summary = generate_summary_from_ai(content)
    # 解析 JSON 格式字符串，提取 summary 的值
    try:
        return json.loads(summary)
    except json.JSONDecodeError as e:
        log(f"解析 JSON 数据失败: {e}")
        return ''

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        replace_summary_and_tags_in_md(md_file, dicts.get('base_dir'), dicts.get('publish_dir'))
    log("==================摘要和标签生成完成==================")
if __name__ == "__main__":
    main()
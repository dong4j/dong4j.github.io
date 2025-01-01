"""
将文章的 tags 写入到 keywords 字段中
"""
import os
import sys
from utils import log, get_process_md_files, split_md, dump_md_yaml

def replace_keywords_tags_in_md(md_file, base_dir, publish_dir):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)

    if not result:
        log("split_md returned None, skipping file.")
        return
    
    data = result['data']
    body = result['body']

    md_tags = data.get('tags')
    if md_tags is not None:
        log(f"将 tags 写入到 keywords 字段中: {md_tags}")
        data['keywords'] = list(md_tags)
    else:
        log("No tags found to write to keywords.")

    # 保存更新后的 YAML 和 body
    try:
        dump_md_yaml(md_file, data, body)
        log(f"文件已更新: {md_file}")
    except Exception as e:
        log(f"保存文件时出错: {e}")

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        replace_keywords_tags_in_md(md_file, dicts.get('base_dir'), dicts.get('publish_dir'))
    log("==================keywords 生成完成==================")

if __name__ == "__main__":
    main()
"""
将文章的 tags 写入到 keywords 字段中
"""
import os
import sys
from utils import log, get_all_md_files, find_md_file, split_md, dump_md_yaml

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
        replace_keywords_tags_in_md(md_file, base_dir, publish_dir)

if __name__ == "__main__":
    main()
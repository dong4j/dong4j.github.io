"""
清理 source/_posts 目录下未被引用的图片.
1. 不传任何参数则处理 source/_posts 目录下所 有Markdown 文件及其图片。
2. 传递一个参数，则处理指定年份的 Markdown 文件及其图片。
3. 传递一个 Markdown 文件名，则处理该Markdown文件和对应的图片。
"""

import os
import sys
from utils import extract_image_urls_from_md

def log(message):
    """
    打印中文日志信息。
    """
    print(f"日志：{message}")

def get_all_md_files(directory):
    """
    获取指定目录下的所有Markdown文件。
    """
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def find_md_file(directory, filename):
    """
    在指定目录及其子目录中查找指定的Markdown文件。
    """
    for root, _, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def get_referenced_images(md_file):
    """
    获取Markdown文件中引用的所有图片。
    """
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return extract_image_urls_from_md(content)

def clean_unreferenced_images(md_file):
    """
    清理未引用的图片。
    """

    image_dir = os.path.splitext(md_file)[0]
    if not os.path.isdir(image_dir):
        log(f"未找到文件 {md_file} 对应的图片目录。")
        return
    
    referenced_images = get_referenced_images(md_file)
    log(f"文件 {md_file} 中引用的图片：{referenced_images}")
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file not in referenced_images:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                log(f"已删除未引用的图片：{file_path}")

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    log(f"博客文章的基准目录：{base_dir}")

    if not args:
        # 处理所有文档和图片
        md_files = get_all_md_files(base_dir)
        log("正在处理所有Markdown文件和图片。")
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的文档和图片
        year_dir = os.path.join(base_dir, args[0])
        md_files = get_all_md_files(year_dir)
        log(f"正在处理年份 {args[0]} 的Markdown文件和图片。")
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文档和其资源文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename)
        if md_file:
            md_files = [md_file]
            log(f"正在处理Markdown文件：{md_file}")
        else:
            log(f"未找到Markdown文件 {md_filename}。")
            return
    else:
        log("参数无效。")
        return

    for md_file in md_files:
        clean_unreferenced_images(md_file)
    
    log("==================图片清理完成==================")

if __name__ == '__main__':
    main()

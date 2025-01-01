"""
清理 source/_posts 目录下未被引用的图片.
1. 不传任何参数则处理 source/_posts 目录下所 有Markdown 文件及其图片。
2. 传递一个参数，则处理指定年份的 Markdown 文件及其图片。
3. 传递一个 Markdown 文件名，则处理该Markdown文件和对应的图片。
"""

import os
import sys
from utils import extract_image_urls_from_md, log, get_process_md_files

def get_referenced_images(md_file):
    """
    获取Markdown文件中引用的所有图片。
    """
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return extract_image_urls_from_md(content)

def clean_unreferenced_images(md_file, exclude_extensions=None):
    """
    清理未引用的图片，支持排除特定格式的文件。

    :param md_file: Markdown 文件路径
    :param exclude_extensions: 要排除的文件扩展名列表（如 ['.keep', '.txt']），默认 None
    """
    if exclude_extensions is None:
        exclude_extensions = []

    image_dir = os.path.splitext(md_file)[0]
    if not os.path.isdir(image_dir):
        log(f"未找到文件 {md_file} 对应的图片目录。")
        return
    
    referenced_images = get_referenced_images(md_file)
    log(f"文件 {md_file} 中引用的图片：{referenced_images}")

    for root, _, files in os.walk(image_dir):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            
            # 检查文件是否被引用或是否在排除列表中
            if file not in referenced_images and ext not in exclude_extensions:
                os.remove(file_path)
                log(f"已删除未引用的图片：{file_path}")
            else:
                log(f"保留文件：{file_path}")

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        clean_unreferenced_images(md_file, exclude_extensions=['.svg'])
    log("==================图片清理完成==================")

if __name__ == '__main__':
    main()

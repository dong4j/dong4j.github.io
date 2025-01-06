"""
清理 source/_posts 目录下未被引用的图片.
1. 不传任何参数则处理 source/_posts 目录下所 有Markdown 文件及其图片。
2. 传递一个参数，则处理指定年份的 Markdown 文件及其图片。
3. 传递一个 Markdown 文件名，则处理该Markdown文件和对应的图片。
"""

import os
import sys
from utils import log, get_process_md_files, find_all_image_tags, move_to_trash

def is_referenced(file_name, referenced_images):
    # 检查文件是否被引用
    # 提取文件名，忽略路径
    return any(file_name in ref for ref in referenced_images)

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
        return
    
    referenced_images = find_all_image_tags(md_file)

    for root, _, file_names in os.walk(image_dir):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            _, ext = os.path.splitext(file_name)
            
            # 检查文件是否被引用或是否在排除列表中
            if not is_referenced(file_name, referenced_images) and ext not in exclude_extensions:
                # 移动文件到废纸篓
                move_to_trash(file_path)
                log(f"已删除未引用的图片：{file_path}")

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        clean_unreferenced_images(md_file, exclude_extensions=['.svg'])
    log("==================图片清理完成==================")

if __name__ == '__main__':
    main()

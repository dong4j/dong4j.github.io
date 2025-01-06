"""
遍历图片便签, 将图片修改为相对位置:
![xxx](xxx.png) -> ![xxx](./md名称/xxx.png)
"""

import os
import sys
import re
from utils import log, get_process_md_files, find_all_image_tags, extract_image_url_from_tag, is_url

def is_referenced(file_name, referenced_images):
    # 检查文件是否被引用
    # 提取文件名，忽略路径
    return any(file_name in ref for ref in referenced_images)

def add_relative_path(md_file, exclude_extensions=None):
    if exclude_extensions is None:
        exclude_extensions = []

    image_dir = os.path.splitext(md_file)[0]
    if not os.path.isdir(image_dir):
        return
    
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取所有图片标签
    image_tags = find_all_image_tags(md_file)
    for tag in image_tags:
        image_name = extract_image_url_from_tag(tag)
        if not image_name or is_url(image_name):
            continue

        if image_name.startswith('/images') or image_name.startswith('./' + os.path.basename(image_dir)):
            continue
        else:
            # 只替换括号()内的内容
            new_tag = re.sub(r'\(.*?\)', f'({os.path.join("./" + os.path.basename(image_dir), image_name)})', tag)
            content = content.replace(tag, new_tag)
            log(f"替换标签 {tag} 为 {new_tag}")
        
     # 保存修改后的Markdown文件到发布目录
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        add_relative_path(md_file, exclude_extensions=[])
    log("==================图片处理完成==================")

if __name__ == '__main__':
    main()

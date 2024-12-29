import re
import os


import re

def find_all_image_tags(md_file):
    """
    从Markdown内容中提取所有图片标签。
    """
    pattern = r'!\[.*?\]\(.*?\)'
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
        return re.findall(pattern, content)

def extract_image_url_from_tag(image_tag):
    """
    从图片标签中提取图片URL。
    """
    # 正则表达式匹配括号内的URL
    pattern = r'\((.*?)\)'
    # 使用findall返回所有匹配的URL列表
    matches = re.findall(pattern, image_tag)
    # 如果找到匹配项，返回第一个匹配的URL
    if matches:
        return matches[0]
    # 如果没有找到匹配项，返回None
    return ''

def extract_image_urls_from_md(content):
    """
    从Markdown内容中提取图片URLs。
    """
    pattern = r'!\[.*?\]\((.*?)\)'
    return re.findall(pattern, content)

def is_url(full_image_path):
    """
    检查给定的路径是否为URL。
    """
    return full_image_path.lower().startswith(('http://', 'https://', 'www.'))

def get_all_md_files(directory, exclude_dir=None):
    md_files = []
    for root, dirs, files in os.walk(directory):
        if exclude_dir and exclude_dir in dirs:
            dirs.remove(exclude_dir)  # 排除指定的目录
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def find_md_file(directory, filename, exclude_dir=None):
    for root, dirs, files in os.walk(directory):
        if exclude_dir and exclude_dir in dirs:
            dirs.remove(exclude_dir)  # 排除指定的目录
        if filename in files:
            return os.path.join(root, filename)
    return None
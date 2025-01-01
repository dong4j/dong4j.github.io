import re
import os
import re
from datetime import datetime
from io import StringIO
from ruamel.yaml import YAML

def log(message):
    """
    打印日志信息，包含时间戳。
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

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
    """
    遍历指定目录，获取所有 Markdown 文件（排除指定目录）。
    """
    md_files = []
    for root, dirs, files in os.walk(directory):
        if exclude_dir and exclude_dir in dirs:
            dirs.remove(exclude_dir)  # 排除指定的目录
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def find_md_file(directory, filename, exclude_dir=None):
    """
    在指定目录中查找特定的 Markdown 文件（排除指定目录）。
    """
    for root, dirs, files in os.walk(directory):
        if exclude_dir and exclude_dir in dirs:
            dirs.remove(exclude_dir)  # 排除指定的目录
        if filename in files:
            return os.path.join(root, filename)
    return None

def load_md_yaml(md_file):
    result = split_md(md_file)
    # 将 data 和 body 通过字典返回
    return result['data']

def split_md(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取 Front-matter 部分
    front_matter_pattern = r"---\n(.*?)\n---\n"
    match = re.match(front_matter_pattern, content, re.DOTALL)
    
    if not match:
        log(f"文件 {md_file} 不包含有效的 Front-matter，跳过处理。")
        return

    front_matter = match.group(1)
    body = content[match.end():]  # Markdown 正文内容

    # 使用 YAML 解析 Front-matter
    data = load_yaml(front_matter)
    # 将 data 和 body 通过字典返回
    return {'data': data, 'body': body}


def dump_md_yaml(md_file, data, body):
    # 将更新后的 Front-matter 转换回 YAML 格式
    updated_front_matter = dump_yaml(data)
    updated_content = f"---\n{updated_front_matter}---\n{body}"

    # 保存更新后的内容到原文件
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# 自定义 YAML Dump 函数，保持缩进和格式
def dump_yaml(data):
    yaml = YAML()
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    # 使用 StringIO 来捕获输出
    stream = StringIO()
    yaml.dump(data, stream)
    
    # 获取字符串值并返回
    return stream.getvalue()

def load_yaml(content):
    return YAML().load(content)

def clean_content_whitespace(content):
    # 删除多余空行，但保留段落间的分隔
    content = re.sub(r'\n\s*\n', '\n', content)
    # 删除每行行首和行尾的多余空白符
    content = "\n".join(line.strip() for line in content.splitlines())
    return content

def clean_md_whitespace(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        blog_content = file.read()
    return clean_content_whitespace(blog_content)

def get_md_title(md_file):
    result = load_md_yaml(md_file)
    return result['title']
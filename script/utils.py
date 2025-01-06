import re
import os
import re
import shutil
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
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return extract_image_urls_from_md(content)

def extract_image_urls_from_md(content):
    """
    从Markdown内容中提取图片URLs。
    """
    pattern = r'!\[.*?\]\(.*?\)'
    all_image_tags = re.findall(pattern, content)
    return all_image_tags

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

def extract_image_desc_from_tag(image_tag):
    """
    从图片标签中提取图片的描述。
    """
    # 正则表达式匹配括号内的URL
    pattern = r'!\[(.*?)\]\(.*?\)'
    # 使用findall返回所有匹配的URL列表
    matches = re.findall(pattern, image_tag)
    # 如果找到匹配项，返回第一个匹配的URL
    if matches:
        return matches[0]
    # 如果没有找到匹配项，返回None
    return ''

def find_image_tag_by_description(md_content, description):
    # 正则表达式，匹配整个图片标签，并捕获描述部分
    pattern = r'!\[({})\]\(.*?\)'.format(re.escape(description))
    # 使用re.search来查找第一个匹配的图片标签
    match = re.search(pattern, md_content)
    # 如果找到匹配的标签，返回整个标签，否则返回None
    return match.group(0) if match else ''

def is_url(image_name):
    """
    检查给定的路径是否为URL。
    """
    return image_name.lower().startswith(('http://', 'https://', 'www.'))

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
        error_message = f"文件 {md_file} 不包含有效的 Front-matter(或者没有写任何内容?)，跳过处理。"
        log(error_message)
        raise ValueError(error_message)

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

def get_md_category(md_file):
    result = load_md_yaml(md_file)
    return result['categories']

def load_processed_files(processed_file):
    """
    加载已处理文件的列表。
    """
    if os.path.exists(processed_file):
        with open(processed_file, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_processed_file(md_file, processed_file):
    """
    保存已处理的文件。
    """
    with open(processed_file, 'a', encoding='utf-8') as f:
        f.write(md_file + "\n")


def get_process_md_files(args):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    publish_dir = os.path.join(base_dir, 'publish')
    log(f"博客文章的基准目录：{base_dir}")
    # 初始化要处理的 Markdown 文件列表
    md_files_to_process = []

    """
    1. 不传任何参数, 则处理 source/_posts 下所有的文档(不包括 publish 目录);
    2. 传入年份参数，则处理指定年份的 Markdown 文件(不包括 publish 目录);
    3. 传入 Markdown 文件名，则处理指定的 Markdown (文件不包括 publish 目录);
    """
    if not args:
        # 处理所有 Markdown 文件
        md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的 Markdown 文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(year_dir, exclude_dir='publish')
        else:
            log(f"年份目录 {args[0]} 不存在。")
            return
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的 Markdown 文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename, exclude_dir='publish')
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到 Markdown 文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return
    
    return {'files': md_files_to_process, 'base_dir': base_dir, 'publish_dir': publish_dir}
    
def move_to_trash(file_path):
    # 获取废纸篓的路径
    trash_path = os.path.expanduser('~/.Trash')
    
    # 确保废纸篓路径存在
    if not os.path.exists(trash_path):
        os.makedirs(trash_path)
    
    # 构造目标路径，避免文件名冲突
    base_name = os.path.basename(file_path)
    target_path = os.path.join(trash_path, base_name)
    
    # 如果目标路径已存在，修改文件名以避免冲突
    count = 1
    while os.path.exists(target_path):
        name, ext = os.path.splitext(base_name)
        target_path = os.path.join(trash_path, f"{name}_{count}{ext}")
        count += 1
    
    # 移动文件到废纸篓
    shutil.move(file_path, target_path)
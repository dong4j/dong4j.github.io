import re
import os
import sys
import shutil
import subprocess
from utils import find_all_image_tags, extract_image_url_from_tag, extract_image_urls_from_md, get_all_md_files, find_md_file, is_url

def log(message):
    """
    打印中文日志信息。
    """
    print(f"日志：{message}")

def upload_image(image_path):
    # 使用picgo命令上传图片，并获取输出
    result = subprocess.run(['picgo', 'upload', image_path], capture_output=True, text=True)
    # 提取图床地址，只匹配以https开头的字符串
    url_match = re.search(r'https://[^ ]+', result.stdout)
    if url_match:
        return url_match.group().strip()
    else:
        raise Exception(f"无法从输出中提取图床地址: {result.stdout}")

def replace_image_tags_in_md(md_file, base_dir, publish_dir):
    print(f"正在处理Markdown文件：{md_file}")
    # 计算Markdown文件相对于base_dir的路径
    relative_path = os.path.relpath(md_file, start=base_dir)
    # 构建发布目录下的Markdown文件路径
    publish_md_file = os.path.join(publish_dir, relative_path)
    # 确保发布目录下的子目录存在
    os.makedirs(os.path.dirname(publish_md_file), exist_ok=True)

    # 检查发布目录下的Markdown文件是否已存在
    if os.path.exists(publish_md_file):
        print(f"文件已存在：{publish_md_file}")
        return  # 文件存在，退出函数
    
    # 复制原始Markdown文件到发布目录
    shutil.copyfile(md_file, publish_md_file)

    # 读取发布目录下的Markdown文件内容
    with open(publish_md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取所有图片标签
    image_tags = find_all_image_tags(md_file)

    for tag in image_tags:
        # 从标签中提取图片文件名
        image_name = extract_image_url_from_tag(tag)
        # 如果 image_name 为空字符串，跳过当前循环
        if not image_name or is_url(image_name):
            print(f"标签 {tag} 中未找到有效的图片路径或者已经是图床地址，跳过。")
            continue

        if image_name.startswith('/images'):
            # 图片路径以 /images 开头，需要在 source/images 目录下查找
            source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source')
            image_path = os.path.join(source_dir, 'images', image_name[len('/images'):].lstrip('/'))
        else:
            # 图片路径不是以 /images 开头，直接在文章目录下查找
            image_path = os.path.join(os.path.splitext(md_file)[0] , image_name)

        # 检查图片文件是否存在
        if os.path.isfile(image_path):
            # 上传图片并获取图床地址
            image_url = upload_image(image_path)
            # 只替换括号()内的内容
            new_tag = re.sub(r'\(.*?\)', f'({image_url})', tag)
            content = content.replace(tag, new_tag)
            if image_name.startswith('/images'):
                log(f"替换 cover 图片地址")
                content = content.replace('cover: ' + image_name, 'cover: ' + image_url)
            log(f"替换标签 {tag} 为 {new_tag}")
        else:
            print(f"图片文件不存在: {image_path}")

    # 保存修改后的Markdown文件到发布目录
    with open(publish_md_file, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    # 构建发布目录路径，确保它在source/_posts下
    publish_dir = os.path.join(base_dir, 'publish')
    # 确保发布目录存在
    os.makedirs(publish_dir, exist_ok=True)
    log(f"博客文章的基准目录：{base_dir}")

    # 初始化要处理的Markdown文件列表
    md_files_to_process = []

    if not args:
        # 处理所有Markdown文件
        md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的Markdown文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
        else:
            log(f"年份目录 {args[0]} 不存在。")
            return
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename, exclude_dir='publish')
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到Markdown文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return

    # 循环处理所有确定的Markdown文件
    for md_file in md_files_to_process:
        replace_image_tags_in_md(md_file, base_dir, publish_dir)

    log("==================图片上传完成==================")

if __name__ == "__main__":
    main()

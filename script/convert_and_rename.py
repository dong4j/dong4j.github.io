import os
import re
import sys
import subprocess
import random
import string
from datetime import datetime
from utils import find_all_image_tags, extract_image_url_from_tag, extract_image_urls_from_md, get_all_md_files, find_md_file, is_url, log

SUPPORTED_IMAGE_FORMATS = {'.png', '.jpg', '.jpeg', '.bmp'}  # 添加更多支持的格式


def is_valid_filename(filename):
    """
    检查文件名是否已满足特定的命名规则。
    """
    naming_pattern = re.compile(r'^\d{14}_[a-zA-Z0-9]{8}\.webp$')
    return naming_pattern.match(filename) is not None

def generate_random_string(length=8):
    """
    生成指定长度的随机字符串。
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def convert_image_to_webp(image_path, quality=75):
    """
    使用ffmpeg将支持的图片格式转换为webp格式，如果图片已经是webp或不是支持的格式则跳过。
    """
    log(f"尝试转换图片 {image_path} 到webp格式")

    # 检查是否为URL或不是支持的图片格式
    if (is_url(image_path) or not os.path.splitext(image_path)[1].lower() in SUPPORTED_IMAGE_FORMATS):
        log(f"路径 {image_path} 是一个URL或不是支持的图片格式，跳过转换。")
        return image_path
    
    # 检查是否已存在同名的webp文件
    webp_path = os.path.splitext(image_path)[0] + '.webp'
    if os.path.exists(webp_path):
        log(f"同名webp文件已存在：{webp_path}，跳过转换。")
        return webp_path

    # 生成输出路径
    output_path = os.path.splitext(image_path)[0] + '.webp'

    # 构建并执行ffmpeg命令
    command = f"ffmpeg -i '{image_path}' -q:v {quality} '{output_path}' -loglevel quiet"
    subprocess.run(command, shell=True, check=True)  # 添加check=True以捕获错误

    log(f"图片 {image_path} 已转换为 {output_path}")
    return output_path

def rename_webp_file(webp_path, starts_with_images=False):
    """
    根据规则重命名webp文件，如果文件已存在则跳过。
    """
    # 检查文件是否为webp文件
    if not webp_path.lower().endswith('.webp'):
        log(f"文件 {webp_path} 不是webp文件，跳过重命名。")
        return os.path.basename(webp_path)
    
    
    # 检查文件名是否已满足规则
    if is_valid_filename(os.path.basename(webp_path)):
        log(f"文件 {webp_path} 名称已满足规则")
        if starts_with_images:
            return "/images/cover/" + os.path.basename(webp_path)   
        else:
            return os.path.basename(webp_path)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_string = generate_random_string()
    new_name = f"{timestamp}_{random_string}.webp"
    new_path = os.path.join(os.path.dirname(webp_path), new_name)
    if os.path.exists(new_path):
        log(f"文件 {new_path} 已存在，跳过重命名。")
        return os.path.basename(webp_path)
    os.rename(webp_path, new_path)
    if starts_with_images:
        # 图片路径以 /images 开头
        new_name = "/images/cover/" + new_name
    log(f"文件 {webp_path} 重命名为 {new_path}")
    return new_name

def update_md_image_tags(md_file, image_tag_map):
    """
    更新Markdown文件中的图片标签。
    """
    with open(md_file, 'r+', encoding='utf-8') as file:
        content = file.read()

        # 跳过不必要的替换
        updated = False
    
        for old_tag, new_tag in image_tag_map.items():
            print(f"正在处理图片标签：{old_tag} -> {new_tag}")
            if old_tag != new_tag and old_tag in content:
                content = content.replace(old_tag, new_tag)
                updated = True
                if '/images/cover/' in old_tag:
                    log(f"替换 cover 标签")
                    content = content.replace('cover: ' + extract_image_url_from_tag(old_tag), 'cover: ' + extract_image_url_from_tag(new_tag))

        # 只有在有更新时才写回文件
        if updated:
            file.seek(0)
            file.write(content)
            file.truncate()
        else:
            print(f"文件 {md_file} 中没有需要更新的图片标签。")

def get_referenced_images(md_file):
    """
    获取Markdown文件中引用的所有图片。
    """
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return extract_image_urls_from_md(content)


def process_md_file(md_file):
    """
    处理单个Markdown文件及其图片，避免重复处理。
    """
    log(f"正在处理 Markdown 文件：{md_file}")

    image_dir = os.path.splitext(md_file)[0]
    if not os.path.isdir(image_dir):
        log(f"未找到文件 {md_file} 对应的图片目录。")
        return

    image_tag_map = {}

    all_image_tags = find_all_image_tags(md_file)
    print(all_image_tags)

    for image_tag in all_image_tags:
        image_path = extract_image_url_from_tag(image_tag)
        if image_path.startswith('http'):
            log(f"已经是图床图片, 不需要转换 {image_path} ")
            continue  # Skip external images

        if image_path.startswith('/images'):
            # 图片路径以 /images 开头，需要在 source/images 目录下查找
            source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source')
            full_image_path = os.path.join(source_dir, 'images', image_path[len('/images'):].lstrip('/'))
        else:
            # 图片路径不是以 /images 开头，直接在文章目录下查找
            full_image_path = os.path.join(image_dir, image_path)
        
        if os.path.isfile(full_image_path):
            webp_path = convert_image_to_webp(full_image_path)
            # 检查 webp_path 是否为网络图片
            if not is_url(webp_path):
                new_name = rename_webp_file(webp_path, starts_with_images=True if image_path.startswith('/images') else False)
                new_tag = f"![{new_name}]({new_name})"
                image_tag_map[image_tag] = new_tag
            else:
                log(f"路径 {webp_path} 是一个URL，跳过重命名和标签替换。")

    if image_tag_map:
        update_md_image_tags(md_file, image_tag_map)

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    log(f"博客文章的基准目录：{base_dir}")

    # 初始化要处理的Markdown文件列表
    md_files_to_process = []

    if not args:
        # 处理所有Markdown文件
        md_files_to_process = get_all_md_files(base_dir)
    elif len(args) == 1 and args[0].isdigit():
         # 处理指定年份的Markdown文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(year_dir)
        else:
            log(f"年份目录 {args[0]} 不存在。")
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename)
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
        process_md_file(md_file)

    log("==================图片转换完成==================")
if __name__ == "__main__":
    main()


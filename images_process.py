import os
import re
import shutil
from PIL import Image
import io

# 递归遍历source目录下的所有.md文件
def find_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                yield os.path.join(root, file)

# 压缩图片并保持其格式
def compress_image(image_path, quality=85):
    # 支持的图片格式
    supported_formats = ('JPEG')
    
    # 需要排除的图片格式
    excluded_formats = ('GIF', 'SVG', 'PNG')
    
    # 获取图片格式
    _, ext = os.path.splitext(image_path)
    img_format = ext[1:].upper()  # 去掉点号并转换为大写

    # 将 'JPG' 映射到 'JPEG'
    if img_format == 'JPG':
        img_format = 'JPEG'

    # 如果图片格式是需要排除的格式之一，则给出提示并退出函数
    if img_format in excluded_formats:
        print(f"Cannot compress excluded image format: {img_format} for image {image_path}")
        return

    # 如果图片格式是支持的格式之一，则进行压缩
    if img_format in supported_formats:
        # 打开图片
        with Image.open(image_path) as img:
            # 压缩图片
            img.save(image_path, format=img_format, quality=quality)
    else:
        print(f"Unsupported image format: {img_format} for image {image_path}")

# 解析Markdown文件中的图片链接
def extract_image_links(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
        # 正则表达式匹配Markdown中的图片链接
        image_links = re.findall(r'!\[.*?\]\((.*?)\)', content)
    return image_links

# 检查图片链接是否存在，并压缩图片
def check_and_compress_image_links(md_file, image_links):
    dir_name = os.path.splitext(md_file)[0]
    processed_images_file = 'processed_images.txt'
    if os.path.exists(processed_images_file):
        with open(processed_images_file, 'r', encoding='utf-8') as file:
            processed_images = file.read().splitlines()
    else:
        processed_images = []

    for link in image_links:
        image_name = os.path.basename(link)
        image_path = os.path.join(dir_name, image_name)
        if image_path in processed_images:
            # print(f"图片已经被处理过: {md_file} -> {link}")
            continue
        if not os.path.isfile(image_path):
            print(f"图片不存在: {md_file} -> {link}")
        else:
            # 压缩图片
            compress_image(image_path)
            # 将图片路径写入记录文件
            with open(processed_images_file, 'a', encoding='utf-8') as file:
                file.write(image_path + '\n')

# 清理同名目录下未被引用的图片，并移动到 delete_source 目录下
def clean_unused_images(md_file, image_links, delete_directory):
    dir_name = os.path.splitext(md_file)[0]
    if os.path.isdir(dir_name):
        files_in_dir = set(os.listdir(dir_name))
        used_images = {os.path.basename(link) for link in image_links}
        # 找出未被引用的图片
        unused_images = files_in_dir - used_images
        for image in unused_images:
            image_path = os.path.join(dir_name, image)
            # 确定在 delete_directory 中的目标路径
            relative_path = os.path.relpath(dir_name, start='source')
            target_directory = os.path.join(delete_directory, relative_path)
            os.makedirs(target_directory, exist_ok=True)
            target_path = os.path.join(target_directory, image)
            # 移动文件
            print(f"移动未引用的图片: {image_path} -> {target_path}")
            shutil.move(image_path, target_path)

# 主函数
def main(source_directory, delete_directory):
    for md_file in find_md_files(source_directory):
        image_links = extract_image_links(md_file)
        if image_links:
            check_and_compress_image_links(md_file, image_links)
            clean_unused_images(md_file, image_links, delete_directory)

# 调用主函数
if __name__ == "__main__":
    source_directory = 'source'  # 假设source目录位于当前工作目录
    delete_directory = 'delete_source'  # 假设delete_source目录位于当前工作目录
    main(source_directory, delete_directory)

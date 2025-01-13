import re
import os
import sys
import shutil
import subprocess
from utils import find_all_image_tags, extract_image_url_from_tag, extract_image_desc_from_tag, find_image_tag_by_description, is_url, log, get_process_md_files

def upload_image(image_path):
    # 使用picgo命令上传图片，并获取输出
    result = subprocess.run(['picgo', 'upload', image_path], capture_output=True, text=True)
    # 提取图床地址，只匹配以https开头的字符串
    url_match = re.search(r'https://[^ ]+', result.stdout)
    if url_match:
        return url_match.group().strip()
    else:
        raise Exception(f"无法从输出中提取图床地址: {result.stdout}")

def copy_to_publish(md_file, base_dir, publish_dir):
    # 计算Markdown文件相对于base_dir的路径
    relative_path = os.path.relpath(md_file, start=base_dir)
    # 构建发布目录下的Markdown文件路径
    publish_md_file = os.path.join(publish_dir, relative_path)
    # 确保发布目录下的子目录存在
    os.makedirs(os.path.dirname(publish_md_file), exist_ok=True)

    # 检查发布目录下的Markdown文件是否已存在
    if os.path.exists(publish_md_file):
        # log(f"文件已存在：{publish_md_file}")
        return publish_md_file
    
    # 复制原始Markdown文件到发布目录
    shutil.copyfile(md_file, publish_md_file)
    return publish_md_file

def replace_image_tags_in_md(md_file, base_dir, publish_dir):
    # log(f"正在处理Markdown文件：{md_file}")

    publish_md_file = copy_to_publish(md_file, base_dir, publish_dir)
    # 读取发布目录下的Markdown文件内容
    with open(publish_md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取所有图片标签
    image_tags = find_all_image_tags(md_file)

    for tag in image_tags:
        
        # 在 publish 的对应文档中根据图片标签描述查找标签, 然后判断图片是否为图床地址:
        image_desc = extract_image_desc_from_tag(tag)
        publish_image_tag = find_image_tag_by_description(content, image_desc)
        # 如果 publish_image_tag 为空字符串或者图片已经上传到图床，跳过当前循环
        if not publish_image_tag or is_url(extract_image_url_from_tag(publish_image_tag)):
            continue

        # 从标签中提取图片文件名
        image_name = extract_image_url_from_tag(tag)
        if image_name.startswith('/images'):
            # 图片路径以 /images 开头，需要在 source/images 目录下查找
            source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source')
            image_path = os.path.join(source_dir, 'images', image_name[len('/images'):].lstrip('/'))
        elif image_name.startswith('./'):
            # 图片路径以 ./ 开头，需要在文章目录下查找
            image_path = os.path.join(os.path.splitext(md_file)[0], os.path.basename(image_name))
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
            log(f"图片文件不存在: {image_path}")

    # 保存修改后的Markdown文件到发布目录
    with open(publish_md_file, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 确保发布目录存在
    os.makedirs(dicts.get('publish_dir'), exist_ok=True)

    # 循环处理所有确定的 Markdown 文件
    for md_file in dicts.get('files'):
        replace_image_tags_in_md(md_file, dicts.get('base_dir'), dicts.get('publish_dir'))

    log("==================图片上传完成==================")

if __name__ == "__main__":
    main()

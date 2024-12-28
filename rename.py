"""
将 _drafts 和 _posts 目录下的 md 文件重命名:
1. 全部使用小写;
2. _ 改成 -;
3. 同步修改同名的资源目录;
4. 同步修改 cover;

比如 Desktop_collocation.md, 需要修改为 desktop-collocation.md, 且当前目录下同名的 Desktop_collocation 目录也需要修改为 desktop-collocation, 但是这个同名目录不一定存在;
最后还要对比 md 文件中的内容, 只需要读取前10 行, 找到 cover, 然后修改 cover 的值:
1. 如果在 cover 中找到匹配的目录名, 重命名规则同上;
2. 不要改动 md 中的其他内容;
"""

# 遍历 _drafts 和 _posts 目录下的所有 .md 文件
import os
import re

def to_snake_case(name):
    """转换为小写并将下划线转换为连字符"""
    return name.lower().replace("_", "-")

def scan_md_files(base_dirs):
    """扫描所有 .md 文件并记录原始路径和新路径"""
    md_files = []
    for base_dir in base_dirs:
        for dirpath, _, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.endswith(".md"):
                    md_file = os.path.join(dirpath, filename)
                    original_name = os.path.splitext(filename)[0]
                    new_name = to_snake_case(original_name)
                    md_files.append((md_file, original_name, new_name))
    return md_files

def update_cover_and_rename(md_file, original_name, new_name):
    """更新 .md 文件中 cover 字段，并重命名同名目录"""
    new_md_name = to_snake_case(os.path.basename(md_file))
    dir_path = os.path.dirname(md_file)
    new_md_path = os.path.join(dir_path, new_md_name)
    
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cover_pattern = re.compile(r"^(cover:\s*)(.+)$", re.IGNORECASE)
    updated = False

    for i, line in enumerate(lines[:10]):
        match = cover_pattern.match(line)
        if match:
            cover_path = match.group(2)
            if original_name in cover_path:
                new_cover_path = cover_path.replace(original_name, new_name)
                lines[i] = f"{match.group(1)}{new_cover_path}\n"
                updated = True
                print(f"修改 cover: {cover_path} -> {new_cover_path}")

    if updated:
        with open(md_file, "w", encoding="utf-8") as f:
            f.writelines(lines)
    
    # 重命名 .md 文件
    if md_file != new_md_path:
        os.rename(md_file, new_md_path)
        print(f"重命名文件: {md_file} -> {new_md_path}")

    # 重命名同名目录
    old_dir = os.path.join(dir_path, original_name)
    new_dir = os.path.join(dir_path, new_name)
    if os.path.isdir(old_dir) and old_dir != new_dir:
        os.rename(old_dir, new_dir)
        print(f"重命名目录: {old_dir} -> {new_dir}")

def process_all_files(base_dirs):
    """处理所有 .md 文件并更新 cover 字段和目录名"""
    md_files = scan_md_files(base_dirs)
    for md_file, original_name, new_name in md_files:
        if original_name != new_name:
            update_cover_and_rename(md_file, original_name, new_name)

if __name__ == "__main__":
    base_dirs = ["source/_drafts", "source/_posts"]
    #base_dirs = ["source/_drafts"]
    for base_dir in base_dirs:
        if os.path.isdir(base_dir):
            print(f"正在处理目录: {base_dir}")
            process_all_files(base_dirs)
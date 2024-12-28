#!/bin/bash

# 配置默认的图片质量
QUALITY=75
SOURCE_DIR="source/_posts"
IMAGE_SOURCE_DIR="./image_source"
LOG_FILE="./conversion.log"

# 检查参数
if [ $# -eq 0 ]; then
    TARGET_DIR="$SOURCE_DIR"
else
    TARGET_DIR="${SOURCE_DIR}/$1"
fi

# 检查目标目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory $TARGET_DIR does not exist."
    exit 1
fi

# 创建 image_source 目录（保留原目录结构）
mkdir -p "$IMAGE_SOURCE_DIR"

# 清空日志文件
> "$LOG_FILE"

# 遍历目标目录下所有 Markdown 文件和对应图片目录
find "$TARGET_DIR" -type f -name "*.md" | while read -r md_file; do
    # 获取 Markdown 文件所在的目录
    md_dir=$(dirname "$md_file")
    # 获取 Markdown 文件名（无后缀）
    md_basename=$(basename "$md_file" .md)
    # 图片目录与 Markdown 文件同名
    img_dir="$md_dir/$md_basename"

    # 如果图片目录存在
    if [ -d "$img_dir" ]; then
        # 遍历图片目录中的所有图片
        find "$img_dir" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | while read -r img_file; do
            # 获取图片的相对路径
            # 确保图片路径正确匹配
            if [[ "$img_file" == "$SOURCE_DIR"* ]]; then
                relative_img_path="${img_file#"$SOURCE_DIR/"}"
            else
                # 如果路径不以 SOURCE_DIR 开头，输出错误信息
                echo "Error: $img_file does not belong to $SOURCE_DIR" >> "$LOG_FILE"
                continue
            fi

            # 创建在 image_source 中的目录结构
            target_backup_dir="$IMAGE_SOURCE_DIR/${relative_img_path%/*}"
            mkdir -p "$target_backup_dir"

            # 移动原始图片到 image_source
            if mv "$img_file" "$target_backup_dir"; then
                # 获取图片文件名和扩展名
                img_name=$(basename "$img_file")
                img_name_no_ext=${img_name%.*}
                webp_file="$img_dir/$img_name_no_ext.webp"

                # 转换为 WebP 格式，并隐藏 ffmpeg 日志
                ffmpeg -i "$target_backup_dir/$img_name" -c:v libwebp -q:v $QUALITY "$webp_file" > /dev/null 2>&1

                # 输出并记录转换信息
                echo "Converting: image_source/$relative_img_path -> $webp_file"
                echo "image_source/$relative_img_path -> $webp_file" >> "$LOG_FILE"

                # 修改 Markdown 文件中的图片引用（处理重复的图片标签）
                sed -i "" -E "s|!\[.*\]\((.*${img_name})\)|![image_source/$relative_img_path](${img_name_no_ext}.webp)|g" "$md_file"
            else
                # 如果移动文件失败，输出错误信息
                echo "Error: Failed to move $img_file to $target_backup_dir"
            fi
        done
    fi
done

echo "Image conversion completed. Conversion log saved to $LOG_FILE."
#!/bin/bash

# 检查是否提供了一个目录参数
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# 输入目录
INPUT_DIR="$1"
# 输出目录
OUTPUT_DIR="${INPUT_DIR}_webp"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 函数：转换图片为webp
convert_to_webp() {
  local input_file="$1"
  local output_file="$2"
  ffmpeg -i "$input_file" "$output_file" &> /dev/null
  if [ $? -eq 0 ]; then
    echo "Converted: $input_file to$output_file"
  else
    echo "Failed to convert: $input_file"
  fi
}

# 递归遍历目录
export -f convert_to_webp
find "$INPUT_DIR" -type f \( -iname \*.jpg -o -iname \*.jpeg -o -iname \*.png  -o -iname \*.heic \) | while read -r file; do
  # 构建输出文件路径
  output_file="${OUTPUT_DIR}${file#$INPUT_DIR}"
  output_file="${output_file%.*}.webp"
  # 创建输出文件的目录结构
  mkdir -p "$(dirname "$output_file")"
  # 转换图片
  convert_to_webp "$file" "$output_file"
done

echo "Conversion completed."

#!/bin/bash

# 定义输入和输出目录
BASE_DIR=$(dirname "$0")  # 当前脚本所在目录
CSS_SOURCE_DIR="$BASE_DIR/../source/css"
MIN_CSS_DIR="$BASE_DIR/../source/min.css"

# 检查 csso-cli 是否已安装
if ! command -v csso &> /dev/null; then
  echo "csso-cli 未安装，请使用 'npm install -g csso-cli' 安装它。"
  exit 1
fi

# 创建输出目录
mkdir -p "$MIN_CSS_DIR"

# 遍历 css 目录中的所有 .css 文件
find "$CSS_SOURCE_DIR" -type f -name "*.css" | while read -r css_file; do
  # 计算输出文件的路径，保持目录结构
  relative_path="${css_file#$CSS_SOURCE_DIR/}"   # 去掉输入目录的前缀
  min_css_file="$MIN_CSS_DIR/$relative_path"

  # 创建输出文件的目录（如果不存在）
  mkdir -p "$(dirname "$min_css_file")"

  # 压缩 CSS 文件
  csso "$css_file" --output "$min_css_file"

  # 输出压缩的文件路径
  echo "压缩完成: $css_file -> $min_css_file"
done


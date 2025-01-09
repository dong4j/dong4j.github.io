#!/bin/bash

# 定义输入和输出目录
BASE_DIR=$(dirname "$0")  # 当前脚本所在目录
JS_SOURCE_DIR="$BASE_DIR/../source/js"
MIN_JS_DIR="$BASE_DIR/../source/min"

# 检查 terser 是否已安装
if ! command -v terser &> /dev/null; then
  echo "terser 未安装，请使用 'npm install -g terser' 安装它。"
  exit 1
fi

# 创建输出目录
mkdir -p "$MIN_JS_DIR"

# 遍历 js 目录中的所有 .js 文件
find "$JS_SOURCE_DIR" -type f -name "*.js" | while read -r js_file; do
  # 计算输出文件的路径，保持目录结构
  relative_path="${js_file#$JS_SOURCE_DIR/}"   # 去掉输入目录的前缀
  min_js_file="$MIN_JS_DIR/$relative_path"

  # 创建输出文件的目录（如果不存在）
  mkdir -p "$(dirname "$min_js_file")"

  # 压缩 JS 文件
  terser "$js_file" -o "$min_js_file" --compress --mangle

  # 输出压缩的文件路径
  echo "压缩完成: $js_file -> $min_js_file"
done

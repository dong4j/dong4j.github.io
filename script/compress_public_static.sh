#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")


# 检查是否安装 csso 和 terser
if ! command -v csso &>/dev/null; then
    echo "Error: csso is not installed. Install it using 'npm install -g csso-cli'."
    exit 1
fi

if ! command -v terser &>/dev/null; then
    echo "Error: terser is not installed. Install it using 'npm install -g terser'."
    exit 1
fi

# 获取目标目录，支持相对路径，默认为当前目录
TARGET_DIR=${1:-$SCRIPT_DIR/../public}

# 将相对路径转为绝对路径（确保 find 和工具能正确识别）
ABS_PATH=$(realpath "$TARGET_DIR")
if [ ! -d "$ABS_PATH" ]; then
    echo "Error: Directory $TARGET_DIR does not exist."
    exit 1
fi

# 搜索并压缩 .css 文件
find "$TARGET_DIR" -type f -name "*.css" | while read -r css_file; do
    csso "$css_file" --output "$css_file" --comments none && echo "✔ Compressed: $css_file"
done

# 搜索并压缩 .js 文件
find "$TARGET_DIR" -type f -name "*.js" | while read -r js_file; do
    terser "$js_file" --compress --mangle --output "$js_file" --comments false && echo "✔ Compressed: $js_file"
done

echo "Compression completed!"
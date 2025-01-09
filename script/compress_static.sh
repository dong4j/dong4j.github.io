#!/bin/bash

# 定义基础目录
BASEDIR=$(dirname "$0") # 当前脚本所在目录

# 定义源文件和压缩后文件的目录
JS_SOURCE_DIR="$BASEDIR/../source/js"
CSS_SOURCE_DIR="$BASEDIR/../source/css"
MIN_DIR="$BASEDIR/../source/min"

# 检查 terser 是否已安装
if ! command -v terser &> /dev/null; then
    echo "terser could not be found, please install it."
    exit 1
fi

# 检查 csso 是否已安装
if ! command -v csso &> /dev/null; then
    echo "csso could not be found, please install it."
    exit 1
fi

# 压缩文件函数
compressfile() {
    local file="$1"
    local output_dir="$2"
    local source_dir="$3"

    # 计算输出文件的路径，保持目录结构
    local relative_path="${file#$source_dir/}"
    local minfile="$output_dir/$relative_path"

    # 创建输出文件的目录（如果不存在）
    mkdir -p "$(dirname "$minfile")"

    # 检查压缩后的文件是否存在
    if [[ -f "$minfile" ]]; then
        # 获取源文件和压缩后文件的最后修改时间
        local source_mtime=$(stat -f %m "$file")
        local minfile_mtime=$(stat -f %m "$minfile")

        # 如果源文件没有改动，则跳过压缩
        if [[ "$source_mtime" -le "$minfile_mtime" ]]; then
            echo "文件未改动，无需压缩: $file"
            return
        fi
    fi

    # 根据文件类型压缩文件
    if [[ $file == *.js ]]; then
        terser "$file" --output "$minfile"
    elif [[ $file == *.css ]]; then
        csso "$file" --output "$minfile"
    else
        echo "Unsupported file type: $file"
        return
    fi

    # 输出压缩的文件路径
    echo "压缩完成: $file ->$minfile"
    
    # 将压缩后的文件名写入到 min_files.txt
    echo "$minfile" >> "$MIN_DIR/modify_files.txt"
}

# 压缩目录中的文件函数
compressfilesindir() {
    local source_dir="$1"
    local output_dir="$2"
    local extension="$3"

    # 查找并压缩所有匹配的文件
    find "$source_dir" -type f -name "*.$extension" -print0 | while IFS= read -r -d '' file; do
        compressfile "$file" "$output_dir" "$source_dir"
    done
}

# 压缩 JS 文件
compressfilesindir "$JS_SOURCE_DIR" "$MIN_DIR" "js"
# 压缩 CSS 文件
compressfilesindir "$CSS_SOURCE_DIR" "$MIN_DIR" "css"

echo "所有文件处理完成。"

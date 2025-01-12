#!/bin/bash

# 定义基础目录
BASEDIR=$(dirname "$0") # 当前脚本所在目录

FILE_PATH=${1:-$BASEDIR/../source/commit/index.md}

# 检查文件是否存在
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File $FILE_PATH does not exist."
    exit 1
fi

# 获取当前时间，格式为 YYYY-MM-DD HH:MM:SS
CURRENT_TIME=$(date "+%Y-%m-%d %H:%M:%S")

# 更新文件中的 `updated:` 字段
# 使用 sed 替换匹配的 `updated:` 行
sed -i '' -E "s/^(updated: ).*/\1$CURRENT_TIME/" "$FILE_PATH"

# 提示用户更新完成
echo "Updated 'updated:' field in $FILE_PATH to: $CURRENT_TIME"
#!/bin/bash

# 检查是否提供了目录参数和 configName 参数
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <directory> <configName>"
  exit 1
fi

# 指定的目录和 configName
DIRECTORY=$1
CONFIG_NAME=$2

# 后缀列表
EXTENSIONS=("css" "js" "webp")

# 检查目录是否存在
if [ ! -d "$DIRECTORY" ]; then
  echo "Directory '$DIRECTORY' does not exist."
  exit 1
fi

# 循环处理指定后缀的文件
for EXTENSION in "${EXTENSIONS[@]}"; do
  # 使用 find 命令递归查找所有匹配的文件
  find "$DIRECTORY" -type f -name "*.$EXTENSION" -print0 | while IFS= read -r -d '' FILE; do
    # 上传文件（静默模式 + 错误输出）
    curl -s -f --request POST \
      --url "http://127.0.0.1:36677/upload?picbed=tcyun&configName=${CONFIG_NAME}" \
      --header 'content-type: multipart/form-data' \
      --form file=@"$FILE" > /dev/null
    
    # 检查 curl命令的退出状态
    if [ $? -ne 0 ]; then
      echo "Failed to upload: $FILE"
    else
      echo "Successfully uploaded: $FILE"
    fi
  done
done

echo "All done."

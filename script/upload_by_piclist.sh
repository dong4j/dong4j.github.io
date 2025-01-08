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
EXTENSIONS=("css" "js")

# 检查目录是否存在
if [ ! -d "$DIRECTORY" ]; then
  echo "Directory '$DIRECTORY' does not exist."
  exit 1
fi

# 循环处理指定后缀的文件
for FILE in "$DIRECTORY"/*; do
  # 获取文件后缀
  EXTENSION="${FILE##*.}"
  
  # 检查文件后缀是否在列表中
  if [[ " ${EXTENSIONS[*]} " =~ "$EXTENSION " ]]; then
    # 上传文件（静默模式 + 错误输出）
    #  -s 参数，它会让 curl 进入静默模式，不输出响应的任何内容
    # -f 选项（即 fail silently 模式），这样当 HTTP 响应代码是 400 或更高时，curl 会返回错误状态，而不会输出响应内容
    curl -s -f --request POST \
      --url "http://127.0.0.1:36677/upload?picbed=tcyun&configName=${CONFIG_NAME}" \
      --header 'content-type: multipart/form-data' \
      --form file=@"$FILE" > /dev/null
    
    # 检查 curl命令的退出状态
    if [ $? -ne 0 ]; then
      echo "Failed to upload: $FILE"
    fi
  fi
done

echo "All done."
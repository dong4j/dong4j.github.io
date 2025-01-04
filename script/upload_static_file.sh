#!/bin/bash

# 检查是否提供了一个目录参数
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# 指定的目录
DIRECTORY=$1

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
    # 上传文件
    curl --request POST \
      --url 'http://127.0.0.1:36677/upload?picbed=tcyun&configName=COS-Blog-Static' \
      --header 'content-type: multipart/form-data' \
      --form file=@"$FILE"
    
    # 检查curl命令的退出状态
    if [ $? -eq 0 ]; then
      echo "Successfully uploaded: $FILE"
    else
      echo "Failed to upload: $FILE"
    fi
  fi
done

echo "All done."

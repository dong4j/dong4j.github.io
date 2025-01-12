#!/bin/bash

# 定义基础目录
BASEDIR=$(dirname "$0") # 当前脚本所在目录

# 检查是否提供了目录参数和 configName 参数
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <directory> <configName>"
  exit 1
fi

# 指定的目录和 configName
DIRECTORY="$BASEDIR/$1"
CONFIG_NAME=$2
MODIFY_FILES_TXT="$DIRECTORY/modify_files.txt"

# 后缀列表
EXTENSIONS=("css" "js" "webp")

# 检查目录是否存在
if [ ! -d "$DIRECTORY" ]; then
  echo "Directory '$DIRECTORY' does not exist."
  exit 1
fi

upload (){
  #上传文件（静默模式 + 错误输出）
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
}

# 检查 modify_files.txt 是否存在，并读取文件中的路径进行处理
if [ -f "$MODIFY_FILES_TXT" ]; then
  while IFS= read -r FILE; do
    upload $FILE ${CONFIG_NAME}
  done < "$MODIFY_FILES_TXT"
  # 清空 modify_files.txt 文件
  > "$MODIFY_FILES_TXT"
else
  # 循环处理指定后缀的文件
  for EXTENSION in "${EXTENSIONS[@]}"; do
    # 使用 find 命令递归查找所有匹配的文件
    find "$DIRECTORY" -type f -name "*.$EXTENSION" -print0 | while IFS= read -r -d '' FILE; do
      upload $FILE ${CONFIG_NAME}
    done
  done
fi

echo "All done."

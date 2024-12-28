#!/bin/bash

# 定义变量
REMOTE_HOST="m920x"
REMOTE_DIR="/opt/1panel/apps/openresty/openresty/www/sites/blog.dong4j.ink/index"
LOCAL_DIR="$(dirname "$0")/public" # 脚本同级目录下的 public

# 生成最新的文件
echo "正在执行 hexo clean && hexo g 以生成最新的文件..."
hexo clean && hexo recommend && hexo generate 

# 检查 public 目录是否生成成功
if [ ! -d "$LOCAL_DIR" ]; then
  echo "public 目录生成失败，请检查 Hexo 配置！"
  exit 1
fi

# 上传文件到远程并覆盖
echo "正在上传 public 目录下的所有文件到 $REMOTE_HOST:$REMOTE_DIR..."
rsync -ah --progress --delete \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '__MACOSX' \
  "$LOCAL_DIR/" "$REMOTE_HOST:$REMOTE_DIR" | tee /dev/null

# 检查上传是否成功
if [ $? -eq 0 ]; then
  echo "文件上传成功！"
else
  echo "文件上传失败，请检查连接或权限配置。"
  exit 1
fi

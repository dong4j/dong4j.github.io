#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")
# 切换到 Makefile 所在的工作目录 (即脚本所在目录的父目录)
cd "$SCRIPT_DIR/.." || exit 1

# 从参数获取 REMOTE_HOST 和 REMOTE_DIR
REMOTE_HOST="${1:-m920x}" # $1 如果未传递，则默认为 "m920x"
REMOTE_DIR="${2:-/opt/1panel/apps/openresty/openresty/www/sites/blog.dong4j.ink/index}" # $2 如果未传递，则使用默认值

# 定义本地目录
LOCAL_DIR="public" # 脚本同级目录下的 public

rm -rf $LOCAL_DIR

# 检查 public 目录是否存在
if [ ! -d "$LOCAL_DIR" ]; then
  echo "public 目录不存在，正在执行 hexo clean && hexo g 以生成最新的文件..."
  hexo clean && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

  # 再次检查 public 目录是否生成成功
  if [ ! -d "$LOCAL_DIR" ]; then
    echo "public 目录生成失败，请检查 Hexo 配置！"
    exit 1
  fi
fi

echo "压缩 css 和 js 文件..."
script/compress_public_static.sh 
echo "修改部署时间..."
script/deploy_update.sh

# 上传文件到远程并覆盖
echo "正在上传 public 目录下的所有文件到 $REMOTE_HOST:$REMOTE_DIR..."
rsync -azqhP --delete \
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
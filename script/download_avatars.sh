#!/bin/bash

# 检查是否提供了YAML文件路径
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path-to-yaml-file>"
    exit 1
fi

YAML_FILE="$1"

# 检查YAML文件是否存在
if [ ! -f "$YAML_FILE" ]; then
    echo "File not found: $YAML_FILE"
    exit 1
fi

# 创建一个目录来存储下载的avatars
avatars_dir="avatars_$(date +%s)"
mkdir -p "$avatars_dir"

# 读取YAML文件并提取avatar链接
while IFS= read -r line; do
    # 删除前后空格
    trimmed_line=$(echo "$line" | xargs)
    # 匹配以'avatar:'开头的行
    if [[ $trimmed_line == avatar:* ]]; then
        # 提取URL
        url=$(echo "$trimmed_line" | cut -d' ' -f2)
        # 替换URL的域名部分
        new_url=$(echo "$url" | sed 's|https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/|https://p.zhheo.com/|')
        # 添加!cover_240w后缀
        new_url="${new_url}!cover_240w"
        # 提取文件名
        filename=$(basename "$url")
        # 使用curl下载文件
        curl -s -o "$avatars_dir/$filename" "$new_url"
        echo "Downloaded $url to$avatars_dir/$filename"
        
        # 删除文件名中的 '!cover_mini' 后缀
        new_filename=$(echo "$filename" | sed 's/!cover_240w//')
        # 重命名文件
        mv "$avatars_dir/$filename" "$avatars_dir/$new_filename"
        echo "Renamed $filename to$new_filename"
    fi
done < "$YAML_FILE"

echo "All avatars have been downloaded and renamed in $avatars_dir"

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

# 创建一个目录来存储下载的siteshots
siteshots_dir="siteshots_$(date +%s)"
mkdir -p "$siteshots_dir"

# 读取YAML文件并提取siteshot链接
while IFS= read -r line; do
    # 删除前后空格
    trimmed_line=$(echo "$line" | xargs)
    # 匹配以'siteshot:'开头的行
    if [[ $trimmed_line == siteshot:* ]]; then
        # 提取URL
        url=$(echo "$trimmed_line" | cut -d' ' -f2)
        # 提取文件名
        filename=$(basename "$url")
        # 使用curl下载文件
        https://p.zhheo.com/UTc20Z21090481619315110835.png!cover_240w
        curl -s -o "$siteshots_dir/$filename" "$url"
        echo "Downloaded $url to$siteshots_dir/$filename"
        
        # 删除文件名中的 '!cover_mini' 后缀
        new_filename=$(echo "$filename" | sed 's/!cover_siteshot//')
        # 重命名文件
        mv "$siteshots_dir/$filename" "$siteshots_dir/$new_filename"
        echo "Renamed $filename to$new_filename"
    fi
done < "$YAML_FILE"

echo "All siteshots have been downloaded and renamed in $siteshots_dir"

import os
from PIL import Image

def convert_png_to_jpg(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                file_path = os.path.join(root, file)
                image = Image.open(file_path)
                jpg_file_path = os.path.splitext(file_path)[0] + '.jpg'
                image.save(jpg_file_path, 'JPEG')
                #os.remove(file_path)

# 使用示例
convert_png_to_jpg('source/_posts/2020/synology-nas')
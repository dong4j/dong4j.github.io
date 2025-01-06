import os
from PIL import Image
import sys
import subprocess

def compress_and_convert_image(input_dir, quality=20):
    """
    裁剪指定目录中的图片到1920x1080分辨率，然后使用FFmpeg转换为WebP格式并保存到另一个目录。
    输出目录为输入目录后加后缀"_compressed_webp"。

    :param input_dir: 输入目录路径
    :param quality: 压缩质量，范围从0到100
    """
    # 生成输出目录路径
    output_dir = f"{input_dir}_compressed_webp"
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_path = os.path.join(input_dir, filename)
            # 生成临时的压缩后的图片路径
            temp_output_path = os.path.join(output_dir, filename)

            # 打开图片
            with Image.open(input_path) as img:
                # 裁剪图片到1920x1080
                # img = crop_center(img, 1920, 1080)
                # 压缩图片
                img.save(temp_output_path, quality=quality)

            # 生成最终的WebP格式图片路径
            webp_output_path = os.path.splitext(temp_output_path)[0] + '.webp'

            # 使用FFmpeg将图片转换为WebP格式
            try:
                subprocess.run([
                    'ffmpeg',
                    '-i', temp_output_path,
                    '-c:v', 'libwebp',
                    '-q:v', '65',
                    webp_output_path
                ], check=True)
            except subprocess.CalledProcessError as e:
                print(f"FFmpeg error: {e}")
            finally:
                # 删除临时的压缩后的图片
                os.remove(temp_output_path)

def crop_center(image, new_width, new_height):
    """
    Crop the center of the image to the specified width and height.

    :param image: The input image to crop.
    :param new_width: The width of the new image.
    :param new_height: The height of the new image.
    :return: The cropped image.
    """
    width, height = image.size

    # Calculate the left, upper, right, and lower coordinates
    left = (width - new_width) / 2
    upper = (height - new_height) / 2
    right = (width + new_width) / 2
    lower = (height + new_height) / 2

    # Crop the center of the image
    cropped_image = image.crop((left, upper, right, lower))
    return cropped_image


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compress_and_convert_images.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]  # 从命令行参数获取输入目录路径
    compress_and_convert_image(input_directory)

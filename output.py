import os
import json

# 设定图片文件夹路径
folder_path = './photo'
output_file = './photo/imagelist.json'

# 支持的图片格式
valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

images = []

# 扫描文件夹
if os.path.exists(folder_path):
    for filename in os.listdir(folder_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in valid_extensions:
            images.append(filename)

# 写入 json 文件
with open(output_file, 'w') as f:
    json.dump(images, f)

print(f"成功! 已将 {len(images)} 张图片写入 {output_file}")
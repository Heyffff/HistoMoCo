import os
import shutil

# 源文件夹路径
source_folder = 'original/EBHI-SEG'
# 目标文件夹路径
destination_folder = 'pretrain/train/EBHI-SEG'

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历源文件夹中的所有文件
counter = 0
for root, dirs, files in os.walk(source_folder):
    if "image" not in root:
        continue
    for file in files:
        source_file = os.path.join(root, file)
        destination_file = os.path.join(destination_folder, str(counter) + ".png")
        shutil.copy(source_file, destination_file)
        counter += 1

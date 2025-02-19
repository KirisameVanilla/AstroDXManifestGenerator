import os
import json

"""
base_dir目录下应该有多个一级文件夹, 每个文件夹下有多个谱面文件夹。
即base_dir下应该有按照自己喜欢的分类方式放的谱面
生成manifest时, 每个manifest的名字是一级文件夹的名字
"""
# 一级文件夹的路径
base_dir = "D:/mai/"

for root, dirs, files in os.walk(base_dir):
    for dir_name in dirs:
        # 一级文件夹的路径
        first_level_dir = os.path.join(root, dir_name)

        # 二级文件夹的名字
        second_level_dirs = [
            d
            for d in os.listdir(first_level_dir)
            if os.path.isdir(os.path.join(first_level_dir, d))
        ]

        # 构造manifest.json
        manifest = {
            "name": dir_name,
            "id": None,
            "serverUrl": None,
            "levelIds": second_level_dirs,
        }

        # 创建以一级文件夹命名的文件夹
        output_dir = os.path.join(base_dir, "output", dir_name)
        os.makedirs(output_dir, exist_ok=True)

        # 写入manifest.json文件
        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=4)

    break  # 只遍历一级文件夹，不继续深入

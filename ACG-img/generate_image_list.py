import os
import json

image_folder = 'ACG-img/img/'
image_list = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

with open('ACG-img/image-list.json', 'w') as f:
    json.dump(image_list, f)

print(f"已生成包含 {len(image_list)} 张图片的列表。")
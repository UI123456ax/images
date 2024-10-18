from flask import Flask, send_file
import os
import random

app = Flask(__name__)

# 图片文件夹路径
IMG_FOLDER = os.path.join('ACG-img', 'img')

@app.route('/')
def random_image():
    # print(f"文件夹中的所有文件: {os.listdir(IMG_FOLDER)}")
    
    # 获取文件夹中所有图片文件
    images = [f for f in os.listdir(IMG_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # print(f"找到的图片文件: {images}")
    
    if not images:
        return "没有找到图片", 404
    
    # 随机选择一张图片
    random_image = random.choice(images)
    
    # 返回图片文件
    return send_file(os.path.join(IMG_FOLDER, random_image), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

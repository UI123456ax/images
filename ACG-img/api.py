import json
import random
from flask import Flask, jsonify, redirect

app = Flask(__name__)

def load_image_list():
    with open('image-list.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/random')
def random_image():
    image_list = load_image_list()
    if not image_list:
        return jsonify({"error": "No images found"}), 404
    
    random_image = random.choice(image_list)
    return redirect(f"https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/ACG-img/{random_image}")

if __name__ == '__main__':
    app.run(debug=True)

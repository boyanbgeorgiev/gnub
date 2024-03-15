from flask import Flask, request, jsonify
from flask import render_template
from api.scan import scan

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def scan_image():

    data = request.get_json()

    if 'image' not in data:
        return jsonify({'message': 'No image provided'}), 400

    image_data = data['image']

    if ";base64," in image_data:
        header, image_data = image_data.split(";base64,")
    else:
        return jsonify({'message': 'Invalid image format'}), 400

    result = scan(image_data)
    return jsonify({'message':result})
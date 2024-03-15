from flask import Flask, request, jsonify
from flask import render_template
import base64
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def scan_image():
   # Parse the JSON request
    data = request.get_json()

    # Check if image data is present
    if 'image' not in data:
        return jsonify({'message': 'No image provided'}), 400

    image_data = data['image']
    
    # Optional: Extract the content type and the base64 data
    if ";base64," in image_data:
        header, image_data = image_data.split(";base64,")
    else:
        return jsonify({'message': 'Invalid image format'}), 400

    # Decode the base64 string
    # Maybe we need this for the AI
    # image_bytes = base64.b64decode(image_data)
    
    # Respond back to the client
    return jsonify({'message': 'Image processed successfully'})
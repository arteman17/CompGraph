from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    operation = data['operation']

    image = cv2.imread('River.jpg', cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((3, 3), np.uint8)

    if operation == 'dilate':
        result = cv2.dilate(image, kernel, iterations=1)
    elif operation == 'erode':
        result = cv2.erode(image, kernel, iterations=1)
    elif operation == 'close':
        eroded_image = cv2.erode(image, kernel, iterations=1)
        result = cv2.dilate(eroded_image, kernel, iterations=1)
    elif operation == 'open':
        dilated_image = cv2.dilate(image, kernel, iterations=1)
        result = cv2.erode(dilated_image, kernel, iterations=1)

    _, buffer = cv2.imencode('.jpg', result)
    encoded_image = base64.b64encode(buffer).decode('utf-8')

    return encoded_image

if __name__ == '__main__':
    app.run(debug=True)
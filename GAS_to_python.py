from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/receive_image', methods=['POST'])
def receive_image():
    image_data = request.json['imageData']
    # Base64デコードして画像ファイルに保存などの処理を行う
    with open('received_image.png', 'wb') as f:
        f.write(base64.b64decode(image_data.split(',')[1]))
    return 'Image received successfully!'

if __name__ == '__main__':
    app.run(debug=True)

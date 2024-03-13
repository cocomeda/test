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


                   
                    url = "https://script.google.com/macros/s/AKfycbx0TTHh88dW9R3wwzISZWUcHiOHcS1p58obwi2dn6yIkkNHQ_3wzomPfjeqxYwGoWDgMQ/exec"

                    # JSON形式でデータを用意してdataに格納
                    data = {
                    "class": 'a',
                    "confidence": 'b',
                    "bounding_box" : 'b'
                    }
                    # json.dumpでデータをJSON形式として扱う
                    r = requests.post(url, data=json.dumps(data))



if __name__ == '__main__':
    app.run(debug=True)



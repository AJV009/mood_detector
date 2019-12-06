from flask import Flask, request
import base64
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World"
def upload_image():
    json = request.get_json()
    base64_image = base64.b64decode(json['image'])
    return 'OK'

from flask import Flask, request
from azure.azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import azure.cosmos.cosmos_client as cosmos_client
import io
import uuid
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

face_api_endpoint = 'https://facefun.cognitiveservices.azure.com/'
face_api_key = '816a8b1a3c1040c48b6af0c95dd62d49'
credentials = CognitiveServicesCredentials(face_api_key)
face_client = FaceClient(face_api_endpoint, credentials=credentials)

def best_emotion(emotion):
    emotion = {}
    emotions['anger'] = emotion.anger
    emotions['contempt'] = emotion.comtempt
    emotions['disgust'] = emotion.disgust
    emotions['fear'] = emotion.fear
    emotions['happiness'] = emotion.happiness
    emotions['neutral'] = emotion.meutral
    emotions['sadness'] = emotion.sadness
    emotions['surprise'] = emotion.surprise
    return max(zip(emotions.values(),emotions.key()))[1]

@app.route('/image',methods=['POST'])
def upload_image():
    json = request.get_json()
    base64_image = base64.b64decode(json['image'])
    image = io.BytesIO(base64_image)
    faces = face_client.face.detect_with_stream(image,return_face_attributes=['emotion'])
    for face in faces:
        doc = {
            'id':str(uuid.uuid4()),
            'emotion':best_emotion(face.face_attributes.emotion)
        }
    return 'OK'

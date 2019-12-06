import cv2
import requests
import base64
import json

def check_sadness(emotions):
    if 'sadness' in emotions:
        if emotions['sadness'] >= 3:
            print('Are you feeling okay? Do you want to talk about it?')

imageUrl = 'https://xaj-pyweb-app.azurewebsites.net/image'

def upload(frame):
    data = {}
    img = cv2.imencode('.jpg',frame)[1]
    data['image'] = base64.b64encode(img).decode()
    results = requests.post(url=imageUrl, json=data)
    check_sadness(results.json())

cam = cv2.VideoCapture(0)
cv2.namedWindow('Press space to take images!')

while True:
    ret, frame = cam.read()
    cv2.imshow('Press space to take a photo !',frame)
    key = cv2.waitKey(1)
    if key%256 == 32:
        upload(frame)
        break

cam.release()
cv2.destroyAllWindows()


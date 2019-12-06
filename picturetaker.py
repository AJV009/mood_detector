import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow('Press space to take images!')
while True:
    ret, frame = cam.read()
    cv2.imshow('Press space to take a photo',frame)
    key = cv2.waitKey(1)
    if key%256 == 32:
        break
cam.release()
cv2.destroyAllWindows()
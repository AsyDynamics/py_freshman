import numpy as np
import cv2

video = cv2.VideoCapture('video/test1.mp4')

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture('video/test1.mp4')
        continue

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('temp', gray)
    # cv2.waitKey(2000)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=5)


    if len(faces) is not 0:
        # print (type(faces))
        print(len(faces))
        print (faces)
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0), 3)
    # else:
        # print ("None faces detected")
    cv2.imshow('Frame', gray)
    key = cv2.waitKey(15)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()

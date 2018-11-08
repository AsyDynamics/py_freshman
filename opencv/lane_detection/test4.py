#!/home/asy/.virtualenvs/py3env1/bin/python3
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img,(0,0),(100,400),(255,120,56),5)
img = cv2.rectangle(img,(100,100),(400,300),(150,110,200),3)
img = cv2.circle(img, (447,63), 80, (250,250,0), -5)
img = cv2.ellipse(img, (256,256), (100,50), 20, 30, 360, 255, 5)
pts = np.array([[10,5],[20,30],[100,200],[200,300],[70,20],[50,10]],np.int32)
pts = pts.reshape(-1,1,2)
img = cv2.polylines(img, [pts], False, (0,255,0))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv test', (100,400), font, 2, (255,255,255), 2, cv2.LINE_AA)
cv2.imshow('create image',img)

cv2.waitKey(0)

#cv2.imwrite('cvline.jpg',img)

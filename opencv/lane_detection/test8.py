#!/home/asy/.virtualenvs/py3env1/bin/python3
import cv2
import numpy as np

img = cv2.imread('car1.jpg')
img2 =img
cv2.imshow('image1',img)
sticker = img[300:450, 300:700]
img2[50:200, 100:500] = sticker
cv2.imshow('image2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

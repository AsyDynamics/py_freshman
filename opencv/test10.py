import cv2
import numpy as np

img = cv2.imread('image_corner.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x,y), 5, (255,255,0), -1)

cv2.imshow('corner.jpg', img)

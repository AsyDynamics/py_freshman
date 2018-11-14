import cv2
import numpy as np

img = cv2.imread('letters.jpg')
ret, thresh1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)


# erosion = cv2.erode(img, kernel, iterations = 1)
# dilation = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow('original', img)
cv2.imshow('close', closing)
cv2.imshow('open', opening)

cv2.waitKey(0)
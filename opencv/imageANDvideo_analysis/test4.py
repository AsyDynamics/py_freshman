import numpy as np 
import cv2

img1 = cv2.imread('image_1.png')
img3 = cv2.imread('image_2.jpg')
img2 = cv2.imread('image_3.jpg')
#add = img1 + img2
#add = cv2.add(img1, img2)
#weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 160, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('mask', img1)

#cv2.imshow('frame', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
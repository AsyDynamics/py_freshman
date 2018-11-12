import numpy as np 
import cv2
img = cv2.imread('image_4.jpg')
retval, threshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 120, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

cv2.imshow('orign', threshold)
cv2.imshow('frame', threshold2)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
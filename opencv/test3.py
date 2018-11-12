import numpy as np
import cv2

img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
px = img[55,55]

img[55,55] = [0, 255, 0]
print(px)

img[100:150, 100:150] = [0,255,0]
watch_face = img[135:185, 300:350]

img[100:150, 100:150] = watch_face


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
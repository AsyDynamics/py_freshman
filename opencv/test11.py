import cv2
import numpy as np

img_name = 'picture/lane1.jpg'
img = cv2.imread(img_name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 700)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=250)
# print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)
# cv2.imshow('image', img)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

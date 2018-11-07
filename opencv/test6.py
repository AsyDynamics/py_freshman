#!/home/asy/.virtualenvs/py3env1/bin/python3
import cv2
import numpy as np
from random import randint as rand

drawing = False
mode = True
ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing  = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.rectangle(img, (ix,iy), (x,y), (rand(0,255),rand(0,255),rand(0,255)),3)
		else:
			cv2.circle(img, (ix,iy), 5, (0,0,255),3)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img, (ix,iy), (x,y), (rand(0,255),rand(0,255),rand(0,255)), 3)
		else:
			cv2.circle(img, (x,y), 10, (rand(0,255),rand(0,255),rand(0,255)), 3)

img = np.zeros((1024,1024,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
	cv2.imshow('imgae', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break
cv2.destroyAllWindows()

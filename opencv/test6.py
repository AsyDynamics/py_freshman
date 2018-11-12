
import numpy as np
import cv2

#img = cv2.imread('image_3.jpg')

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150,100,50])
	upper_red = np.array([180,255,100])
	#dark_red = np.uint([[[12,22,12]]])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(res, -1, kernel)

	blur = cv2.GaussianBlur(res, (15,15), 0)
	median = cv2.medianBlur(res, 15)
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)


	# cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	cv2.imshow('median', median)
	cv2.imshow('blur', blur)
	k = cv2.waitKey(25)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()

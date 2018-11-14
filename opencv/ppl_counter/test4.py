import cv2
import numpy as np

cap = cv2.VideoCapture('Budapest_Street.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print (fps)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
w = cap.get(3)
h = cap.get(4)
# for i in range(19):
	# print (i, cap.get(i))



# erosion = cv2.erode(img, kernel, iterations = 1)
# dilation = cv2.dilate(img, kernel, iterations = 1)

# cv2.imshow('original', img)


while True:
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)

	ret1, thresh1 = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
	kernel = np.ones((5,5), np.uint8)
	opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
	

	cv2.namedWindow('by subtracted', cv2.WINDOW_AUTOSIZE)
	cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
	cv2.namedWindow('close', cv2.WINDOW_AUTOSIZE)
	cv2.namedWindow('open', cv2.WINDOW_AUTOSIZE)
	
	cv2.imshow('bg subtracted', fgmask)
	cv2.imshow('original', frame)
	cv2.imshow('close', closing)
	cv2.imshow('open', opening)

	k = cv2.waitKey(33)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
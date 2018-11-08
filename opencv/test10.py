import cv2
import numpy as np
#import argparse
#import glob

def auto_canny(image, sigma=4):
        v = np.median(image)
        # lower = int(max(0,(1.0-sigma)*v))
        # upper = int((1.0+sigma)*v)
        # print ('value of v.median, lower and upper thres:')
        # print (v, lower, upper)
        lower = int(0.1*v)
        if v<20:
            upper = 100
        else:
            upper = int(sigma*v)
        edges = cv2.Canny(image, lower, upper)
        return edges, lower, upper, v

img = cv2.imread('lane8.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# lower = 50
# upper = 500
# edges = cv2.Canny(gray, lower, upper)
# cv2.HoughLines() # cpu usage high
# cv2.HoughLinesP()
sigma = 4
edges, lower, upper, v = auto_canny(img, sigma)

font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Median: ' + str(v) + ', Sigma: ' + str(sigma) +', threshould: ' + str(lower) + ', ' + str(upper)
# text = "Threshold: " + str(lower) + ", " + str(upper)
print (text)
cv2.putText(edges, text, (10,30), font, 1, (100,100,100), 2, cv2.LINE_AA)

cv2.imwrite('lane8-myauto0.jpg', edges)
# cv2.imshow("image", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

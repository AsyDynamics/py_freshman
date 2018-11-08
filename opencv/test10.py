import cv2
import numpy as np
#import argparse
#import glob

def auto_canny(image, sigma=0.33):
        v = np.median(image)
        lower = int(max(0,(1.0-sigma)*v))
        upper = int(min(255,(1.0+sigma)*v))
        print ('value of v.median, lower and upper thres:')
        print (v, lower, upper)
        edges = cv2.Canny(image, lower, upper)
        return edges, lower, upper, v

img = cv2.imread('lane1.jpeg')

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray, 100, 200)
# cv2.HoughLines() # cpu usage high
#cv2.HoughLinesP()
sigma = 0.6
edges, lower, upper, v = auto_canny(img, sigma)

font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Median: ' + str(v) + ', Sigma: ' + str(sigma) +', threshould: ' + str(lower) + ', ' + str(upper)
print (text)
cv2.putText(edges, text, (10,50), font, 1, (255,255,255), 1, cv2.LINE_AA)

cv2.imwrite('lane1-temp5.jpg', edges)
# cv2.imshow("image", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#!/home/asy/.virtualenvs/py3env1/bin/python3
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('car2.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

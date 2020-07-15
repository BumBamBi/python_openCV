import cv2

import numpy as np

img = cv2.imread('/home/lkw/Downloads/i.jpg')
img2 = img.astype(np.uint16)

b, g, r = cv2.split(img2)

gray1 = ((b+g+r)/3).astype(np.uint8)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('origin', img)
cv2.imshow('g1', gray1)
cv2.imshow('g2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()

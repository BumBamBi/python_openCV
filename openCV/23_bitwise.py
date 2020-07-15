import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('/home/lkw/Downloads/w.jpg')

mask = np.zeros_like(img)
cv2.circle(mask, (300, 300), 100, (255,255,255), -1)

# bit단위로 and시킴
# or, xor, not도 있음
# 여기선 위에서 만든 mask와 and 시킴
masked = cv2.bitwise_and(img, mask)

cv2.imshow('origin', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)

cv2.waitKey()
cv2.destroyAllWindows()

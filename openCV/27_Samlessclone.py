import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('/home/lkw/Downloads/c.png')
img2 = cv2.imread('/home/lkw/Downloads/w.jpg')

mask = np.full_like(img1, 255)

h, w = img2.shape[:2]
c = (w//2, h//2)

normal = cv2.seamlessClone(img1, img2, mask, c, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, c, cv2.MIXED_CLONE)

cv2.imshow('normal', normal)
cv2.imshow('mixed', mixed)

cv2.waitKey()
cv2.destroyAllWindows()
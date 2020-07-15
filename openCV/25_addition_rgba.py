import cv2
import numpy as np
import matplotlib.pylab as plt

imgb = cv2.imread('/home/lkw/Downloads/w.jpg')
imgf = cv2.imread('/home/lkw/Downloads/logo.png', cv2.IMREAD_UNCHANGED)

_, mask = cv2.threshold(imgf[:,:,3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

imgf = cv2.cvtColor(imgf, cv2.COLOR_BGRA2BGR)
h, w = imgf.shape[:2]
roi = imgb[10:10+h, 10:10+w]

maskedf = cv2.bitwise_and(imgf, imgf, mask=mask)
maskedb = cv2.bitwise_and(roi, roi, mask=mask_inv)

added = maskedf + maskedb
imgb[10:10+h, 10:10+w] = added


cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('maskedf', maskedf)
cv2.imshow('maskedb', maskedb)
cv2.imshow('added', added)
cv2.imshow('imgb', imgb)

cv2.waitKey()
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('/home/lkw/Downloads/w.jpg')
img2 = cv2.imread('/home/lkw/Downloads/w2.jpg')

img1_g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(img1_g, img2_g)

_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_red = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
diff_red[:,:,2] = 0

spot = cv2.bitwise_xor(img2, diff_red)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('spot', spot)

cv2.waitKey()
cv2.destroyAllWindows()

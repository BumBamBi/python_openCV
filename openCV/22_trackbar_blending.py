import cv2
import numpy as np
import matplotlib.pylab as plt

w_name = 'alpha_blending'
track_bar_name = 'fade'

def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(w_name, dst)


img1 = cv2.imread('/home/lkw/Downloads/w.jpg')
img2 = cv2.imread('/home/lkw/Downloads/ch.png')

cv2.imshow(w_name, img1)
cv2.createTrackbar(track_bar_name, w_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()

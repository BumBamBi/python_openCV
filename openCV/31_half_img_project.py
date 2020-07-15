import cv2
import numpy as np
import matplotlib.pylab as plt

# 두 사진을 자연스럽게 연결하기

img1 = cv2.imread('/home/lkw/Downloads/w1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/w2.jpg')
img = np.zeros_like(img1)

h = img1.shape[0]
w = img1.shape[1]
m = w//2

alpha_rate = 15
alpha_width = w * alpha_rate//100
start_alpha = m - alpha_width//2
end_alpha = m + alpha_width//2
step = 100//alpha_width

img[:, :m, :] = img1[:, :m, :].copy()
img[:, m:, :] = img2[:, m:, :].copy()
cv2.imshow('half', img)

for i in range(alpha_width+1):
    alpha = (100 - step*i)/100
    beta = 1-alpha
    img[:, start_alpha+i] = img1[:, start_alpha+i]*alpha + img2[:, start_alpha+i]*beta

    print(i, alpha, beta)

cv2.imshow('half_img', img)
cv2.waitKey()
cv2.destroyAllWindows()
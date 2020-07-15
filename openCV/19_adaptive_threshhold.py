import cv2

import numpy as np
import matplotlib.pylab as plt


# 주변 배경이 일정하지 않을 때(조명이나 배경색이 다름)는 하나의 값을 적용하기 힘들
# 따라서 일정 픽셀 주변만 이용하여 경계값을 정하는 adaptive threshhold(적응형 threshold)를 사용

blk_size = 9
C = 5

img = cv2.imread('/home/lkw/Downloads/i.jpg', cv2.IMREAD_GRAYSCALE)

# otsu의 알고리즘으로 단일 값으로 전체 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 적응형 threshhold를 평균과 가우시안 분포로 각각 적용
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

imgs = {'Origin': img, 'Global-Otsu = %d'%ret:th1, 'Adaptive_mean':th2, 'Adaptive_gaussian':th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v, 'gray')
    plt.xticks([]); plt.yticks([])

plt.show()
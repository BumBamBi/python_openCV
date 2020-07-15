import cv2
import numpy as np

file_path = '/home/lkw/Downloads/cube.png'
img = cv2.imread(file_path)

# edge를 검출하기 위해 직전 픽셀을 빼는 미분을 실행하면 됨
# 이 과정이 개선되고 다시 개선됨



# sobel Filter
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)

merged = np.hstack((img, sobelx, sobely, sobelx+sobely))
cv2.imshow('sobel', merged)
cv2.waitKey(0)

# Scharr Filter
# sobel의 단점을 개선한 필터
scharrx = cv2.Scharr(img, -1, 1, 0)
scharry = cv2.Scharr(img, -1, 0, 1)

merged = np.hstack((img, scharrx, scharry, scharrx+scharry))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)

# Laplacian Filter
# 미분결과를 다시 미분을 하여, 좀 더 정확안 edge를 검출 -> 대표적인 2차 미분 mask
# noise에 민감해서 Gaussian 필터로 noise를 제거한 후 사용하는 것이 좋다
edge = cv2.Laplacian(img, -1)

merged = np.hstack((img, edge))
cv2.imshow('Laplacian', merged)
cv2.waitKey(0)

# canny edge 적용
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

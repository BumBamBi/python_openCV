import cv2
import numpy as np

file_path = '/home/lkw/Downloads/cube.png'
img = cv2.imread(file_path)

# 평균 blurring
# 평균 blurring 의 두가지 방법
blur1 = cv2.blur(img, (10, 10))
blur2 = cv2.boxFilter(img, -1, (10, 10))

merged = np.hstack((img, blur1, blur2))
cv2.imshow('mean blur', merged)
cv2.waitKey(0)

# 가우시안 blurring -> 노이즈 제거 효과
blur3 = cv2.GaussianBlur(img, (3, 3), 0)
merged = np.hstack((img, blur3))
cv2.imshow('Gaussian blur', merged)
cv2.waitKey(0)

# 미디언 blurring
# 소금-후추 잡음제거에 효과적
blur4 = cv2.medianBlur(img, 5)
merged = np.hstack((img, blur4))
cv2.imshow('median blur', merged)
cv2.waitKey(0)

# 바이레터럴 필터
# 노이즈 제거와 경계검출을 둘 다 할 수 있도록 필터를 두개 사용함
blur5 = cv2.bilateralFilter(img, 5, 75, 75)
merged = np.hstack((img, blur5))
cv2.imshow('bilateral filter', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

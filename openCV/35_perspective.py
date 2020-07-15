import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[0:2]

# 원근변환
# 원근전환 전 후의 좌표 4개씩 값을 지정
postion1 = np.float32([[0, 0], [0, row], [col, 0], [col, row]])
postion2 = np.float32([[200, 50], [10, row-50], [col-200, 50], [col-0, row-50]])

# 변환 전 4개 좌표를 이미지에 표시해주기
cv2.circle(img, (0, 0), 5, (255, 0, 0), -1)
cv2.circle(img, (0, row), 5, (0, 255, 0), -1)
cv2.circle(img, (col, 0), 5, (0, 0, 255), -1)
cv2.circle(img, (col, row), 5, (0, 255, 255), -1)

# 원근변환에 쓰일 행렬을 함수를 통해 불러옴
matrix = cv2.getPerspectiveTransform(postion1, postion2)

# 원근변환 적용
dst = cv2.warpPerspective(img, matrix, (col, row))

# 출력
cv2.imshow('origin', img)
cv2.imshow('perspective', dst)
cv2.waitKey()
cv2.destroyAllWindows()

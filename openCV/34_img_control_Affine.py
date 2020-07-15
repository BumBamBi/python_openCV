import cv2
import numpy as np
from matplotlib import pyplot as plt

# 세개의 점을 찍어서 사진화면을 맘대로 컨트롤

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[0:2]

# 변환 전 후의 3개 좌표 생성
postion1 = np.float32([[100, 50], [200, 50], [100, 200]])
postion2 = np.float32([[80, 70], [210, 60], [250, 120]])

# 변환 전 3개 좌표를 이미지에 표시해주기
cv2.circle(img, (100, 50), 5, (255, 0, 0), -1)
cv2.circle(img, (200, 50), 5, (0, 255, 0), -1)
cv2.circle(img, (100, 200), 5, (0, 0, 255), -1)

# 어핀변환에 쓰일 행렬을 함수를 통해 불러옴
matrix = cv2.getAffineTransform(postion1, postion2)

# 어핀변한 적용
dst = cv2.warpAffine(img, matrix, (int(col*1.5), int(row)))

# 출력
cv2.imshow('origin', img)
cv2.imshow('affine', dst)
cv2.waitKey()
cv2.destroyAllWindows()

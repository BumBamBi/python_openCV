import cv2
import numpy as np

file_path = '/home/lkw/Downloads/cube.png'
img = cv2.imread(file_path)

# 침식/팽창 => 둘을 결합한 열림/닫힘

# 침식 Erode
# 작은 노이즈 제거 / 겹쳐져서 하나의 물체로 보일때 객체 분리
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
erosion = cv2.erode(img, k)

merged = np.hstack((img, erosion))
cv2.imshow('Erode', merged)
cv2.waitKey(0)

# 팽창 Dilation
# 침식과 반대로 사물을 주변까지 확장시켜서 보여줌
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dst = cv2.dilate(img, k)

merged = np.hstack((img, dst))
cv2.imshow('Dilation', merged)
cv2.waitKey(0)

# 위 두 연산은 물체가 작아지거나 뚱뚱해지는 단점이 있음
# 따라서 침식-팽창 / 팽창-침식을 해서 노이즈만 제거하는 방법

# 열림/닫힘
# 침식-팽창/팽창-침식

# kernel(5x5) 생성 후, 열림/닫힘 연산
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)

merged1 = np.hstack((img, opening))
merged2 = np.hstack((img, closing))
merged3 = np.vstack((merged1, merged2))
cv2.imshow('opening, closing', merged3)
cv2.waitKey(0)

# Gradient 연산으로 edge 검출
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)

# 결과 출력
merged = np.hstack((img, gradient))
cv2.imshow('gradient', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

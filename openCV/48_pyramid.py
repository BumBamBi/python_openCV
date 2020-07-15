import cv2
import numpy as np

file_path = '/home/lkw/Downloads/cube.png'
img = cv2.imread(file_path)

# 피라미드 -> 영상을 확대 축소해서 나열 해놓는것
# 이유 : 영상을 분석할 때 작은영상으로 미리 보는게 더 나음

# Gaussian 이미지 피라미드 축소/확대
smaller = cv2.pyrDown(img)          # img x 1/4
bigger = cv2.pyrUp(img)             # img x 4

cv2.imshow('img', img)
cv2.imshow('pyrDown', smaller)
cv2.imshow('pyrUp', bigger)
cv2.waitKey(0)


# Gaussian 학대시, 값이 흐려짐 따라서 다시 pyrUp/Down 함수를 이용해도 복원이 안됨
# 이런 문제점을 해결하기위해 '원본 - 확대영상' 의 차이를 저장한 후, 복원할 때 사용
# Laplacian 이미지 피라미드라고 함. (복원시 외엔 딱히 다를건 없음;)

# 원본 영상을 가우시안 피라미드로 축소한 후 다시 확대
smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(smaller)


# 원본에서 축소 후 다시 확대한 영상 빼기
# 여기선 축소후 확대한 이미지가 원본가 size가 달라서 안됨...
laplacian = cv2.subtract(img, bigger)

# 확대 한 영상에 라플라시안 영상 더해서 복원
restored = bigger + laplacian

# 결과 출력 (원본 영상, 라플라시안, 확대 영상, 복원 영상)
merged = np.hstack((img, laplacian, bigger, restored))
cv2.imshow('Laplacian Pyramid', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
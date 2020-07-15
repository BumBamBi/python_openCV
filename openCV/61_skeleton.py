import cv2
import numpy as np

# 이진화
img = cv2.imread('/home/lkw/Downloads/4star.jpg', cv2.IMREAD_GRAYSCALE)
_, biimg = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 도형 외곽으로 부터 거리 계산
dst = cv2.distanceTransform(biimg, cv2.DIST_L2, 5)
# 거리 값을 0 ~ 255 범위로 normalize
dst = (dst/(dst.max()-dst.min()) * 255).astype(np.uint8)
# threshold로 처리하여, 뼈대만 남김
skeleton = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, -3)

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('dist', dst)
cv2.imshow('skel', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()

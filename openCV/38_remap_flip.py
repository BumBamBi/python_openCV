import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

# remap을 이용 해서 flip

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
img2 = img.copy()
draw = img.copy()
row, col = img.shape[:2]

st2 = time.time()

# flip을 하기 위한 mtrix 생성
mapy, mapx = np.indices((row, col), dtype=np.float32)

# matrix에 flip을 위한 뒤집기 연산
mapx = col - mapx - 1
mapy = row - mapy - 1

# remap 함수로 flip하기
fliped2 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# 출력
cv2.imshow('origin', img)
cv2.imshow('fliped', fliped2)
cv2.waitKey()
cv2.destroyAllWindows()

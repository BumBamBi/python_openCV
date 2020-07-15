import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[0:2]
dx, dy = 100, 50


# 평행이동
# x' = x + dx
# y' = y + dy
# 따라서 평행이동시에는
# 1 0 dx
# 0 1 dy 행렬 이용
matrix_move = np.float32([[1, 0, dx], [0, 1, dy]])
move = cv2.warpAffine(img, matrix_move, (col+dx, row + dy))

# 확대/축소
# a 0 0
# 0 b 0 행렬 이용
# 2x2도 가능하지만, 평행이동과 함께 사용가능해서 2x3으로 사용
matrix_big = np.float32([[2, 0, 0], [0, 2, 0]])
matrix_small = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
big = cv2.warpAffine(img, matrix_big, (int(row*2), int(col*2)))
small = cv2.warpAffine(img, matrix_small, (int(row*0.5), int(col*0.5)))

# 이걸 쉽게 해주는 openCV 명령어가 있음 - (보간법 알고리즘 추가)
big_resize = cv2.resize(img, (int(row*2), int(col*2)), interpolation=cv2.INTER_AREA)
small_resize = cv2.resize(img, (int(row*0.5), int(col*0.5)), interpolation=cv2.INTER_CUBIC)

# 회전
# cos -sin 0
# sin  cos 0 을 사용하지만, 복잡함
# 따라서 주어진 함수 사용 + 확대/축소까지 한번에 가능
# 45도 회전 + 0.5배율
matrix_rotate = cv2.getRotationMatrix2D((col/2, row/2), 45, 0.5)
rotate = cv2.warpAffine(img, matrix_rotate, (col, row))

cv2.imshow('move', move)
cv2.imshow('big', big)
cv2.imshow('small', small)
cv2.imshow('big_resize', big_resize)
cv2.imshow('small_resize', small_resize)
cv2.imshow('rotate', rotate)
cv2.waitKey()
cv2.destroyAllWindows()
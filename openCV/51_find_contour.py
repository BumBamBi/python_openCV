import cv2
import numpy as np

file_path = '/home/lkw/Downloads/b.jpg'
img = cv2.imread(file_path)

# BGR2Gray
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold + _INV => 검은배경 흰색그림
ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)


# 바깥쪽 contour 반환 (현재버젼에선 img, img2값을 변화시키지 않음)
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 가장 외곽의 contour의 꼭짓점 반환
contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('도형의 갯수: %d(%d)'% (len(contour), len(contour2)))

# contour 그리기 (모든좌표/꼭짓점)
cv2.drawContours(img, contour, -1, (0, 255, 0), 4)
cv2.drawContours(img, contour2, -1, (0, 255, 0), 4)

# contour 를 점으로 표시 (모든좌표/꼭짓점)
for i in contour:
    for j in i:
        cv2.circle(img, tuple(j[0]), 1, (255, 0, 0), -1)

for i in contour2:
    for j in i:
        cv2.circle(img, tuple(j[0]), 1, (255,0,0), -1)


cv2.imshow('CHAIN_APPROX_NONE', img)
cv2.imshow('CHAIN_APPROX_SIMPLE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


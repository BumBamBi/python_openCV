import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/sudoku.jpg')
img2 = img.copy()
h, w = img.shape[:2]

# 허프 선 변환은 일일히 계산해서 느림
# 무작위로 허프변환을 진행하고 그 수를 점점 늘려가는 방식
# HoughLinesP() 함수로 구현 가능

# 그레이 스케일로 변환 및 엣지 검출 ---①
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 30, 150 )

# 확율 허프 변환 적용 ---②
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, None, 20, 2)
for line in lines:
    # 검출된 선 그리기 ---③
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1,y1), (x2, y2), (0,255,0), 1)

merged = np.hstack((img, img2))
cv2.imshow('Probability hough line', merged)
cv2.waitKey()
cv2.destroyAllWindows()
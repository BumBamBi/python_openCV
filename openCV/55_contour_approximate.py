import cv2
import numpy as np

file_path = '/home/lkw/Downloads/b.jpg'
img = cv2.imread(file_path)

# noise 때문에 너무 정확한 contour 를 찾는것 보다 조금 널널하게 찾는게 더 많이 쓰임.
# approxPolyDP() 함수를 이용해서 단순화 시킴

# 이진화
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

# 컨투어 찾기
contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[0]

# 전체 둘레의 5% 오차 범위 지정
epsilon = 0.05 * cv2.arcLength(contour, True)

# contour 단순화
approx = cv2.approxPolyDP(contour, epsilon, True)

# 각각 컨투어 선 그리기 ---④
cv2.drawContours(img, [contour], -1, (0,255,0), 3)
cv2.drawContours(img, [approx], -1, (0,255,0), 3)

# 결과 출력
cv2.imshow('approx', img)
cv2.waitKey()
cv2.destroyAllWindows()
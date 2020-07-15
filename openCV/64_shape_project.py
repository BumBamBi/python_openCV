import cv2
import numpy as np


img = cv2.imread("/home/lkw/Downloads/5shapes.jpg")
img2 = img.copy()

# 이진화
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# contour 찾기
contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # approxPolyDP 함수를 이용하여,contour 노이즈나 불필요 값들을 신경쓰지 않도록 근사 contour로 단순화시킴
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # 단순화된 contour의 꼭지점의 갯수를 구함
    vertices = len(approx)

    # 중심점 찾기
    mmt = cv2.moments(contour)
    cx, cy = int(mmt['m10'] / mmt['m00']), int(mmt['m01'] / mmt['m00'])

    name = "Unkown"
    if vertices == 3:  # 꼭지점이 3개는 삼각형
        name = "Triangle"
        color = (0, 255, 0)
    elif vertices == 4:  # 꼭지점 4개는 사각형
        x, y, w, h = cv2.boundingRect(contour)
        if abs(w - h) <= 3:  # 폭과 높이의 차이가 3보다 작으면 정사각형(오차 생각ㅇㅇ)
            name = 'Square'
            color = (0, 125, 255)
        else:  # 폭과 높이 차이가 3보다 크면 직사각형(혹은 직관전인 직사각형을 위해서)
            name = 'Rectangle'
            color = (0, 0, 255)
    elif vertices == 10:  # 꼭 지점 갯수 10개는 별
        name = 'Star'
        color = (255, 255, 0)
    elif vertices >= 15:  # 꼭 지점 10개 이상이면 원
        name = 'Circle'
        color = (0, 255, 255)
    # 컨투어 그리기
    cv2.drawContours(img2, [contour], -1, color, -1)
    # 도형 이름 출력
    cv2.putText(img2, name, (cx - 50, cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 100, 100), 1)

cv2.imshow('Input Shapes', img)
cv2.imshow('Recognizing Shapes', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
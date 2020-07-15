import cv2
import numpy as np

file_path = '/home/lkw/Downloads/b.jpg'
img = cv2.imread(file_path)

# 이진화
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# cv2.findContours()를 통해서 contour 찾기
contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 도형마다 contour moment 연산
for c in contours:

    # moments() 함수를 통한 moment 값 구하기
    mmt = cv2.moments(c)

    # 나누기 연산으로 중심점 계산
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    # 영역 넓이
    a = mmt['m00']

    # 영역 외곽선 길이
    l = cv2.arcLength(c, True)

    # 중심점에 노란색 점 그리기
    cv2.circle(img, (cx, cy), 5, (0, 255, 255), -1)

    # 중심점 근처에 넓이 그리기
    cv2.putText(img, "A:%.0f"%a, (cx, cy+20) , cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

    # 컨투어 시작점에 길이 그리기
    cv2.putText(img, "L:%.2f"%l, tuple(c[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))

    # 함수로 컨투어 넓이 계산해서 출력
    print("area:%.2f" %cv2.contourArea(c, False))

# 결과 출력
cv2.imshow('center', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/b.jpg')
img2 = img.copy()

# 한 물체 전체를 감싸는 contour 생성 -> 볼록선체(convexhull)
# convexHull() 함수로 생성 가능

# 이진화
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# contour 찾고 그리기
contours, heiarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntr = contours[0]
cv2.drawContours(img, [cntr], -1, (0, 255, 0), 1)

# 볼록 선체(물체 전체를 감싸는 contour) 찾기(좌표 기준)와 img2에 그리기
hull = cv2.convexHull(cntr)
cv2.drawContours(img2, [hull], -1, (0, 255, 0), 1)

# 볼록 선체인지 isContourConvex() 함수를 이용해서 확인
print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))


# 사실상 여기까지만 하면 완료지만, 가장 먼 곳의 좌표를 찍기 위해 다음과 같은 과정 수행


# 볼록 선체 찾기(인덱스 기준) ---⑤
hull2 = cv2.convexHull(cntr, returnPoints=False)
# 볼록 선체 결함 찾기 ---⑥
defects = cv2.convexityDefects(cntr, hull2)
# 볼록 선체 결함 순회
for i in range(defects.shape[0]):
    # 시작, 종료, 가장 먼 지점, 거리 ---⑦
    startP, endP, farthestP, distance = defects[i, 0]
    # 가장 먼 지점의 좌표 구하기 ---⑧
    farthest = tuple(cntr[farthestP][0])
    # 거리를 부동 소수점으로 변환 ---⑨
    dist = distance/256.0
    # 거리가 1보다 큰 경우 ---⑩
    if dist > 1 :
        # 빨강색 점 표시
        cv2.circle(img2, farthest, 3, (0,0,255), -1)

# 결과 이미지 표시
cv2.imshow('contour', img)
cv2.imshow('convex hull', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
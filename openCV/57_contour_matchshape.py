import cv2
import numpy as np

# 유사도 판단해서 비슷한 도형 찾기
# matchShapes() 함수로 유사도 검사

# 매칭을 위한 이미지 읽기
target = cv2.imread('/home/lkw/Downloads/4star.jpg') # 매칭 대상
shapes = cv2.imread('/home/lkw/Downloads/shapestomatch.jpg') # 여러 도형기

# 이진화
targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)

# contour 찾기
cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs_shapes, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어와 매칭 점수를 보관할 리스트 (낮을수로 닮음)
matchs = []

# 각 도형과 매칭을 위한 반복문
for contr in cntrs_shapes:
    # 유사도 확인해서 match에 저장
    match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
    # match에 contour 좌표도 함께 붙여서 저장
    matchs.append( (match, contr) )
    # 해당 도형의 컨투어 시작지점에 매칭 점수 표시
    cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255),1 )

# sorting
matchs.sort(key=lambda x : x[0])

# 가장 낮은 점수를 그림
cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)
cv2.imshow('target', target)
cv2.imshow('Match Shape', shapes)
cv2.waitKey()
cv2.destroyAllWindows()
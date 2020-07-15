
# opevCV가 지원하는 특징점 검출 알고리즘 중 하나
# 3. Blob
#
# 자잘자잘한건 noise로 판단, 큰 객체만 관심을 가지는 방식
# 인자값(필터 옵션)을 여러개 조정하여 원하는 모양으로 필터링 가능#

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blob 검출 필터의 Parameter 생성
# 이 값을 조정하여 Blob 검출의 방식? 을 다양하게 함
params = cv2.SimpleBlobDetector_Params()

# 경계값 조정
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5
# 면적 필터 켜고 최소 값 지정
params.filterByArea = True
params.minArea = 200
# 컬러, 볼록 비율, 원형비율 필터 옵션 끄기
params.filterByColor = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByCircularity = False

# 필터 파라미터로 blob 검출기 생성
detector = cv2.SimpleBlobDetector_create(params)
# 키 포인트 검출
keypoints = detector.detect(gray)
# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 결과 출력
cv2.imshow("Blob with Params", img_draw)
cv2.waitKey(0)

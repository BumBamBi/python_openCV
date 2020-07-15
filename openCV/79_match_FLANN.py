
# BF 매칭을 할 때, 이미지/영상이 너무 크면 속도가 느려지는데,이때 사용하는 FLANN
# 가장 가까운 이웃의 근사값으로 매#칭

import cv2, numpy as np

img1 = cv2.imread('/home/lkw/Downloads/taekwonv1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# SIFT 생성
detector = cv2.xfeatures2d.SIFT_create()
# 같은 방법으로 surf와 orb 방법도 사용가능
# detector2 = cv2.xfeatures2d.SURF_create()
# detector3 = cv2.xfeatures2d.ORB_create()

# 키 포인트와 서술자 추출
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

# 인덱스 파라미터와 검색 파라미터 값을 설정
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Flann macher 생성
matcher = cv2.FlannBasedMatcher(index_params, search_params)
# match 계산
matches = matcher.match(desc1, desc2)
# 선 그리기
res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('Flann + SIFT', res)
cv2.waitKey()
cv2.destroyAllWindows()

# bf나 flann 중 어떤 방법을 쓰던 쓸모없는 match가 너무 많음
# 좋은 매칭점만 남기는 작업이 필요하고, 작업후에 매칭점이 너무적으면 연관이 없는걸로 간주
# match(), knnMatch() 함수를 이용

import cv2, numpy as np

img1 = cv2.imread('/home/lkw/Downloads/taekwonv1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB로 서술자 추출
detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

# BF-Hamming으로 매칭
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(desc1, desc2)

# 매칭 결과를 거리기준 오름차순으로 정렬
matches = sorted(matches, key=lambda x:x.distance)

# 최소 거리 값과 최대 거리 값 확보
min_dist, max_dist = matches[0].distance, matches[-1].distance

# 최소 거리의 15% 지점을 임계점으로 설정
ratio = 0.2
good_thresh = (max_dist - min_dist) * ratio + min_dist

# 임계점 보다 작은 매칭점만 좋은 매칭점으로 분류
good_matches = [m for m in matches if m.distance < good_thresh]

# 좋은 매칭점만 그리기
res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# 결과 출력
cv2.imshow('Good Match_match', res)
cv2.waitKey()
cv2.destroyAllWindows()
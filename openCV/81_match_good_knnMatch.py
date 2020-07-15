
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

# BF-Hamming 생성
matcher = cv2.BFMatcher(cv2.NORM_HAMMING2)

# knnMatch, k=2
matches = matcher.knnMatch(desc1, desc2, 2)

# 첫번재 이웃의 거리가 두 번째 이웃 거리의 75% 이내인 것만 추출
ratio = 0.75
good_matches = [first for first,second in matches if first.distance < second.distance * ratio]
print('matches:%d/%d' %(len(good_matches),len(matches)))

# 좋은 매칭만 그리기
res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# 결과 출력
cv2.imshow('Matching', res)
cv2.waitKey()
cv2.destroyAllWindows()
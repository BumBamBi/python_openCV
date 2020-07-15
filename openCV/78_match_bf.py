
# 두 영상/이미지에서 구한 특징 키포인트들을 짝지어 놓는것

import cv2, numpy as np

img1 = cv2.imread('/home/lkw/Downloads/taekwonv1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# SIFT 서술자 추출기 생성
detector = cv2.xfeatures2d.SIFT_create()
# 같은 방식으로 surf, orb 방법으로 매칭 시킬 수 있다.
# detector2 = cv2.xfeatures2d.SURF_create()
# detector3 = cv2.xfeatures2d.ORB_create()

# 각 영상에 대해 키 포인트와 서술자 추출
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

# BFMatcher 생성, L1 거리, 상호 체크
matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
# 매칭 계산
matches = matcher.match(desc1, desc2)
# 매칭 결과 그리기
res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# 결과 출력
cv2.imshow('BFMatcher + SIFT', res)
cv2.waitKey()
cv2.destroyAllWindows()
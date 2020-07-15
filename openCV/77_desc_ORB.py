
# opevCV가 지원하는 특징점 검출 알고리즘 중 하나
# 6. ORB
#
# 특징 검출로는 FAST를 사용하고, BRIEF라는 알고리즘을 개선시킨 알고리즘
# FAST와 SURF의 대안으로 사용됨#

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ORB 추출기 생성
orb = cv2.ORB_create()
# 키 포인트 검출과 서술자 계산
keypoints, descriptor = orb.detectAndCompute(img, None)
# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 결과 출력
cv2.imshow('ORB', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()

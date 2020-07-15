
# opevCV가 지원하는 특징점 검출 알고리즘 중 하나
# 5. Surf
#
# 느린 Shif를 개선하여 필터의 커널 크기를 바꾸는 식으로 성능 개선
# 근데 안됨..ㅠ#

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SURF 추출기 생성 ( 경계:1000, 피라미드:3, 서술자확장:True, 방향적용:True)
surf = cv2.xfeatures2d.SURF_create(1000, 3, True, True)

# 키 포인트 검출 및 서술자 계산
keypoints, desc = surf.detectAndCompute(gray, None)
print(desc.shape, desc)
# 키포인트 이미지에 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SURF', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()

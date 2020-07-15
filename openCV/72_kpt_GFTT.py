
# opevCV가 지원하는 특징점 검출 알고리즘 중 하나
# 1. GFTTDetect
# #

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 특징 검출기 생성
gftt = cv2.GFTTDetector_create()
# 검출기로 특징 검출하여 키포인트 찾기
keypoints = gftt.detect(gray, None)
# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None)

# 결과 출력
cv2.imshow('GFTTDectector', img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
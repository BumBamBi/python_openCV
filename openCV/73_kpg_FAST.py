
# opevCV가 지원하는 특징점 검출 알고리즘 중 하나
# 2. FAST
#
# 미분연산이 아닌, 원을 통한 연산으로 속도가빠름#

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# FAST 특징 검출기 생성
fast = cv2.FastFeatureDetector_create(50)
# 특징 검출기를 이용하여 이미지의 키포인트 찾기
keypoints = fast.detect(gray, None)
# 키 포인트 그리기
img = cv2.drawKeypoints(img, keypoints, None)
# 결과 출력
cv2.imshow('FAST', img)
cv2.waitKey()
cv2.destroyAllWindows()
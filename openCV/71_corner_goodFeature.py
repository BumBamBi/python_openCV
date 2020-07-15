
# harris 를 개선한 알고리즘
# 객체추적에좋은 특징이 됨
# goodFeaturesToTrack()

import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/cube.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corner 검출 함수사용
corners = cv2.goodFeaturesToTrack(gray, 80, 0.01, 10)
# 실수 좌표를 정수 좌표로 변환
corners = np.int32(corners)

# 좌표에 동그라미 표시
for corner in corners:
    x, y = corner[0]
    cv2.circle(img, (x, y), 5, (0,0,255), 1, cv2.LINE_AA)

cv2.imshow('Corners', img)
cv2.waitKey()
cv2.destroyAllWindows()


# 이 함수르 통해 harris를 사용할 수도 있지만, 값이 실수값으로 나와서 int형으로 바꿔주어야함
# 사용법은 useHarrisDetector 인자에 True 대입
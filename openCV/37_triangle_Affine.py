import cv2
import numpy as np
from matplotlib import pyplot as plt

# 왠지 모르겠는데 안됨....

# 들로네 삼각분할
# 영역을 여러개의 삼각형으로 분할 시켜 놓은 것
# openCV는 사각형으로 처리하므로, 몇가지 과정을 거쳐야함

# 변환 전/후 삼각형 좌표 를 구함
# 변환 전 삼각형에 외접하는 사각형 좌표를 구함
# 이 사각형을 ROI로 지정
# ROI에서 변환 전-> 변환 후로 Affine 변환시킴
#

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
img2 = img.copy()
draw = img.copy()

# 변환 전/후 삼각형 좌표 구하기
pts1 = np.float32([[188, 14], [85, 202], [294, 216]])
pts2 = np.float32([[128, 40], [85, 307], [306, 167]])

# openCV의 함수를 이용해서 삼각형에 외접하는 사각형 좌표 구하기
x1, y1, w1, h1 = cv2.boundingRect(pts1)
x2, y2, w2, h2 = cv2.boundingRect(pts2)

# 사각형 좌표로 ROI 설정
roi1 = img[y1:y1+h1, x1:x1+w1]
roi2 = img[y2:y2+h2, x2:x2+w2]

# ROI 기준으로 좌표계산
offset1 = np.zeros((3, 2), dtype=np.float32)
offset2 = np.zeros((3, 2), dtype=np.float32)
for i in range(3):
    offset1[i][0], offset1[i][1] = pts1[i][0] - x1, pts1[i][1] - y1
    offset2[i][0], offset1[i][1] = pts1[i][0] - x2, pts2[i][1] - y2

# ROI에서 삼각형좌표를 Affine 변환 시킴
mtrx = cv2.getAffineTransform(offset1, offset2)
warped = cv2.warpAffine(roi1, mtrx, (w2, h2), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)

# 변환 후 삼각형만 골라내기 위한 mask 생성
mask = np.zeros((h2, w2), dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(offset2), 0)

# 삼각형 영역만 making 해서 합성
warped_masked = cv2.bitwise_and(warped, warped, mask=mask)
roi2_masked = cv2.bitwise_and(roi2, roi2, mask=cv2.bitwise_not(mask))
roi2_masked = roi2_masked + warped_masked
img2[y2:y2+h2, x2:x2+w2] = roi2_masked

# 삼각형 선과 함께 출력
cv2.rectangle(draw, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 1)
cv2.polylines(draw, [pts1.astype(np.int32)], True, (255, 0, 0), 1)
cv2.rectangle(img2, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 1)

cv2.imshow('origin', draw)
cv2.imshow('triangle', img2)
cv2.waitKey()
cv2.destroyAllWindows()

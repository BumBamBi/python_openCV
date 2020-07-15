import cv2
import numpy as np

# 볼록,오목 효과 주기
# 원효과는 직교좌표계, 극좌표계 중 극좌표계로 사용하는것이 편함
# 중점까지의 거리, 각도 두 값을 이용해서 위치 접근

img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[:2]

# 볼록/오목 지수
exp = 0.3
# 변환 영역 크기 0~1
scale = 1

# matrix 생성
mapy, mapx = np.indices((row, col), dtype=np.float32)

# 0드-1~1로 normalize (원점은 0이고,양/음수가 필요하므로)
mapx = 2*mapx/(col-1) -1
mapy = 2*mapy/(row-1) -1

# 직교좌표계를 극좌표계로 변환
r, theta = cv2.cartToPolar(mapx, mapy)

# 극 좌표계에서 r값 조정하여 왜곡(확대/축소)
r[r<scale] = r[r<scale]**exp

# 극좌표계를 다시 직교좌표계로 변환
mapx, mapy = cv2.polarToCart(r, theta)

# 극좌표계로 표현하기위해 normalize한걸 다시 돌려줌
mapx = ((mapx+1)*col-1)/2
mapy = ((mapy+1)*row-1)/2

# matrix 이용해서 remap 함수로 이미지 변형하기
trans = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# 출력
cv2.imshow('origin', img)
cv2.imshow('trans', trans)
cv2.waitKey()
cv2.destroyAllWindows()

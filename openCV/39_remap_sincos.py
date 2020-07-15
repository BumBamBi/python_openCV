import cv2
import numpy as np

# sin/cos 으로 사진을 remap 하기

# 파형을 위한 값들
l = 20      # 파장
amp = 15    # 진폭


img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[:2]


# matrix 생성
mapy, mapx = np.indices((row, col), dtype=np.float32)


# sin/cos 를 통한 변형 수식 연산
sinx = mapx + amp * np.sin(mapy/l)
cosy = mapy + amp * np.sin(mapx/l)

# matrix 이용해서 remap 함수로 이미지 변형하기
img_sinx = cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR)
img_cosy = cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR)
img_both = cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE)     # 외곽을 채우는 보정추가

# 출력
cv2.imshow('origin', img)
cv2.imshow('img_sinx', img_sinx)
cv2.imshow('img_cosy', img_cosy)
cv2.imshow('img_both', img_both)
cv2.waitKey()
cv2.destroyAllWindows()

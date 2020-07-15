import cv2
import numpy as np

# 방사왜곡 효과
# 둥근 렌즈로 사각형의 영상/이미지를 뽑아내며 생기는 왜곡..
# openCV는 이런 왜곡을 제거하기위해 undistort라는 함수 제공
# 이때, cameraMatrix값은 임의로 넣어야함(HW적 요소)


# 격자무늬 생성
img = np.full((300, 300, 3), 255, np.uint8)
img[::10, :, :] = 0
img[:, ::10, :] = 0

height, width = img.shape[:2]

# 왜곡 계수 값 설정
k1, k2, p1, p2 = 0.001, 0, 0, 0      # 배럴 왜곡 -
#k1, k2, p1, p2 = -0.0005, 0, 0, 0     # 핀쿠션 왜곡 -
distCoeff = np.float64([k1, k2, p1, p2])

# 임의값으로 cameraMatrix 설정
fx, fy = 10, 10
cx, cy = width/2, height/2
cameraMatrix = np.float32([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

# 왜곡 변형
dst = cv2.undistort(img, cameraMatrix, distCoeff)


# 출력
cv2.imshow('origin', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

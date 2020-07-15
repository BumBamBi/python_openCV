import cv2
import numpy as np

# 직교좌표를 극좌표로 바꿔서, 원의 선을 검출할 수 있다.

img = cv2.imread('/home/lkw/Downloads/coins_connected.jpg')


# BGR2GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 노이즈 제거를 위한 가우시안 블러
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# 허프 원 변환 적용
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 30, None, 300)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # 원 둘레에 초록색 원 그리기
        cv2.circle(img,(i[0], i[1]), i[2], (0, 255, 0), 2)
        # 원 중심점에 빨강색 원 그리기
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 5)

# 결과 출력
cv2.imshow('hough circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

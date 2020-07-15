import cv2
import numpy as np
from matplotlib import pyplot as plt

win_name = "scanning"
img = cv2.imread('/home/lkw/Downloads/w1.jpg')
row, col = img.shape[0:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)


def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스 좌클릭하면 초록 점으로 copy된 draw에 점을 찍음
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        # 해당 좌표 저장 및 4번 실행반복
        pts[pts_cnt] = [x, y]
        pts_cnt += 1

        if pts_cnt == 4:
            # 각 좌표의 상하좌우를 확인
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            # 변환전 4개좌표
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            # 변환 후 폭과 높이 계산
            w1 = abs(bottomLeft[0] + bottomRight[0])
            w2 = abs(topLeft[0] + topRight[0])
            h1 = abs(topRight[0] + bottomRight[0])
            h2 = abs(topLeft[0] + bottomLeft[0])

            width = max(w1, w2)
            height = max(h1, h2)

            # 변환 후 4개 좌표
            pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])

            # 행원근변환 행렬 함수를 통해 계산
            matrix = cv2.getPerspectiveTransform(pts1, pts2)

            # 원근 변환을 실행
            result = cv2.warpPerspective(img, matrix, (width, height))

            # 출력
            cv2.imshow('scanned', result)


cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey()
cv2.destroyAllWindows()



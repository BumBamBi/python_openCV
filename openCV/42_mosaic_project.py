import cv2
import numpy as np
from matplotlib import pyplot as plt경

# ROI를 설정하여 축소시켰다가, 다시 확대시킴
# 이때, 보간법을 이용하여 화질이 저화질로 변

win_title = 'mosaic'
img = cv2.imread('/home/lkw/Downloads/w1.jpg')
mosaic_rate = 15

while True:
    x, y, w, h = cv2.selectROI(win_title, img, False)
    if w and h:
        # 사진 축소
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (w//mosaic_rate, h//mosaic_rate))

        # 사진 확대
        roi = cv2.resize(roi, (w, h), interpolation = cv2.INTER_AREA)
        img[y:y + h, x:x + w] = roi
        cv2.imshow(win_title, img)
    else:
        break

cv2.destroyAllWindows()



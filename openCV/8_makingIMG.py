import cv2
import numpy as np

img = np.zeros((520, 520, 3), dtype=np.uint8)
# openCV 에서 이미지를 표현하기 위한 Numpy 배열은 항상 unit8이어야 함

img[25:35, :] = 45
img[55:65, :] = 115
img[85:95, :] = 160
img[:, 35:45] = 205
img[:, 75:85] = 255

img[125:135, :] = [255, 0, 0]
img[155:165, :] = [0, 255, 0]
img[185:195, :] = [0, 0, 255]
img[:, 260:280] = [255, 255, 0]
img[:, 300:320] = [255, 0, 255]
img[:, 500:520] = [0, 255, 255]

cv2.imshow('Colors', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



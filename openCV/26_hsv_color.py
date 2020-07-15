import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('/home/lkw/Downloads/cube.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# HSV 색상표에따른 값 설정
# 색조, 채도, 명도
b1 = np.array([90, 50, 50])
b2 = np.array([120, 255, 255])
g1 = np.array([30, 20, 20])
g2 = np.array([80, 255, 255])
r1 = np.array([0, 50, 50])
r2 = np.array([10, 255, 255])
r3 = np.array([170, 50, 50])
r4 = np.array([180, 255, 255])
y1 = np.array([20, 50, 50])
y2 = np.array([35, 255, 255])

maskb = cv2.inRange(hsv, b1, b2)
maskg = cv2.inRange(hsv, g1, g2)
maskr1 = cv2.inRange(hsv, r1, r2)
maskr2 = cv2.inRange(hsv, r3, r4)
masky = cv2.inRange(hsv, y1, y2)

resb = cv2.bitwise_and(img, img, mask=maskb)
resg = cv2.bitwise_and(img, img, mask=maskg)
resr1 = cv2.bitwise_and(img, img, mask=maskr1)
resr2 = cv2.bitwise_and(img, img, mask=maskr2)
resr = cv2.bitwise_or(resr1, resr2)
resy = cv2.bitwise_and(img, img, mask=masky)

imgs = {'origin':img, 'b':resb, 'g':resg, 'r':resr, 'y':resy}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]); plt.yticks([])

plt.show()
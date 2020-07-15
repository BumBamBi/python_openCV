import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('/home/lkw/Downloads/w1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/ch.png')

# 그냥 더해서 합치기
img3 = img1 + img2
# cv2.add 이용해서 합치기
img4 = cv2.add(img1, img2)
# alpha blending 이용해서 겹치기
img5 = cv2.addWeighted(img1, 0.5, img2, (1-0.5), 0)

imgs = {'img1':img1, 'img2':img2, 'img1+img2':img3, 'cv2.add':img4, 'alpha':img5}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]); plt.yticks([])

plt.show()
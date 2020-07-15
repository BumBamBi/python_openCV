import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('/home/lkw/Downloads/i.jpg', cv2.IMREAD_GRAYSCALE)

# 값 직접지정
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

# 오츠 알고리즘 선택
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu value : ', t)

# 다만 Otsu는 시간이 오래걸리고, noise가 심하면 완벽하지 않음
imgs = {'Origin': img, 't=130': t_130, 'otsu = %d' %t: t_otsu}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()

# 따라서 블러링 필터를 적용해야함
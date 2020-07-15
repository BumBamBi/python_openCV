import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = '/home/lkw/Downloads/i.jpg'
img = cv2.imread(img_path)

x = 400
y = 300
h = 150
w = 150

roi = img[y:y+h, x:x+w]
img2 = roi.copy()
img[y:y+h, x+w:x+w+w] = roi

cv2.rectangle(img, (x,y), (x+w+w, y+h), (255,0 ,255))

plt.imshow(img[:, :, ::-1])
plt.xticks([])
plt.yticks([])
plt.show()

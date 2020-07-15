import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = '/home/lkw/Downloads/i.jpg'

img = cv2.imread(img_path)

plt.imshow(img[:, :, ::-1])
plt.xticks([])
plt.yticks([])
plt.show()

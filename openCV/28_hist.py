import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('/home/lkw/Downloads/i.jpg')
cv2.imshow('img', img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

channels = cv2.split(img)
colors = {'b', 'g', 'r'}

for (ch, color) in zip (channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)

plt.show()

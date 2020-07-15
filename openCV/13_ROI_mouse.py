import numpy as np
import matplotlib.pyplot as plt
import cv2


isDrag = False
x0, y0, w, h = -1, -1, -1, -1
b = [255, 0, 0]
r = [0, 0, 255]


def onMouse(event, x, y, flags, param):
    global isDrag, x0, y0, w, h, img, img_path

    if event == cv2.EVENT_LBUTTONDOWN:
        isDrag = True
        x0 = x
        y0 = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDrag:
            roi = img.copy()
            cv2.rectangle(roi, (x0, y0), (x, y), b)
            cv2.imshow('img', roi)

    elif event == cv2.EVENT_LBUTTONUP:
        if isDrag:
            isDrag = False
            w = x - x0
            h = y - y0
            roi = img.copy()

            cv2.rectangle(roi, (x0, y0), (x, y), r, 2)
            cv2.imshow('img', roi)
            check_roi = img[y0:y0 + h, x0:x0 + w]
            cv2.imshow('cropped', check_roi)
            cv2.moveWindow('cropped', 0, 0)
            cv2.imwrite('croped.jpg', check_roi)
    else:
        cv2.imshow('img', img)
        print('pls check ROI')

w, h = 0, 0
check_roi = 0
img = cv2.imread('/home/lkw/Downloads/i.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

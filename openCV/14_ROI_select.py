import cv2
import numpy as np

img = cv2.imread('/home/lkw/Downloads/i.jpg')

x, y, w, h = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi)
    cv2.moveWindow('cropped', 0, 0)
    cv2.imwrite('./cropped2.jpg', roi)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# mask = np.zeros_like(img)
#                 x, y, w, h = cv2.selectROI('img', img, False)
#                 if w and h:
#                     cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)
#                     masked = cv2.bitwise_and(img, mask)
#                     cv2.imshow('cropped', masked)
#
#                 cv2.imshow('img', img)
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()#
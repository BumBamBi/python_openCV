import cv2

img = cv2.imread('/home/lkw/Downloads/logo.png')
bgr = cv2.imread('/home/lkw/Downloads/logo.png', cv2.IMREAD_COLOR)
bgra = cv2.imread('/home/lkw/Downloads/logo.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('bgrr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('allpha', bgra[:,:,3])
cv2.waitKey(0)
cv2.destroyAllWindows()
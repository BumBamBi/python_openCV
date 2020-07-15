import cv2

i = '/home/lkw/Downloads/i.jpg'

img = cv2.imread(i)

cv2.line(img, (50, 50), (150, 50), (55, 0, 0))
cv2.line(img, (200, 50), (300, 50), (0, 255, 0))
cv2.line(img, (350, 50), (450, 50), (0, 0, 255))


cv2.line(img, (100, 100), (400, 50), (55, 0, 0), 10)
cv2.line(img, (100, 150), (400, 50), (0, 255, 0), 10)
cv2.line(img, (100, 200), (400, 50), (0, 0, 255), 10)


cv2.line(img, (100, 50), (400, 50), (55, 0, 0), 20, cv2.LINE_4)
cv2.line(img, (100, 50), (400, 50), (0, 255, 0), 20, cv2.LINE_8)
cv2.line(img, (100, 50), (400, 100), (0, 0, 255), 20, cv2.LINE_AA)

cv2.putText(img, "test", (800, 50), cv2.FONT_ITALIC | cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 0))

cv2.imshow('lines.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img_path = '/home/lkw/Downloads/i.jpg'
img = cv2.imread(img_path)
title = 'track_bar'
cv2.imshow(title, img)

colors = {
    'k': (0, 0, 0),
    'r': (0, 0, 255),
    'b': (255, 0, 0),
    'g': (0, 255, 0)
}

def onChange(x):
    print(x)
    r = cv2.getTrackbarPos('R', title)
    g = cv2.getTrackbarPos('G', title)
    b = cv2.getTrackbarPos('B', title)
    print(r, g, b)
    img[:] = [b, g, r]
    cv2.imshow(title, img)


cv2.createTrackbar('R', title, 255, 255, onChange)
cv2.createTrackbar('G', title, 255, 255, onChange)
cv2.createTrackbar('B', title, 255, 255, onChange)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
import cv2

img_path = '/home/lkw/Downloads/i.jpg'
img = cv2.imread(img_path)
title = 'IMG'
x, y = 500, 500

cv2.imshow(title, img)

cv2.moveWindow(title, x, y)

while True:
    key = cv2.waitKey(0) & 0xFF

    print(key, chr(key))
    cv2.moveWindow(title, x, y)

    if key == ord('w'):
        y -= 1
    elif key == ord('s'):
        y += 1
    elif key == ord('a'):
        x -= 1
    elif key == ord('d'):
        x += 1
    elif key == ord('q'):
        break
        cv2.destroyAllWindows()

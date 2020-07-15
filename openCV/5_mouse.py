import cv2

img_path = '/home/lkw/Downloads/i.jpg'
img = cv2.imread(img_path)
title = 'mouse_event'
cv2.imshow(title, img)

colors = {
    'k': (0, 0, 0),
    'r': (0, 0, 255),
    'b': (255, 0, 0),
    'g': (0, 255, 0)
}

def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)
    color = colors['k']

    if event ==cv2.EVENT_LBUTTONDOWN:
        if (flags & cv2.EVENT_FLAG_CTRLKEY) and (flags & cv2.EVENT_FLAG_SHIFTKEY):
            # 두 버튼
            color = colors['g']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            # 하나
            color = colors['b']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            # 둘
            color = colors['r']

        cv2.circle(img, (x,y), 30, color, -1)
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
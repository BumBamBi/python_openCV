import cv2

v_file = "/home/lkw/Downloads/v.mp4"

cap = cv2.VideoCapture(v_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = int(1000/fps)

    while True:
        ret, img = cap.read()
        if ret:

            cv2.imshow(v_file, img)
            cv2.waitKey(fps)
        else:
            break
else:
    print('no video')

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pylab as plt

# 움직이는 모션 감지

thresh = 25
max_diff = 5
a, b, c = None, None, None

v_file = '/home/lkw/Downloads/v.mp4'
cap = cv2.VideoCapture(v_file)

fps = cap.get(cv2.CAP_PROP_FPS)
fps = int(1000 / fps)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)


if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()

    while ret:
        if not ret:
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break

        ret, c = cap.read()
        if ret:

            draw = c.copy()
            a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
            c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

            diff1 = cv2.absdiff(a_gray, b_gray)
            diff2 = cv2.absdiff(b_gray, c_gray)

            ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
            ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

            diff = cv2.bitwise_and(diff1_t, diff2_t)

            # 열림 연산(침식-팽창)으로 노이즈 제거
            k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

            diff_cnt = cv2.countNonZero(diff)
            if diff_cnt > max_diff:
                nzero = np.nonzero(diff)
                cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])), (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)
                cv2.putText(draw, "Motion Detected", (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

            stacked= np.hstack((draw, cv2.cvtColor(diff,cv2.COLOR_GRAY2BGR)))
            cv2.imshow('motion senseo', stacked)

            cv2.waitKey(fps)

            a = b
            b = c

cap.release()
cv2.destroyAllWindows()
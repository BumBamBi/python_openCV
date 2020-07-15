
# tracking
# 우선 객체가 아닌 배경을 제거해야함
# 이는 createBackfroundSubtractorMOG() 함수로 구할 수 있다.#

import cv2, numpy as np

#cap = cv2.VideoCapture('/home/lkw/Downloads/v.mp4')
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)
# 배경 제거 객체 생성 --- ①
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 배경 제거 마스크 계산 --- ②
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('bgsub',fgmask)
    if cv2.waitKey(1) & 0xff == 27:
        break
cap.release()
cv2.destroyAllWindows()
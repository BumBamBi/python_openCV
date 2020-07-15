import cv2


win_title = 'mosaic'    # 창 제목
file_path = '/home/lkw/Downloads/cube.png'
img = cv2.imread(file_path)    # 이미지 읽기

ksize = 30              # 블러 처리에 사용할 커널 크기

while True:
    # ROI 의 좌표 및 넓이 폭 구하기
    x, y, w, h = cv2.selectROI(win_title, img, False)
    if w > 0 and h > 0:
        # ROI 설정
        roi = img[y:y+h, x:x+w]
        # blur 적용
        roi = cv2.blur(roi, (ksize, ksize))
        # blur 적용된 ROI를 원본 이미지에 적용
        img[y:y+h, x:x+w] = roi
        cv2.imshow(win_title, img)
    else:
        break
cv2.destroyAllWindows()

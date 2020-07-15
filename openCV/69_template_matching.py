import cv2
import numpy as np

# 입력이미지와 템플릿 이미지 읽기
img = cv2.imread('/home/lkw/Downloads/figures.jpg')
template = cv2.imread('/home/lkw/Downloads/taekwonv1.jpg')
th, tw = template.shape[:2]
cv2.imshow('template', template)

# 3가지 매칭 방법을 돌아가면서 확인
methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']
for i, method_name in enumerate(methods):
    img_draw = img.copy()
    method = eval(method_name)
    # 선택한 매칭 방법으로 matchTemplate 실행하며, 매칭
    res = cv2.matchTemplate(img, template, method)
    # minMaxLoc 함수를 이용하여, 배열 전체에서의 최/소값과 그 좌표 구하기
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # TM_SQDIFF의 경우 값이 작아야 좋은 매칭, 나머지는 그 반대임
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    # 매칭된 좌표를 구하여 사각형 그리기
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0,0,255),2)
    # 매칭 포인트 표시
    cv2.putText(img_draw, str(match_val), top_left, cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0), 1, cv2.LINE_AA)
    cv2.imshow(method_name, img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()

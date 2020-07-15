import cv2
import numpy as np

# 스케치 효과를 주기 위해서 할 일
# Gaussian Blur 로 노이즈를 없앤 후, Laplacian 함수를 실행해서 edge를 검출한다.
# Threshold 함수를 이용해서, edge가 아닌건 삭제

# 물감 효과를 주기 위해서 할 일
# 경계선을 강조하기 위해 erode(침식) 연산을 하고
# 평균 blur 를 적용한 후, 해당 영상 두개 bitwise_and 연산을 한다.


file_path = '/home/lkw/Downloads/v.mp4'
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 프레임 읽기
    ret, frame = cap.read()
    # 속도 향상을 위해 영상크기를 절반으로 축소
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    if cv2.waitKey(1) == 27:
        break

    if ret:
        # 스케치 효과주기
        # edge를 검출하기 위해 gray_scale 로 변경
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Laplacian을 적용하기 전, noise를 제거하기위해 Gaussian Blur 적용
        img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)
        # Laplacian으로 edge 검출
        edges = cv2.Laplacian(img_gray, -1, None, 5)
        # threshold에 임의 값을 넣어서, 경계선 edge 만 남기고 제거함 (+화면 반전효과를 주기)
        ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

        # 물감 효과주기
        # 경계선 강조를 위해 erode(침식) 연산
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        sketch = cv2.erode(sketch, kernel)
        # edge를 자연스럽게 하기 위해 median blur 적용
        sketch = cv2.medianBlur(sketch, 5)
        # 그레이 스케일에서 BGR 컬러 스케일로 변경
        img_sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
        # 컬러 이미지 선명선을 없애기 위해 평균 블러 필터 적용
        img_paint = cv2.blur(frame, (10, 10))
        # 컬러 영상과 스케치 영상과 합성
        img_paint = cv2.bitwise_and(img_paint, img_paint, mask=sketch)

        # 결과 출력
        merged = np.hstack((img_sketch, img_paint))
        cv2.imshow('Sketch Camera', merged)
    else:
        break

cap.release()
cv2.destroyAllWindows()

# 스케치효과는 edge를 검출하기 전, noise를 제거하기위해 GaussianBlur를 사용함
# 그후 Laplacian으로 edge를 검출해낸다.
# Threshold함수에 인자값을 조정하여 edge 외엔 검은색으로 표현 되도록 함
# 그 후 _INV를 통해 edge가 검은색/배경 흰색 으로 만들어서 스케치 효과 완성

# 물감 효과는 edge를 강하게 만든 후 검출해내서 이를 mask로 사용함
# 해당 edge는 보이지 않도록 해서 검은 선 효과를 나타내줌
# blur시킨 영상 두개를 bitwise_and연산하여 물감처럼 느껴지도록 함
# mask를 통한 검은 선과, 물감의 질감이 합쳐져서 물감효과 완성

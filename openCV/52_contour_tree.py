import cv2
import numpy as np

file_path = '/home/lkw/Downloads/b.jpg'
img = cv2.imread(file_path)

# BGR2GRAY + threshold + _INV = 이진화
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 가장 외곽의 contour 반환 후 확인
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contour), hierarchy)

# 모든 contour를 tree 계층으로 반환 후 확인
contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contour2), hierarchy)

# 가장 외곽의 contour 그리기
cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

# 모든 contour 그리기 (tree 계층 사용)
for idx, cont in enumerate(contour2):
    # 랜덤 숫자로 contour 그리기
    color = [int(i) for i in np.random.randint(0,255, 3)]
    cv2.drawContours(img, contour2, idx, color, 3)

    # contour 처음 그릴 때 index 표시
    cv2.putText(img, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255))


cv2.imshow('RETR_EXTERNAL', img)
cv2.imshow('RETR_TREE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
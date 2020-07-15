
# good 및 knnMatch를 이용하여 좋은 매칭점 좌표를구했을때, 원근에 맞지 않다면 이를 맞춰주는 것
# 원근 변환 행렬을 근사값으로 찾아주는 함수 findHomography()
# 원래좌표를 원근변화해주는 함수 perspctiveTransform()

import cv2, numpy as np

img1 = cv2.imread('/home/lkw/Downloads/taekwonv1.jpg')
img2 = cv2.imread('/home/lkw/Downloads/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB, BF-Hamming 로 knnMatch
detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)
matcher = cv2.BFMatcher(cv2.NORM_HAMMING2)
matches = matcher.knnMatch(desc1, desc2, 2)

# 이웃 거리의 75%로 좋은 매칭점 추출
ratio = 0.75
good_matches = [first for first,second in matches if first.distance < second.distance * ratio]
print('good matches:%d/%d' %(len(good_matches),len(matches)))

# 좋은 매칭점의 queryIdx로 원본 영상의 좌표 구하기
src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ])
# 좋은 매칭점의 trainIdx로 대상 영상의 좌표 구하기
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ])

# findHomography() 함수로 원근 변환 행렬 구하기
mtrx, mask = cv2.findHomography(src_pts, dst_pts)

# 원본 영상 크기로 변환 영역 좌표 생성
h,w, = img1.shape[:2]
pts = np.float32([ [[0,0]],[[0,h-1]],[[w-1,h-1]],[[w-1,0]] ])

# perspectiveTransform() 함수로 원본 영상 좌표를 원근 변환시킴
dst = cv2.perspectiveTransform(pts,mtrx)

# 변환 좌표 영역을 대상 영상에 그리기
img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

# 좋은 매칭 그려서 출력
res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('Matching Homography', res)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2

# 사진을 8x8로 변경하고 0과 1로 변환시키

#영상 읽어서 그레이 스케일로 변환
img = cv2.imread('/home/lkw/Downloads/4star.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 8x8 크기로 축소기
gray = cv2.resize(gray, (16, 16))
# 영상의 평균값 구하기
avg = gray.mean()
# 평균값을 기준으로 0과 1로 변환 ---③
bin = 1 * (gray > avg)
print(bin)

# 2진수 문자열을 16진수 문자열로 변환 ---④
dhash = []
for row in bin.tolist():
    s = ''.join([str(i) for i in row])
    dhash.append('%02x'%(int(s,2)))
dhash = ''.join(dhash)
print(dhash)

cv2.namedWindow('star', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('star', img)
cv2.waitKey(0)

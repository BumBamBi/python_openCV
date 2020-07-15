import cv2
import numpy as np
import matplotlib.pylab as plt

# 노말라이징 하기위해서, 이진화하여 진행

img = cv2.imread('/home/lkw/Downloads/smog.jpg', cv2.IMREAD_GRAYSCALE)

img_n = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

#hist_n = cv2.calcHist([img_n], [0], None, [256], [0, 256])

imgs = {'origin':img, 'normalize':img_n}

cv2.imshow('ori', img)
cv2.imshow('n', img_n)

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()

# 잘 안되네ㅣ..
# 이퀄라이즈는 명암조절임
# 따라서 BGR보다는, 명암만 따로 값조절이 가능한, HSV나 YUV를 씀
# img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)        BGR->YUV 변환용
# img_yuv[:,:,0] = cv2.equalizedHit(img_yuv[:,:,0])     이퀄라이즈 실행
# img2 = cv2.cvtCOLOR(img_yuv, cv2.COLOR_YUV2BGR)       YUV->BGR 변환

# 너무 강한 명도일 때 값이날라가는 현상을 방지하기위해 CLAHE를 적용  
# clahe = cv2.createCLAHE(clipLimit=3,0, tileGridSize=(8,8) clahe생성
# img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])          clahe적
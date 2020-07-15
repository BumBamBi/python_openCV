# 랜덤수를 생성해서 임의의 두 값을 랜덤하게골라서 두 값의 중간값으로 값을 구분
# 모든 값의 중간값이 구해질 때까지 이 과정을 반복하여 두 그룹으로 나움

import numpy as np, cv2
import matplotlib.pyplot as plt

# 0~150 임의의 2수, 25개
a = np.random.randint(0,150,(25,2))
# 128~255 임의의 2수, 25개
b = np.random.randint(128, 255,(25,2))
# a, b를 병합
data = np.vstack((a,b)).astype(np.float32)

# 중지 요건
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 평균 클러스터링 적용
ret,label,center=cv2.kmeans(data,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# label에 따라 결과 분류
red = data[label.ravel()==0]
blue = data[label.ravel()==1]

# plot에 결과 출력
plt.scatter(red[:,0],red[:,1], c='r')
plt.scatter(blue[:,0],blue[:,1], c='b')

# 각 그룹의 중앙점 출력
plt.scatter(center[0,0],center[0,1], s=100, c='r', marker='s')
plt.scatter(center[1,0],center[1,1], s=100, c='b', marker='s')
plt.show()
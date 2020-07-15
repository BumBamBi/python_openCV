import cv2
import numpy as np
import matplotlib.pylab as plt


# 이미지 연사을 할 때, numpy를 이용해도 되지만, 0~255값을 정해주기 위해, cv2.연산을 사용#

a = np.uint8([[200, 50]])
b = np.uint8([[100, 100]])

add1 = a + b
add2 = cv2.add(a, b)

print(add1, add2)

# 그냥 뎃셈은 255를 통과하면, 초과되어 나옴 -> 오버플로 일어나는듯


# mask와 누적하랑 이용
aa = np.array([[1, 2]], dtype=np.uint8)
bb = np.array([[10, 20]], dtype=np.uint8)
mask = np.array([[2, 0]], dtype=np.uint8)

c1 = cv2.add(aa, bb, None, mask)
c2 = cv2.add(aa, bb, bb, mask)
print(c1, c2)

# c1은 mask가 1, 0 이므로, [1, 0] + [10, 0]을 해서 [11, 0] 임
# c2는 누적할당을 사용하므로, mask가 0이면 계산을 안하는걸로 생각하여,
# [1, x] + [10, x]을 해서 [11, x] 이므로, 계산된 11은 대입하고, x는 기존값 유지 -> [11, 20]
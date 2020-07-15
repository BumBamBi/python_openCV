import numpy as np

import matplotlib.pyplot as plt

a = np.array([2, 6, 7, 3, 12, 8, 4, 5])
plt.plot(a)
plt.show()

x = np.arange(100)
y = x**2 # power()와 동일

plt.plot(x, y)
plt.show()

# 그래프 색상기호
# b g r c(청록) m(자홍) y k w
# matlab처럼 --, --., o, ^, >, 1, 2, 3, 4, p, s, * 등등 사용가능.. #

plt.plot(x, y, 'm<')
plt.show()
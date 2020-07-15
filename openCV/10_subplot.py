import numpy as np
import matplotlib.pyplot as plt

x = np.arange(30)

plt.subplot(2, 2, 1)
plt.plot(x, x**2)

plt.subplot(2, 2, 2)
plt.plot(x, x)

plt.subplot(223)
plt.plot(x, np.tan(x))

plt.subplot(224)
plt.plot(x, np.cos(x))

plt.show()

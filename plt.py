import matplotlib.pyplot as plt
import numpy as np
import math

a = 100
b = 0.5

x = np.arange(0.0001, 200.0, 1.0)
y = x
z = x / (1.0 + (a / x)**b)
d = y-z

plt.plot(x, y, color="red", linestyle='-.')
plt.plot(x, z, color="blue", linestyle="-")
plt.plot(x, d, color="black", linestyle=":")
plt.show()

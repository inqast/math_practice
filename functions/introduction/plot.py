import numpy as np
from matplotlib import pyplot as plt

coefs = np.array([1, 3, -9, -23, -12])

f = np.poly1d(coefs)

x = np.arange(-4, 3, 0.1)
result = f(x)

plt.plot(x, result)
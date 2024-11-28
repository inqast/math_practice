import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Считывание данных. В результате data - NumPy массив.
data = pd.read_csv('https://code.s3.yandex.net/Math/datasets/oleg_float.csv', index_col=0)
data = data.values.astype(float)

x = data[:, 1]
y = data[:, 2]

plt.scatter(x, y)

coefs = np.polyfit(x, y, 1)
f = np.poly1d(coefs)

trend_y = f(x)

print(coefs)
plt.plot(x, trend_y)
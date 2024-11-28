import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Чтение данных. data - NumPy массив с 7-ю столбцами.
vals = pd.read_csv('https://code.s3.yandex.net/Math/datasets/auto-mpg.csv').to_numpy()

x = vals[:,4]
y = vals[:,0]

plt.scatter(x, y, c=vals[:,1])
plt.xscale("log")
plt.yscale("log")
import numpy as np

# Данная функция.
def f(x):
    return np.log((3 * x - 1) ** 2 + (2 * x - 4) ** 2 + (x - 0.5) ** 2)

dx = 1e-8
x = -2.5

df = (f(x+dx)-f(x))/dx
print(df)
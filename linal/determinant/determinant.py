import numpy as np

w = np.array([
    [-7, 4],
    [5, 8]
])

q = np.array([
    [9, -11, 56],
    [3, -6, -8],
    [2, 17, 4]
])

print("Матрица:")
print(w)
print("Определитель:")
print(np.linalg.det(w))
print("Матрица:")
print(q)
print("Определитель:")
print(np.linalg.det(q))

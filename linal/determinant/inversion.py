import numpy as np

a = np.array([
    [-8, 3, 9, 6],
    [0, 6, 0, 3],
    [1, 2, 78, 4.7],
    [2, 315, 0.6, 7]
])

b = np.linalg.inv(a)

print("Матрица:")
print(a)
print("Обратная матрица:")
print(b)
print("Проверка единичной матрицей:")
print((a @ b).round())
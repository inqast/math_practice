import numpy as np

a = np.array([
    [-5, 1, 3, 6],
    [-3, 2, -1, 8],
    [4, -12, 9, 0],
    [0, 3, 6, 2]
])
a_inv = np.linalg.inv(a)

y = np.array([3, 11, -6, 5]).reshape(4, 1)
f = np.array([8, -2, 1, 3]).reshape(4, 1)

y_image = a_inv @ y
f_proto = a @ f

print("Прообраз точки Y:")
print(y_image)
print("Проверка:")
print(a @ y_image)
print("Образ точки F:")
print(f_proto)
print("Проверка:")
print(a_inv @ f_proto)

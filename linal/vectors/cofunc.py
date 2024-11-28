import numpy as np

sin_alpha = -np.pi/4
cos_beta = np.pi/5

a = np.arcsin(sin_alpha)
b = np.arccos(cos_beta)

print(np.rad2deg(a), np.rad2deg(b)) # Вывод значения углов альфа и бета
print(np.tan(a)) # Вывод значения тангенса угла альфа
print(np.tan(b)) # Вывод значения тангенса угла бета
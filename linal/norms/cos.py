from numpy import array, arccos, rad2deg
from numpy.linalg import norm

A = array([2, -12, 8.5])
B = array([0.7, 21.2, 0.8])
C = array([5, -0.6, -4])
D = array([1, -8.2, 5])

BA = A - B
BC = C - B

cos_angle = BA @ BC / norm(BA) / norm(BC)
angle = arccos(cos_angle)
print("Косинус угла:", cos_angle)
print("Сам угол:", rad2deg(angle))

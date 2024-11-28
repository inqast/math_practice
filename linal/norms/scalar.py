from numpy import array

c = array([31, 2, 0.8, 44, -20])
d = array([2, 7.625, 34, -0.5, 8])

a = 2.5 * c - 8 * d
b = -4 * c + 7 * d

print(a @ b)

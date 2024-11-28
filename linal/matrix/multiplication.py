from numpy import array


a = array([8, -3, 1, 6])

C = array([
    [0, 6, -4, 2],
    [1, 8, 7, -12],
    [5, 0, -2, 8],
    [3, 8, 2, 4]
])

Z = array([
    [1, 1, -9, 4],
    [2, 8, 4, 6],
    [0, 8, 6, 0],
    [1, 5, -3, 4]
])

M = array([
    [2, 15, 1],
    [1, -7, 9],
    [3, 3, 7], 
    [0, 5, 12]
])

print("Произведение Za:")
print(Z @ a)
print()
print("Произведение CM:")
print(C @ M)
print()
print("Произведение a^TM:")
print(a.T @ M)
print()
print("Произведение CZ:")
print(C @ Z)
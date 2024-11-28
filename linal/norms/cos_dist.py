from numpy import array
from numpy.linalg import norm

s1 = array([1,1,1,1,1,1,1,0,0,0,0])
s2 = array([0,1,0,0,0,0,0,1,1,1,0])
s3 = array([0,1,0,1,1,0,0,0,0,1,1])

print("СМИ 1 и 2:", s1 @ s2 / norm(s1) / norm(s2))
print("СМИ 1 и 3:", s1 @ s3 / norm(s1) / norm(s3))
print("СМИ 2 и 3:", s2 @ s3 / norm(s2) / norm(s3))

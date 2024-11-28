from scipy.integrate import quad
import numpy as np

def p(x):
	return np.exp(-(x-65)**2 / 800) / 20 / np.sqrt(2*np.pi)

res, err = quad(p, 60, 120)

print(res)
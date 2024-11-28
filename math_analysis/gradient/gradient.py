import  numpy as np

x = np.array([1, 2])

def f(x):
    return (x[0]*np.log(x[0]) + x[1]) ** 2


def dx(x):
    return 2*(x[0]*np.log(x[0]) + x[1])*(np.log(x[0])+1)


def dy(x):
    return 2*(x[0]*np.log(x[0]) + x[1])
    
def grad(x):
	return np.array([dx(x),dy(x)])

gamma = 0.1
eps = 1e-5
max_iters = 5000

val_f_old = f(x)

x = x - grad(x)*gamma
val_f_new = f(x)

iter = 1
while abs(val_f_old - val_f_new) > eps and iter < max_iters:
    print(val_f_old, val_f_new)
    
    val_f_old = val_f_new
    
    x = x - grad(x)*gamma
    val_f_new = f(x)

# Вывод точки.
print('------------')
print('Финальное значение точки x:')
print(x)
print('Финальное значение f(x):')
print(val_f_new)
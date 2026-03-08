from numpy import sin, cos, exp, pi
from scipy.integrate import quad

func = input('f(x) = ')

def f(x):
    return eval(func)

try:
    F = quad(f, 0, pi)
    print(f'The integral of f(x) = {func} between x = [0, π] is {F[0]:g}, with an error of {F[1]:g}.')
except TypeError:
    print('TypeError: Please input the correct format (e.g.: \'sin(x)\', not \'sin\').')
except NameError:
    print('This function or number is not supported by this program; please use only sin, cos, and exp functions and pi.')
except OverflowError:
    print('A value too large appears when calculating the integral.')

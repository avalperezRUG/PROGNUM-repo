from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

A = float(input('A = '))
x0 = float(input('x0 = '))
sig = float(input('sig = '))
z0 = float(input('z0 = '))
lowlim = float(input('Lower Integration Limit = '))
uplim = float(input('Upper Integration Limit = '))

N = (uplim - lowlim) / 10
x = np.arange(lowlim, uplim+N, N)

def g(x):
    return A*np.exp(-(x-x0)**2/(2*sig**2))+z0

G = integrate.quad(g, lowlim, uplim)
print(G)


X = np.arange(lowlim - (1 + lowlim*.1), uplim + (1 + uplim*.1), N/2)
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
Ga = gauss(X,A,x0,sig,z0)

plt.plot(X, Ga)
plt.fill_between(x, g(x), label=f'Area = {G[0]:f}')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt


def RiemannZeta(n, limit):
    total = 1
    for k in range(limit):
        value = 1 / ((k + 1) ** n)
        total = total + value

    return total


criticalLine = 1 / 2

imag = np.arange(-40, 40, 0.01)

D = np.zeros([1, len(imag)], dtype=complex)

a = 0
for im in imag:
    D[0, a] = RiemannZeta(criticalLine + im * 1j, 100)
    a += 1

X = np.real(D)
Y = np.imag(D)

plt.scatter(X, Y)
plt.show()

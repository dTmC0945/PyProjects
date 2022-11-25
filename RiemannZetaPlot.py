import numpy as np


def RiemannZeta(n, limit):
    total = 1
    for k in range(limit):
        value = 1 / pow(k + 1, n)
        total = total + value

    return total

realLimit = 10
imagLimit = 10

D = np.zeros([realLimit, imagLimit])

for a in range(realLimit):
    for b in range(imagLimit):
        print(b*1j)
        D[a][b] = RiemannZeta(a + b*1j, 100)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def madhavaLeibniz1(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = 1 / (2 * k + 1) * pow(-1, k)
        cache = value + cache
        output[k] = cache
        k += 1
    return output * 4


def madhavaLeibniz2(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = 1 / (2 * k + 1) * pow(-3, -k)
        cache = value + cache
        output[k] = cache
        k += 1
    return output * np.sqrt(12)


n = 100

x = np.arange(0, n, 1)

y1 = madhavaLeibniz1(n)
y2 = madhavaLeibniz2(n)

ax = plt.plot(x, y1, 'r--',x, y2)
ax.set_yscale('log')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme()
sns.set_style("ticks")
sns.set_context("paper")
sns.axes_style()
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
n = 15

def leibniz(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = 1 / (2 * k + 1) * pow(-1, k)
        cache = value + cache
        output[k] = cache
        k += 1
    return output * 4


def madhava(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = 1 / (2 * k + 1) * pow(-3, -k)
        cache = value + cache
        output[k] = cache
        k += 1
    return output * np.sqrt(12)


def euler(n):
    output = np.ones(n)
    return 20 * np.arctan(1 / 7) + 8 * np.arctan(3 / 79) * output


def newton(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = pow(np.math.factorial(k), 2) * pow(2, k) / np.math.factorial(2 * k + 1)
        cache = value + cache
        output[k] = cache
        k += 1
    return output * 2


def ramanujan(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = np.math.factorial(4 * k) * (1103 + 26390 * k) / (pow(np.math.factorial(k), 4) * pow(396, 4 * k))
        cache = value + cache
        output[k] = cache
        k += 1
    return 1 / (output * 2 * np.sqrt(2) / 9801)


def chudnovsky(n):
    output = np.zeros(n)
    cache = 0
    k = 0
    while k < n:
        value = pow(-1, k) * np.math.factorial(6 * k) * (13591409 + 545140134 * k) / (
                    pow(np.math.factorial(k), 3) * pow(np.math.factorial(k), 3) * pow(640320, 3 * k + 3 / 2))
        cache = value + cache
        output[k] = cache
        k += 1
    return 1 / (output * 12)




x = np.arange(0, n, 1)

df1 = pd.DataFrame({'x': x, 'y': chudnovsky(n)})
df2 = pd.DataFrame({'x': x, 'y': ramanujan(n)})
df3 = pd.DataFrame({'x': x, 'y': newton(n)})
df4 = pd.DataFrame({'x': x, 'y': madhava(n)})
df5 = pd.DataFrame({'x': x, 'y': leibniz(n)})

y1 = madhava(n)
y2 = chudnovsky(n)
g_results1 = sns.lineplot(data=df1, x='x', y='y', color="red")
g_results2 = sns.lineplot(data=df2, x='x', y='y')
g_results3 = sns.lineplot(data=df3, x='x', y='y')
g_results4 = sns.lineplot(data=df4, x='x', y='y')
g_results5 = sns.lineplot(data=df5, x='x', y='y')

#g_results.set(xscale='log')

sns.despine()

plt.show()

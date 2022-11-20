import numpy as np
from mpmath import mp
from matplotlib import pyplot as plt
import seaborn


def PhasorPlot(Array):
    x_main = 0
    y_main = 0

    PlotArray = np.zeros((len(Array), 4))

    for i in range(len(Array)):
        x = Array[i][0]
        y = Array[i][1]
        x_main = x_main + x
        y_main = y_main + y

    x_main = abs(x_main)
    y_main = abs(y_main)

    for i in range(len(Array) - 1):
        PlotArray[i][2] = Array[i + 1][0]
        PlotArray[i][3] = Array[i + 1][1]

        x_sub_main = 0
        y_sub_main = 0

        j = 0
        while j <= i + 1:
            x = Array[j][0]
            y = Array[j][1]
            x_sub_main = x_sub_main + x
            y_sub_main = y_sub_main + y
            j += 1
        PlotArray[i + 1][0] = x_sub_main
        PlotArray[i + 1][1] = y_sub_main

    PlotArray[-1] = [0, 0, 0, 0]

    X, Y, U, V = zip(*PlotArray)
    x = np.linspace(0.2, 10, 100)
    seaborn.set(style='ticks')

    plt.figure()
    plt.ylabel("Imaginary - Axis")
    plt.xlabel("Real - Axis")
    plt.plot(0, 0, 'ok')  # <-- plot a black point at the origin
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', color=['r', 'b', 'g'], scale=1)
    ax.set_xlim([- x_main - 5, x_main + 5])
    ax.set_ylim([- y_main - 5, y_main + 5])
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    plt.axvline(0)
    plt.axhline(0)
    seaborn.despine(ax=ax, offset=0)  # the important part here
    plt.draw()
    plt.show()


digits = 10

value = mp.nstr((mp.mpf(mp.pi)), digits)

print(value)
my_list = []

for x in str(value):
    my_list.append(str(x))

my_list.remove('.')

data = list(map(int, my_list))

Array = np.zeros((digits, 2))

k = 0
for n in data:
    print(n)
    Array[k] = [5 * np.sin(2 * np.pi / 10 * n), 5 * np.cos(2 * np.pi / 10 * n)]
    k += 1

print(Array)

PhasorPlot(Array)
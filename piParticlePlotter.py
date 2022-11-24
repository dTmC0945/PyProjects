import numpy as np  # needed for array and trigo functions
from mpmath import mp  # needed to get the digits of pi
from matplotlib import pyplot as plt  # to plot stuff


def VectorPlot(array):
    plot_array = np.zeros((len(array), 4))

    for i in range(len(array) - 1):
        plot_array[i][2] = array[i + 1][0]
        plot_array[i][3] = array[i + 1][1]

        x_sub_main = 0
        y_sub_main = 0

        j = 0
        while j <= i + 1:
            x = array[j][0]
            y = array[j][1]
            x_sub_main = x_sub_main + x
            y_sub_main = y_sub_main + y
            j += 1
        plot_array[i + 1][0] = x_sub_main
        plot_array[i + 1][1] = y_sub_main

    plot_array[-1] = [0, 0, 0, 0]

    x, y, u, v = zip(*plot_array)
    plt.style.use('dark_background')

    plt.figure()
    plt.plot(0, 0, 'ow')  # plot a white point at the origin
    ax = plt.gca()
    ax.quiver(x, y, u, v, scale_units='xy', color=["r", "b", "g", "c", "m", "y", "w"], scale=1)

    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('equal')
    ax.grid(False, which='both')
    plt.draw()
    plt.show()

    return plot_array


digits = 1000  # number of digits to be plotted
mp.dps = digits  # sets the precision to the mpmath function

value = mp.nstr((mp.mpf(mp.pi)), digits)  # gets the pi value and converts into string.

my_list = []  # generate an empty array

# convert all the string to individual string values. Including . which we need to remove.
for ii in str(value):
    my_list.append(str(ii))

my_list.remove('.')  # removes the annoying .

data = list(map(int, my_list))  # converts the string values to integer values. The final hurdle

Array = np.zeros((digits + 1, 2))  # generate a zero array for the vector plot
# convert the bits into a vector plot.
k = 1
for n in data:
    Array[k] = [5 * np.cos(2 * np.pi / 10 * n), 5 * np.sin(2 * np.pi / 10 * n)]
    k += 1

# Finally plotting
k = VectorPlot(Array)
p = np.hsplit(k, [2])

a = p[0]

plt.hist(a[:,0], bins=200)
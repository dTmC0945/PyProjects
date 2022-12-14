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

    return plot_array


digits = 500  # number of digits to be plotted
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
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

rect_diff = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

plt.style.use('dark_background')

plt.figure(figsize=(6, 6))

ax_diff = plt.axes(rect_diff)
ax_diff.tick_params(direction='in', top=False, right=True)
ax_histx = plt.axes(rect_histx)
ax_histx.tick_params(direction='in', labelbottom=False)
ax_histy = plt.axes(rect_histy)
ax_histy.tick_params(direction='in', labelleft=False)

plot_array = VectorPlot(Array)

x, y, u, v = zip(*plot_array)

ax_diff.plot(0, 0, 'ow')  # plot a white point at the origin
# ax_diff = plt.gca()
ax_diff.quiver(x, y, u, v, scale_units='xy', color=["r", "b", "g", "c", "m", "y", "w"], scale=1)

ax_diff.spines['left'].set_color('none')
ax_diff.spines['right'].set_color('none')
ax_diff.spines['bottom'].set_color('none')
ax_diff.spines['top'].set_color('none')

ax_diff.set_aspect('equal')
ax_diff.grid(False, which='both')

ax_diff.axis("off")

Xx, Yy = plot_array[:, 0], plot_array[:, 1]

binwidth = 0.1
lim = np.ceil(np.abs([x, y]).max() / binwidth) * binwidth
ax_diff.set_xlim((-lim, lim))
ax_diff.set_ylim((-lim, lim))

bins = np.arange(-lim, lim + binwidth, binwidth)

ax_histx.hist(Xx, bins=bins)
ax_histy.hist(Yy, bins=bins, orientation='horizontal')

ax_histx.spines['left'].set_color('none')
ax_histx.spines['right'].set_color('none')
ax_histx.spines['top'].set_color('none')

ax_histy.spines['bottom'].set_color('none')
ax_histy.spines['right'].set_color('none')
ax_histy.spines['top'].set_color('none')

plt.show()

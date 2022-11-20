import numpy as np
import matplotlib.pyplot as plt


class Brownian:

    def __init__(self, x0=1):
        assert (type(x0) == float or type(x0) == int or x0 is None)

        self.x0 = float(x0)

    def gen_random_walk(self, n_step=10):

        w = np.ones((n_step, 1)) * self.x0

        ii = 0

        while ii < n_step:
            yi = np.random.choice([1, -1])

            w[ii] = w[ii - 1] + (yi / np.sqrt(n_step))

            ii += 1

        return w

    def gen_normal(self, n_step=100):

        w = np.ones(n_step) * self.x0

        for i in range(1, n_step):
            yi = np.random.normal()

            w[i] = w[i - 1] + (yi / np.sqrt(n_step))

        return w


b1 = Brownian()
b2 = Brownian()

x = b1.gen_normal(10000)
y = b2.gen_normal(10000)

plt.plot(x,y,c='b')
xmax,xmin,ymax,ymin = x.max() * 1.1 ,x.min() * 1.1 ,y.max() * 1.1 ,y.min() * 1.1
scale_factor = 1
xmax,xmin,ymax,ymin = xmax*scale_factor,xmin*scale_factor,ymax*scale_factor,ymin*scale_factor
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.show()

plt.style.use('dark_background')

ax = plt.plot(b.gen_random_walk(1000),  color="white")


plt.figure()
ax = plt.gca()

ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_aspect('equal')
ax.grid(False, which='both')
plt.draw()
plt.show()

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
patch = plt.Circle((5, -5), 0.75, fc='y')

def init():
    patch.center = (0, 0)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 0 + 3 * np.sin(np.radians(i))
    y = 0 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=2,
                               blit=True)

plt.show()

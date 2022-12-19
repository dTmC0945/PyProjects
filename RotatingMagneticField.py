import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

X, Y = np.sin(np.arange(0,0.01, 2*np.pi)), np.cos(np.arange(0,0.01, 2*np.pi))

U = np.cos(X)
V = np.sin(Y)

fig, ax = plt.subplots(1, 1)
Q = ax.quiver(X, Y, U, V, pivot='mid', color='r', units='inches')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)


def update_quiver(num, Q, X, Y):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """

    U = np.cos(X + num * 0.1)
    V = np.sin(Y + num * 0.1)

    Q.set_UVC(U, V)

    return Q,


# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=50, blit=False)
fig.tight_layout()
plt.show()

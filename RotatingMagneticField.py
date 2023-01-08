import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# X, Y = np.sin(np.arange(0, 0.01, 2*np.pi)), np.cos(np.arange(0, 0.01, 2*np.pi))

X, Y = 0, 0
U, V = 1 * np.sin(np.pi / 4), 1 * np.cos(np.pi / 4)
fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, pivot='tail', color='r', units='inches')

ax.set_xlim(-5, 5), ax.set_ylim(-5, 5)


def update_quiver(num, Q, X, Y, phase, amplitude):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U = X + (np.sin(num * 2 * np.pi / 100 - phase)) * np.sin(phase) * amplitude
    V = Y + (np.sin(num * 2 * np.pi / 100 - phase)) * np.cos(phase) * amplitude

    Q.set_UVC(U, V)

    return Q

circle1 = plt.Circle((0, 0), 5, color='r', fill=False)

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
ani1 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, 0, 5), interval=1)
ani2 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, 2*np.pi/3, 5), interval=1)
#fig.tight_layout()
ax.add_patch(circle1)
ax.set_box_aspect(1)
plt.show()

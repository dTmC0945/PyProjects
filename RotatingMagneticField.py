import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# X, Y = np.sin(np.arange(0, 0.01, 2*np.pi)), np.cos(np.arange(0, 0.01, 2*np.pi))

X, Y = [0, 0, 0], [0, 0, 0]
U, V = [1*np.cos(np.pi/2), 1*np.cos(np.pi/2 + 2*np.pi/3), 1*np.cos(np.pi/2 - 2*np.pi/3)],\
       [1*np.sin(np.pi/2), 1*np.sin(np.pi/2 + 2*np.pi/3), 1*np.sin(np.pi/2 - 2*np.pi/3)]

fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, pivot='tail', color='r', units='inches')

ax.set_xlim(-5, 5), ax.set_ylim(-5, 5)


def update_quiver(num, Q, X, Y):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U = [X[0] + (np.sin(num * 2 * np.pi / 100 - np.pi/2)) * np.sin(np.pi/2),
         X[1] + (np.sin(num * 2 * np.pi / 100 - np.pi/2 - 2 * np.pi/3)) * np.sin(np.pi/2 + 2 * np.pi/3),
         X[2] + (np.sin(num * 2 * np.pi / 100 - np.pi/2 + 2 * np.pi/3)) * np.sin(np.pi/2 - 2 * np.pi/3)]

    V = [Y[0] + (np.sin(num * 2 * np.pi / 100 - np.pi/2)) * np.cos(np.pi/2),
         Y[1] + (np.sin(num * 2 * np.pi / 100 - np.pi/2 - 2 * np.pi/3)) * np.cos(np.pi/2 + 2 * np.pi/3),
         Y[2] + (np.sin(num * 2 * np.pi / 100 - np.pi/2 + 2 * np.pi/3)) * np.cos(np.pi/2 - 2 * np.pi/3)]

    Q.set_UVC(U, V)

    return Q


Inner_Stator = plt.Circle((0, 0), 5, color='k', fill=False)

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
ani1 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=1)
fig.tight_layout()
ax.add_patch(Inner_Stator)
ax.set_box_aspect(1)
plt.show()

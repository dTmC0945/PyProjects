import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# X, Y = np.sin(np.arange(0, 0.01, 2*np.pi)), np.cos(np.arange(0, 0.01, 2*np.pi))

X, Y = [0, 0, 0], [0, 0, 0]
U, V = [1, 1*np.cos(2*np.pi/3), 1*np.cos(-2*np.pi/3)], [1, 1*np.sin(2*np.pi/3), 1*np.sin(4*np.pi/3)]

fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, scale=5, pivot='tail', color='r', units='inches')
plt.show()

ax.set_xlim(-5, 5), ax.set_ylim(-5, 5)


def update_quiver(num, Q, X, Y, phase, amplitude):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U = X[1] + (np.sin(num * 2 * np.pi / 100 - phase)) * np.sin(phase) * amplitude
    V = Y[1] + (np.sin(num * 2 * np.pi / 100 - phase)) * np.cos(phase) * amplitude

    Q.set_UVC(U, V)

    return Q


Inner_Stator = plt.Circle((0, 0), 5, color='k', fill=False)

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
#ani1 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, 0, 5), interval=1)
#ani2 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, 2*np.pi/3, 5), interval=1)
#fig.tight_layout()
#ax.add_patch(Inner_Stator)
#ax.set_box_aspect(1)
#plt.show()

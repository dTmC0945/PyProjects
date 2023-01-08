import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

phase = 10


def quiverGeneration(phase):
    x_int, y_int, x_dest, y_dest = [], [], [], []
    for i in range(phase):
        x_int.append(0), y_int.append(0)
        x_dest.append(1 * np.cos(i * np.pi / phase))
        y_dest.append(1 * np.sin(i * np.pi / phase))
    return x_int, y_int, x_dest, y_dest


X, Y, U, V = quiverGeneration(phase)

fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, pivot='tail', color='r', units='xy', scale=1)

ax.set_xlim(-1, 1), ax.set_ylim(-1, 1)


def update_quiver(num, Q, X, Y, phase):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U, V = [], []
    for i in range(phase):
        U.append(X[i] + (np.sin(num * np.pi / 50 - (i * np.pi / phase)) *
                         np.sin(i * np.pi / phase)))
        V.append(Y[i] + (np.sin(num * np.pi / 50 - (i * np.pi / phase)) *
                         np.cos(i * np.pi / phase)))


    Q.set_UVC(U, V)

    return Q


Inner_Stator = plt.Circle((0, 0), 1, color='k', fill=False)
Middle_Stator = plt.Circle((0, 0), 0.5, color='k', fill=False, linestyle='--', alpha =0.25)

Central = plt.Circle((0, 0), 0.05, color='k', fill=True)

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
ani1 = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, phase), interval=10)
fig.tight_layout()
ax.add_patch(Inner_Stator)
ax.add_patch(Middle_Stator)
ax.add_patch(Central)
ax.set_box_aspect(1)
plt.show()

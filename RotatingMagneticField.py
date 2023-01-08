import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# number of phases in the system
phase = 100


# function to define the quiver points for the number of phases
def quiverGeneration(value):
    x_int, y_int, x_dest, y_dest = [], [], [], []
    for i in range(value):
        x_int.append(0), y_int.append(0)
        x_dest.append(1 * np.cos(i * np.pi / value))
        y_dest.append(1 * np.sin(i * np.pi / value))
    return x_int, y_int, x_dest, y_dest


# get the necessary values from the function
X, Y, U, V = quiverGeneration(phase)

fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, pivot='tail', color=(.4, .5, .6), units='xy', scale=1)


def update_quiver(num, Q, X, Y, value):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U, V = [], []
    for i in range(value):
        U.append(X[i] + (np.sin(num * np.pi / 50 - (i * np.pi / value)) *
                         np.sin(i * np.pi / value)))
        V.append(Y[i] + (np.sin(num * np.pi / 50 - (i * np.pi / value)) *
                         np.cos(i * np.pi / value)))

    Q.set_UVC(U, V)

    return Q


Inner_Stator = plt.Circle((0, 0), 1, color='k', fill=False)
Middle_Stator = plt.Circle((0, 0), 0.5, color='k', fill=False, linestyle='--', alpha=0.25)

Central = plt.Circle((0, 0), 0.05, color='k', fill=True)

# cleared on subsequent frames
anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y, phase), interval=1)
fig.tight_layout()
ax.set_xlim(-1, 1), ax.set_ylim(-1, 1)
ax.add_patch(Inner_Stator)
ax.add_patch(Middle_Stator)
ax.add_patch(Central)
ax.set_box_aspect(1)
plt.show()

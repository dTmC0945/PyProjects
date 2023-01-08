import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# X, Y = np.sin(np.arange(0, 0.01, 2*np.pi)), np.cos(np.arange(0, 0.01, 2*np.pi))

X, Y = 0, 0
U, V = 1 * np.sin(np.pi / 4), 1 * np.cos(np.pi / 4)
fig, ax = plt.subplots(1, 1)

Q = ax.quiver(X, Y, U, V, pivot='tail', color='r', units='inches')

ax.set_xlim(-5, 5), ax.set_ylim(-5, 5)


def update_quiver(num, X, Y, phase, amplitude):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U = X + (np.sin(num * 2 * np.pi / 100 - phase)) * np.sin(phase) * amplitude
    V = Y + (np.sin(num * 2 * np.pi / 100 - phase)) * np.cos(phase) * amplitude

    U2 = X + (np.sin(num * 2 * np.pi / 100 - (phase + 2*np.pi/3))) * np.sin(phase + 2*np.pi/3) * amplitude
    V2 = Y + (np.sin(num * 2 * np.pi / 100 - (phase + 2*np.pi/3))) * np.cos(phase + 2*np.pi/3) * amplitude

    Q.set_UVC(U2, V2)
    Q

    return Q


# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
anim1 = animation.FuncAnimation(fig, update_quiver, fargs= (X, Y, 2*np.pi/3, 5), interval=5, blit=False)
fig.tight_layout()
plt.show()

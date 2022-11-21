import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

scale = 2
particles = 2


def E(q, r0, x, y):
    den = np.hypot(x - r0[0], y - r0[1]) ** 3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


# Grid of x, y points
nx, ny = 128, 128
x, y = np.linspace(-scale, scale, nx), np.linspace(-scale, scale, ny)
X, Y = np.meshgrid(x, y)

# Create a multi-pole with nq charges of alternating sign, equally spaced
# on the unit circle.

charges = []
for i in range(particles):
    q = i % 2 * 2 - 1
    charges.append((q, (np.cos(2 * np.pi * i / particles), np.sin(2 * np.pi * i / particles))))

# Electric field vector, E=(Ex, Ey), as separate components
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey

plt.style.use('dark_background')

fig = plt.figure()
ax = fig.add_subplot(111)

charge_colors = {True: '#aa0000', False: '#0000aa'}  # Add filled circles for the charges themselves (blue and red)
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.11, color="white"))
    ax.add_artist(Circle(pos, 0.1, color=charge_colors[q > 0]))

# Plotting information -------------------------------------------------------------------------------------------------

color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=0.5, cmap=plt.cm.autumn, density=1.2, arrowstyle='->', arrowsize=0.2)

ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim(-scale, scale)
ax.set_ylim(-scale, scale)

ax.set_aspect('equal')

plt.show()

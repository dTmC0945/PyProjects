import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Mean magnitude of the Earth's magnetic field at the equator in T
B_0 = 3.12e-5
# Radius of Earth, Mm (10^6 m: mega-metres!)
RE = 6.370
# Deviation of magnetic pole from axis
alpha = np.radians(9.6)


def B(r, theta):
    """Return the magnetic field vector at (r, theta)."""
    fac = B_0 * (RE / r) ** 3
    return -2 * fac * np.cos(theta + alpha), -fac * np.sin(theta + alpha)


# Grid of x, y points on a Cartesian grid
nx, ny = 400, 400
xmax, ymax = 80, 80
x = np.linspace(-xmax, xmax, nx)
y = np.linspace(-ymax, ymax, ny)
X, Y = np.meshgrid(x, y)
r, theta = np.hypot(X, Y), np.arctan2(Y, X)

# Magnetic field vector, B = (Ex, Ey), as separate components
Br, Btheta = B(r, theta)
# Transform to Cartesian coordinates: NB make North point up, not to the right.
c, s = np.cos(np.pi / 2 + theta), np.sin(np.pi / 2 + theta)
Bx = -Btheta * s + Br * c
By = Btheta * c + Br * s

fig, ax = plt.subplots()

# Plot the streamlines with an appropriate colormap and arrow style
color = 2 * np.log(np.hypot(Bx, By))
ax.streamplot(x, y, Bx, By, color=color, linewidth=0.5, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=0.5)

# Add a filled circle for the Earth; make sure it's on top of the streamlines.
ax.add_patch(Circle((0, 0), RE, color='k', zorder=100))
ax = plt.gca()

ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-xmax, xmax)
ax.set_ylim(-ymax, ymax)
ax.set_aspect('equal')
plt.style.use('dark_background')

plt.show()

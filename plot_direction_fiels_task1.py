import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero


def df(x, y):
    return y * y - 2 * y + x


def foo(y):
    return -(y - 1) ** 2


fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

# Mesh Grid for the Direction Field
minx = -6
maxx = 6
xsteps = 13
miny = -3
maxy = 3
ysteps = 13
x, y = np.meshgrid(np.linspace(minx, maxx, xsteps), np.linspace(miny, maxy, ysteps))

# Direction values for the vectors
u = x - x + 1
v = 1 * df(x, y)

# Normalize the vectors so they are the same size
r = np.power(np.add(np.power(u, 2), np.power(v, 2)), 0.5)

# Use vectorw with no arrow heads
plt.quiver(x, y, u / r, v / r, angles="xy", headwidth=0)

solutionsteps = 101
p0 = 2.5
t = np.linspace(miny, maxy, solutionsteps)
# Sol1 = odeint(foo, p0, t, tfirst=True)
# plt.plot(t, Sol1, 'k')

plt.plot(list(map(lambda y: -(y - 1) ** 2, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -(y - 1) ** 2 + 1.5, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -(y - 1) ** 2 + 0.5, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -(y - 1) ** 2 + 2, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -(y - 1) ** 2 + 2.5, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -(y - 1) ** 2 - 0.5, list(t))), list(t), 'k')
plt.plot(list(map(lambda y: -y ** 2 + 2*y, list(t))), list(t), 'r')

plt.plot(list(map(lambda y: -y ** 2 + 2*y - 1/(2*y -2) , list(t))), list(t), 'y')

plt.show()

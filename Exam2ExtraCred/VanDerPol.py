import numpy as np
import matplotlib.pyplot as plt

# Python file to plot the phase portrait of a Van Der Pol oscillator with a given mu.
# Some code borrowed and modified from the excellent work of John Kitchin at the CMU ChemE department.

mu = 100


# differential equation.
def x_dot(x, t):
    x1, x2 = x
    return [x2, mu * (1 - x1 * x1) * x2 - x1]


# thetas and omegas to plot.
x1 = np.linspace(-100, 100, 20)
x2 = np.linspace(-100, 100, 20)

# create variables for the vectors. this is not the python-y way of doing it, but it works.
X1, X2 = np.meshgrid(x1, x2)
u, v = np.zeros(X1.shape), np.zeros(X2.shape)

NI, NJ = X1.shape

# time variable. In this case, the system is time-invariant (aka autonomous) so this isn't used.
t = 0

# get component of the vector for each point on the plot.
for i in range(NI):
    for j in range(NJ):
        x = X1[i, j]
        y = X2[i, j]
        y_dot = x_dot([x, y], t)
        u[i, j] = y_dot[0]
        v[i, j] = y_dot[1]

Q = plt.quiver(X1, X2, u, v, color='k')
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.title("Phase Portrait of a Van Der Pol Oscillator with μ = 1")
plt.xlim([-100, 100])
plt.ylim([-100, 100])
plt.savefig("../images/van-der-pol.png")
plt.show()

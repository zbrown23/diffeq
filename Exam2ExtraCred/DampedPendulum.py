import numpy as np
import matplotlib.pyplot as plt

# Python file to plot the phase portrait of a damped pendulum.
# Some code borrowed and modified from the excellent work of John Kitchin at the CMU ChemE department.

# differential equation. In this case, g/L is assumed to be -1 G per meter.

# the damping coefficient
c = 0.5
# time variable. In this case, the system is time-invariant (aka autonomous) so this isn't used.
t = 0


def x_dot(x, t):
    x1, x2 = x
    return [x2, -np.sin(x1) - c * x2]


# thetas and omegas to plot.
theta = np.linspace(-2 * np.pi, 2 * np.pi, 20)
omega = np.linspace(-4, 4, 20)

# create variables for the vectors. this is not the python-y way of doing it, but it works.
Theta, Omega = np.meshgrid(theta, omega)
u, v = np.zeros(Theta.shape), np.zeros(Omega.shape)

NI, NJ = Theta.shape

# get component of the vector for each point on the plot.
for i in range(NI):
    for j in range(NJ):
        x = Theta[i, j]
        y = Omega[i, j]
        y_dot = x_dot([x, y], t)
        u[i, j] = y_dot[0]
        v[i, j] = y_dot[1]

Q = plt.quiver(Theta, Omega, u, v, color='k')
plt.xlabel('Angle (radians)')
plt.ylabel('Angular Velocity (radians/s')
plt.title("Phase Portrait of a Damped Pendulum")
plt.xlim([-2 * np.pi, 2 * np.pi])
plt.ylim([-5, 5])
plt.savefig("../images/Damped-pendulum-phase-portrait.png")
plt.show()

import math
import numpy as np
from matplotlib import pyplot, cm
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


# bifurcation diagram implementation
def yprime(x, y):
    return y * np.cos(x) + 0.2 * (1 - x * np.cos(x))


def plotdiffeq():
    x = np.arange(0, 10, 0.25)
    y = np.arange(0, 20, 0.25)
    t0 = np.arange(0, 20, 0.5)
    for init in t0:
        solution = odeint(yprime, init, x)
        plt.plot(x, solution)


def plotsurface():
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    x, y = np.meshgrid(x, y)
    z = y * np.cos(x) + 0.2 * (1 - x * np.cos(x))
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)


def main():
    plotdiffeq()
    plotsurface()
    plt.show()


if __name__ == '__main__':
    main()

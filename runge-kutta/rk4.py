import math
import numpy as np
import matplotlib.pyplot as plt


# dy/dx = sqrt(y)
def function(x, y):
    return math.sqrt(y)


# fourth order Runge-Kutta method.
def rk4_list(func, y_0, x_0, h, x_f):
    x = x_0
    y = y_0
    series = [(x, y)]
    while x < x_f:
        k1 = h * func(x, y)
        k2 = h * func(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * func(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * func(x + h, y + k3)
        y = y + (1 / 6) * k1 + (1 / 3) * k2 + (1 / 3) * k3 + (1 / 6) * k4
        x = x + h
        series.append((x, y))
    return series


def plot_rk4(func, y_0, x_0, h, x_f):
    series = rk4_list(func, y_0, x_0, h, x_f)
    plotx = []
    ploty = []
    for element in series:
        plotx.append(element[0])
        ploty.append(element[1])
    plt.plot(plotx, ploty, label="rk4 w/ h = " + str(round(h, 3)))
    plt.xlabel("time (s)")
    plt.ylabel("w(t)")


# plot the analytical solution to the dy/dx = sqrt(y) for comparison to rk4.
def plot_analytical_solution(end):
    analytical_plotx = np.linspace(0, end, 100)
    analytical_ploty = 0.25 * (analytical_plotx + 2) ** 2
    plt.plot(analytical_plotx, analytical_ploty, label="Analytical Solution")


# main.
def main():
    plot_rk4(function, 1, 0, 1, 4)
    plot_analytical_solution(4)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()

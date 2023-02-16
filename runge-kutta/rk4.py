import math
import numpy as np
import matplotlib.pyplot as plt


# dy/dx = sqrt(y)
def function(x, y):
    return math.sqrt(y)


# analytical solution to the above differential equation.
def solution(x):
    return 0.25 * (x + 2) ** 2


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
    plt.plot(plotx, ploty, label="rk4 with h = " + str(round(h, 3)))
    plt.xlabel("x")
    plt.ylabel("y(x)")


# function to plot the error of rk4 vs a given analytical solution.
def plot_rk4_error(func, analytical, y_0, x_0, h, x_f):
    series = rk4_list(func, y_0, x_0, h, x_f)
    plotx = []
    ploty = []
    plote = []
    for element in series:
        plotx.append(element[0])
        ploty.append(element[1])
        plote.append(element[1] - analytical(element[0]))
    plt.plot(plotx, plote, label="error when h = " + str(round(h, 3)))
    plt.xlabel("x")
    plt.ylabel("y(x)")


# plot the analytical solution to the dy/dx = sqrt(y) for comparison to rk4.
def plot_analytical_solution(function, end):
    analytical_plotx = np.linspace(0, end, 100)
    analytical_ploty = []
    for element in analytical_plotx:
        analytical_ploty.append(function(element))
    plt.plot(analytical_plotx, analytical_ploty, label="Analytical Solution")


# main.
def main():
    plot_rk4(function, 1, 0, 0.1, 10)
    # plot_rk4_error(function, solution, 1, 0, 0.1, 10)
    plot_analytical_solution(solution, 10)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()

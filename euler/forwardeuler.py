import math
import numpy as np
import matplotlib.pyplot as plt


# the differential equation that euler's method is being run on
def function(y, t):
    return math.sqrt(y)


# run forward euler's method on a function, and return the solution at a point specified by end.
def forward_euler(func, y_0, t_0, h, end):
    t = t_0
    y = y_0
    while t < end:
        y = y + h * func(y, t)
        t = t + h
    return y


# run forward euler's method, but return a time series instead of just the solution at the end.
def forward_euler_list(func, y_0, t_0, h, end):
    t = t_0
    y = y_0
    series = [(t, y)]
    while t < end:
        y = y + h * func(y, t)
        t = t + h
        series.append((t, y))
    return series


# run forward euler's method, return a time series, and plot it as well.
def plot_euler_method(func, x_0, y_0, delta_t, end):
    series = forward_euler_list(func, y_0, x_0, delta_t, end)
    plotx = []
    ploty = []
    for element in series:
        plotx.append(element[0])
        ploty.append(element[1])
    plt.plot(plotx, ploty, label="h = " + str(round(delta_t, 3)))
    plt.xlabel("x")
    plt.ylabel("y(x)")
    return [plotx, ploty]


# plot the analytical solution to the diffeq dy/dx = sqrt(y), with y(0) = 1
def plot_analytical_solution(end):
    analytical_plotx = np.linspace(0, end, 100)
    analytical_ploty = 0.25 * (analytical_plotx + 2) ** 2
    plt.plot(analytical_plotx, analytical_ploty, label="Analytical Solution")


def main():
    plot_euler_method(function, 0, 1, 1, 4)
    plot_euler_method(function, 0, 1, 0.5, 4)
    plot_euler_method(function, 0, 1, 0.25, 4)
    plot_analytical_solution(4)
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()

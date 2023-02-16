import math
import numpy as np
import matplotlib.pyplot as plt
from forwardeuler import forward_euler_list, plot_euler_method, plot_analytical_solution


# the differential equation.
def function(y, t):
    return math.sqrt(y)


# an analytical solution to the differential equation
def solution(t):
    return 0.25 * (t + 2) ** 2


# calculate the integrated error of an euler approximation of a given diff eq and its analytically determined solution.
def euler_error(diffeq, analytical, x_0, y_0, delta_t, end):
    series = forward_euler_list(diffeq, y_0, x_0, delta_t, end)
    plotx = []
    ploty = []
    solutiony = []
    for element in series:
        plotx.append(element[0])
        ploty.append(element[1])
        solutiony.append(analytical(element[0]))
    return integrate_error(ploty, solutiony, delta_t)


# function that integrates the difference between two functions represented by a lists via a Riemann sum.
def integrate_error(a, b, delta_t):
    i = 0
    error = 0
    for element in a:
        error = error + math.fabs(element - b[i]) * delta_t
        i = i + 1
    return error


# plot the error series with a given start ∆t, stop ∆t, # of ∆t values to try, and endpoint.
# plotsolution is a boolean that enables plotting y over t in a separate figure
# numsolutionplots specifies the number of solutions to plot, for instance
# if steps is very large, and you would not like to plot every single ∆t value.
def plot_error_series(start_deltat, stop_deltat, steps, end, plotsolution, numsolutionplots=None):
    if numsolutionplots is not None:  # check to see if numsolutionplots was specified
        mod = steps / numsolutionplots
    else:  # if it wasn't, plot every solution
        mod = 1
    error_series = []
    delta_tlist = np.linspace(start_deltat, stop_deltat, steps)  # create the list of ∆t values to try
    for idx, delta_t in enumerate(delta_tlist):  # try that euler instance and then plot its integrated error.
        error_series.append(euler_error(function, solution, 0, 1, delta_t, end))
        if plotsolution and (idx % mod == 0):  # if you're supposed to plot the solution, do it.
            plot_euler_method(function, 0, 1, delta_t, end)
    plt.legend()  # plot the legend
    plt.figure(2)  # change the figure to two, so you can plot the error series.
    plt.plot(delta_tlist, error_series)
    plt.xlabel("h")
    plt.ylabel("integrated error")


def main():
    plot_error_series(10, 1e-6, 100, 10, True, 10)  # plot the error series and it's associated stuff.
    plt.figure(1)
    plot_analytical_solution(10)  # plot the analytical solution on figure 1
    plt.legend()  # show the legend on figure 1
    plt.show()  # show the plots.


if __name__ == '__main__':
    main()

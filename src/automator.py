#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oscillator import Oscillator
from plot import Plot, Sequence
from movie_writer import save_plot
from matplotlib import pyplot as plt

def main():
    #init
    values = [(1, 1), (0, 2), (0.5, 2), (1, 2), (2, 2), (5, 2)]
    osc = []
    for val in values:
        osc.append(Oscillator(mu=val[0], x0=val[1]))

    # meta
    x1 = Sequence(None, '$x$')
    x2 = Sequence(None, '$\dot{x}$')
    x1.set_color('b')
    x1.set_line_width(2)
    x2.set_color('r')
    x2.set_line_style('')
    x2.set_marker('o')
    figure = Plot([x1, x2])
    figure.set_legend()
    title = figure.title
    line = [None]*5

    # phase plots
    fig=plt.figure()
    ax=fig.add_subplot(111,autoscale_on=False, xlim=(-8,8), ylim=(-8,8))
    ax.grid()
    line[0], line[1], line[2], line[3], line[4], = ax.plot([], [], 'b-',
                                                           [], [], 'r--',
                                                           [], [], 'g-.',
                                                           [], [], 'yo',
                                                           [], [], 'k-',
                                                           lw=2)

    # solve and plot
    for i, plant in enumerate(osc):
        ans = plant.solve(0, 25, 0.01)
        x1.set_data(ans[:,0])
        x2.set_data(ans[:,1])
        figure.set_title(title) # + '\n' + '$\mu$ = {}, $x$ = {}'.format(plant.mu, plant.x0))
        figure.plot()
        if i:
            line[i-1].set_data(ans[:,0], ans[:,1])
        figure.save(i+1, save_plot)

    ax.legend([x[0] for x in values[1:]])
    fig.suptitle(r"Variation with $\mu$ values")
    save_plot(fig, 'variation')

    # create latex
    with open('latex/python_params.tex', 'w') as f:
        f.write("% This is a python generated file. Do not edit since it will be rewritten during make")
        # params used for images
        for i in range(0, len(values), 2):
            f.write(r"""
\begin{figure}[ht]
    \centering
    \begin{minipage}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{%(1)d}
        \caption{%(2)s}
        \label{fig:fig%(1)d}
    \end{minipage}\hfill
    \begin{minipage}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{%(3)d}
        \caption{%(4)s}
        \label{fig:fig%(3)d}
    \end{minipage}
\end{figure}
"""%{
     '1': i+1, '2': r'$\mu$=%(1).1f, $x_0$=%(2).1f'%{'1': values[i][0],
                                                 '2': values[i][1]},
     '3': i+2, '4': r'$\mu$=%(1).1f, $x_0$=%(2).1f'%{'1': values[i+1][0],
                                                 '2': values[i+1][1]}})

if __name__ == "__main__":
    main()

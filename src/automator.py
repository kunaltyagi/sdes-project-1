#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oscillator import Oscillator
from plot import Plot, Sequence
from movie_writer import save_plot

def main():
    #init
    values = [(0, 1), (0.5, 1), (1, 1),
              (1, 2), (2, 2), (5, 2)]
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

    # solve and plot
    for i, plant in enumerate(osc):
        ans = plant.solve(0, 25, 0.01)
        x1.set_data(ans[:,0])
        x2.set_data(ans[:,1])
        figure.set_title(title + '\n' +
                         '$\mu$ = {}, $x$ = {}'.format(plant.mu, plant.x0))
        figure.plot()
        figure.save(i)


if __name__ == "__main__":
    main()

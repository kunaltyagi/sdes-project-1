#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Oscillator class and related tests
"""
import numpy as np
import scipy as sp
# some error
from scipy.integrate import odeint

class Oscillator(object):
    """
    Oscillator class as a wrapper around the given ODE
    """
    def __init__(self, mu=0.01, x0=1., x1=0.):
        self.mu = float(mu)
        self.x0 = float(x0)
        self.x1 = float(x1)
        self.x2 = float(0)

    def next_step_normal(self, Y, t):
        # x2 = x1'
        # Y[1] = x1 = x'
        # Y[0] = x

        # Y[0]' = Y[1]
        # Y[1]' = u(1-Y[0]**2)*Y[1] - Y[0]
        return [Y[1], self.mu*(1-Y[0]**2)*Y[1] - Y[0]]

    def next_time_alt(self, Y, t):
        # Lienard Transformation
        # y = x - x**3/3 - x'/mu
        # y' = x/mu
        # x' = mu(x - x**3/3 - y)

        return [self.mu*(Y[0] - (Y[0]**3)/3 - Y[1]), Y[0]/self.mu]

    def solve(self, begin, end, time_step, alt=False):
        time = np.arange(begin + time_step, end + time_step, time_step)
        get_next_time_step = self.next_time_alt if alt else self.next_step_normal
        solution = sp.integrate.odeint(get_next_time_step,
                                       [self.x0, self.x1], time)
        return solution

    def _no_scipy_solve(self, begin, end, time_step):
        time = np.arange(begin + time_step, end + time_step, time_step)
        states = [(self.x2, self.x1, self.x0)]
        for t in time:
            ans = self.next_step_normal([self.x0, self.x1], t)
            self.x0 += self.x1*time_step
            self.x1 = ans[0]
            self.x2 = ans[1]
            states.append((self.x2, self.x1, self.x0))
        return states

    def __call__(self, *args):
        return self.next_step_normal(args[0], args[1])

def test():
    # trivial test
    no_mu = Oscillator(mu=0)
    ans = no_mu.next_step_normal([1, 0], 9)
    assert ans[0] == 0
    assert ans[1] == -1

    # test by makin each part of the Y[1]' 0
    mu = Oscillator(mu=1)
    ans = mu.next_step_normal([1, 5], 9)
    assert ans[0] == 5
    assert ans[1] == -1
    ans = mu.next_step_normal([-3, 0], 9)
    assert ans[0] == 0
    assert ans[1] == 3

    # test with mu = 1
    unity_mu = Oscillator(mu=1)
    ans = unity_mu.next_step_normal([0, -1], 9)
    assert ans[0] == -1
    assert ans[1] == -1

if __name__ == "__main__":
    test()

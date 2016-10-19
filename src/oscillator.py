#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Oscillator class and related tests
"""
import numpy as np
import scipy as sp

class Oscillator(object):
    """
    Oscillator class as a wrapper around the given ODE
    """
    def __init__(self, mu=0.01, x0=1., x1=0.):
        self.mu = float(mu)
        self.x0 = float(x0)
        self.x1 = float(x1)
        self.x2 = float(0)

    def get_next_time_step(self, Y, t):
        # x2 = x1'
        # Y[1] = x1 = x'
        # Y[0] = x

        # Y[0]' = Y[1]
        # Y[1]' = u(1-Y[0]**2)*Y[1] - Y[0]
        return [Y[1], self.mu*(1-Y[0]**2)*Y[1] - Y[0]]

    def solve(self, begin, end, time_step):
        time = np.arange(begin + time_step, end + time_step, time_step)
        solution = sp.integrate.odeint(self.get_next_time_step,
                                       [self.x0,self.x1], time)
        return solution

    def _no_scipy_solve(self, begin, end, time_step):
        time = np.arange(begin + time_step, end + time_step, time_step)
        states = [(self.x2, self.x1, self.x0)]
        for t in time:
            ans = self.get_next_time_step([self.x0, self.x1], t)
            self.x0 += self.x1*time_step
            self.x1 = ans[0]
            self.x2 = ans[1]
            states.append((self.x2, self.x1, self.x0))
        return states

    def __call__(self, *args):
        return self.get_next_time_step(args[0], args[1])

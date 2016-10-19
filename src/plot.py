#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib as mpl
import mpl.pyplot as plt

class Sequence(object):
    def __init__(self):
        self.color = ''
        self.marker = ''
        self.width = 0
        self.label=''
        self.reset()

    def reset(self):
        self.set_line_width()
        self.set_marker()
        self.set_color()
        self.set_label()

    def set_label(self, label):
        self.label = label

    def set_color(self, color='b'):
        self.color = color

    def set_line_width(self, width=1):
        self.width = width

    def set_marker(self, marker=''):
        self.marker = marker

    def plot(self, data):
        return plt.plot(data, color=self.color, marker=self.marker,
                linestyle=self.linestyle, linewidth=self.width,
                label=self.label)

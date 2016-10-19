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

class Plot(object):
    def __init__(self):
        self.x = {}
        self.y = {}
        self.legend = None
        self.font_size = 0
        self.title = ''

    def reset(self):
        self.set_axis()
        self.set_legend()
        self.set_title()
        self.set_font_size()

    def set_axis(self, x='time', y='magnitude'):
        self.x['label'] = x
        self.y['label'] = y

    def set_title(self, title='Van der Poll Oscillator')
        self.title = title

    def set_legend(self, legend=True):
        self.legend = legend

    def set_font(self, font):
        pass

    def set_font_size(self, size=12):
        self.font_size = size

    def plot(self, sequences):
        fig = plt.figure()
        fig.suptitle(self.title, fontsize=self.font_size)
        mpl.rcParams['font.size'] = self.font_size
        for seq in sequences:
            seq.plot()
        if self.legend:
            plt.legend()
        plt.show()

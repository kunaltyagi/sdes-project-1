#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

class Sequence(object):
    def __init__(self, data, label='random_max'):
        self.fig = None
        self.data = None
        self.color = ''
        self.marker = ''
        self.width = 0
        self.label=''
        self.reset(label=label, data=data)

    def reset(self, label='random_max', data=None):
        self.fig = None
        self.set_line_width()
        self.set_line_style()
        self.set_marker()
        self.set_color()
        self.set_label(label)
        self.set_data(data)

    def set_label(self, label='some_label'):
        self.label = label

    def set_color(self, color='b'):
        self.color = color

    def set_line_width(self, width=1):
        self.width = width

    def set_line_style(self, style='-'):
        self.linestyle = style

    def set_marker(self, marker=''):
        self.marker = marker

    def set_data(self, data):
        self.data = data

    def plot(self, data=None, lim=[-1,-1]):
        if data:
            self.data = data
        if lim == [-1, -1]:
            lim = [0, len(self.data)]
        return plt.plot(self.data[lim[0]:lim[1]], color=self.color,
                        marker=self.marker, linestyle=self.linestyle,
                        linewidth=self.width, label=self.label)

class Plot(object):
    def __init__(self, sequences=None):
        self.label = {}
        self.sequences = sequences
        self.legend = None
        self.font_size = {}
        self.font_type = {}
        self.title = ''
        self.reset()

    def reset(self):
        self.set_axis()
        self.set_legend()
        self.set_title()
        self.set_font_size()
        self.set_font_type()

    def set_axis(self, x='time', y='magnitude'):
        self.label['x'] = x
        self.label['y'] = y

    def set_title(self, title='Van der Poll Oscillator'):
        self.title = title

    def set_legend(self, legend=True):
        self.legend = legend

    def set_font(self, font):
        pass

    def set_font_size(self, data={'label':12, 'title':18, 'legend':12}):
        for key, value in data.items():
            self.font_size[key] = value

    def set_font_type(self, data={'label':'sans',
                'title':'fantasy', 'legend':'monospace'}):
        for key, value in data.items():
            self.font_type[key] = value

    def save(self, name, save_fn):
        save_fn(self.fig, str(name))

    def plot(self, sequences=None, display=False):
        if sequences:
            self.sequences = sequences
        self.fig = plt.figure()
        self.fig.suptitle(self.title, fontsize=self.font_size['title'])
        mpl.rcParams['font.size'] = self.font_size['legend']
        mpl.rcParams['font.family'] = self.font_type['legend']

        for seq in self.sequences:
            seq.plot()
        if self.legend:
            plt.legend(loc=3)

        mpl.rcParams['font.size'] = self.font_size['label']
        mpl.rcParams['font.family'] = self.font_type['label']
        for axis in ['x', 'y']:
            getattr(plt, axis + 'label')(self.label[axis])

        mpl.rcParams['font.family'] = self.font_type['title']
        # plt.title(self.title, fontdict={'fontsize': self.font_size['title']})
        if display:
            self.fig.show()

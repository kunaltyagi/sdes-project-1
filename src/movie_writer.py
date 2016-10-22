#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
from matplotlib import animation as anim
from matplotlib import pyplot as plt


class MovieCreator(object):
    def __init__(self, fps=5, title="matplotlib.animation",
                 artist="Kunal Tyagi", comment=""):
        FFMpegWriter = anim.writers['ffmpeg']
        metadata = {title=title, artist=artist, comment=comment}
        self.writer = FFMpegWriter(fps=fps, metadata=metadata)

    def creator(file_name, figure, plot_editor, init_func, frames, dpi=72):
        with self.writer.saving(figure, file_name, dpi):
            init_func()
            for i in range(0, frames):
                plot_editor()
                self.writer.grab_frame()

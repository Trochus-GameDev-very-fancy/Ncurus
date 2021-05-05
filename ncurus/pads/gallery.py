# gallery.py

import curses

from src.img import BaseImage
from ..type import ConsoleEffect, CursesWin
from .pad import Pad


class Gallery(Pad):
    def __init__(self, win: CursesWin):
        self.win = win

    def show(self, img: BaseImage) -> ConsoleEffect:
        for y, line in enumerate(img):
            for x, char_color in enumerate(line):
                self.win.addch(y, x,
                               "█",
                               curses.color_pair(int(char_color)))

        self.refresh()


import curses

from ncurus.img import BaseImage
from ..type import ConsoleEffect, CursesWin
from .pad import Pad


class Gallery(Pad):
    """Encapsulate a gallery which can show various images."""

    def __init__(self, win: CursesWin):
        self.win = win

    def show(self, img: BaseImage) -> ConsoleEffect:
        """Display given img in self.win. Images exceeding the width and
        height of the window are cut off.
        """
        # TODO: Make compatibitly for ASCII image.

        truncated_img = img[:self.max_y]
        for y, line in enumerate(truncated_img):
            for x, char_color in enumerate(line[:self.max_x]):
                self.win.addch(y, x,
                               "█",
                               curses.color_pair(int(char_color)))

        self.refresh()

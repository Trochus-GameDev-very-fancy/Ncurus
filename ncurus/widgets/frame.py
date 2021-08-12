
from .widget import Widget


class Frame(Widget):

    def __init__(self, win):
        self.win = win

    def show(self, img):
        for y, line in enumerate(img):
            for x, char in enumerate(line):
                self.win.addstr(y,
                                x,
                                char)

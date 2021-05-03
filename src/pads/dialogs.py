# dialogs.py

from visualdialog import DialogBox

from .pad import Pad
from ..type import ConsoleEffect, CursesWin


class Dialogs(Pad, DialogBox):
    def __init__(self, win: CursesWin):
        self.win = win
        # self.win.bkgdset("b")

        self.textbox = DialogBox(0, 0, 20, 6, "TextBox")

    def char_by_char(self, *args, **kwargs) -> ConsoleEffect:
        self.textbox.char_by_char(self.win, *args, **kwargs)

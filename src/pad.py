# pad.py

from typing import NoReturn

from visualdialog import DialogBox

from .type import ConsoleEffect, CursesWin


class Pad:
    """Encapsulate a pad."""
    def __init__(self, win: CursesWin):
        self.win = win

    def box(self) -> ConsoleEffect:
        self.win.box()

    def clear(self) -> ConsoleEffect:
        self.win.clear()

    def refresh(self) -> ConsoleEffect:
        self.win.refresh()

    def update(self):
        pass


class Gallery(Pad):
    def __init__(self, win: CursesWin):
        self.win = win
        # self.win.bkgdset("t")

    def update(self) -> ConsoleEffect:
        pass


class Dialogs(Pad, DialogBox):
    def __init__(self, win: CursesWin):
        self.win = win
        # self.win.bkgdset("b")

        self.textbox = DialogBox(0, 0, 20, 6, "TextBox")

    def update(self) -> ConsoleEffect:
        pass

    def char_by_char(self, *args) -> ConsoleEffect:
        self.textbox.char_by_char(self.win, *args)

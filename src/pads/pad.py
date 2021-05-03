# pad.py

from ..type import ConsoleEffect, CursesWin


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

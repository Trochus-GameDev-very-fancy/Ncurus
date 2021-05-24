
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

    @property
    def max_x(self) -> int:
        """Return number of column of windows."""
        return self.win.getmaxyx()[1]

    @property
    def max_y(self) -> int:
        """Return number of line of windows."""
        return self.win.getmaxyx()[0]

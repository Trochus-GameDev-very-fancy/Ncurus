
from ..type import ConsoleEffect, CursesWin, WidgetProtocol


class DynamicPos:

    def __set__(self, obj: WidgetProtocol, value: int) -> None:
        """"""
        obj._width = value
        obj.win.resize(obj.height, obj.width)


class Widget:
    """Encapsulate a widget. A widget manages positions and dimensions
    of a ``curses`` window object.
    """

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

    @property
    def half_y(self) -> int:
        """Return half of the total height window."""
        return self.max_y // 2

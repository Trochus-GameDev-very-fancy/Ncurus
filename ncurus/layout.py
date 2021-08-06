"""Contains objects related to layout."""

__all__ = ["Layout"]

import curses
from typing import Callable, Literal, NoReturn, Optional, Tuple

from .deque import WidgetList
from .type import ConsoleEffect, CursesWin, WidgetProtocol
from .widgets import Dialogs, Gallery, Widget


def calc(base, new):
    return base*10 // new


class Layout:
    """Encapsulate a layout to manage a set of widget efficiently."""

    def __init__(self, win: CursesWin):
        self.win = win
        self.widgets = WidgetList()

        self.resize()

    @property
    def dimensions(self) -> Tuple[int, int]:
        """Returns a tuple composed of ``self.width`` and ``self.height``."""
        return self.width, self.height

    def disp_widget(self,
                    widget: WidgetProtocol,
                    purcent_x: int,
                    purcent_y: int,
                    *args,
                    **kwargs):
        """"""
        nlines = calc(self.height, purcent_x)
        ncols = calc(self.width, purcent_y)

        derivate_win = self.win.subwin(nlines, ncols, )

        widget = Widget(*args, **kwargs)

        self.widgets.append(widget, purcent_x, purcent_y)

        return widget()

    def refresh(self) -> None:
        """Calls ``routine`` method of each widgets in ``self.widgets``."""
        self.resize()

        for widget, (dim_x, dim_y) in self.widgets:
            widget.width = self.width*10 // dim_x
            widget.height = self.height*10 // dim_y 

            widget.routine()

    def resize(self) -> None:
        """Sets ``self.width`` and ``self.heigth`` to current size of terminal."""
        self.width, self.heigth = os.get_terminal_size()
        self.refresh()

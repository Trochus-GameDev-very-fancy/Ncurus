
import curses
from typing import Callable, Literal, NoReturn, Optional, Tuple

from .type import ConsoleEffect, CursesWin
from .widgets import Dialogs, Gallery, Widget


Dimension = Literal["full", "half"]
Position = Literal["up", "down"]


class RoutineHandler:

    def __get__(self, obj: "Layout", objtype=None) -> CursesWin:
        obj.routine()
        return obj.stdscr


class Layout(Widget):
    """Encapsulate a layout to manage a set of widget more efficiently."""
    stdscr = RoutineHandler()

    def __init__(self,
                 win: CursesWin,
                 *,
                 offsetting_y: int = 0,
                 side_borders_width=1):
        self.stdscr = win  #  Catch original win.

        max_y, max_x = win.getmaxyx()

        self.win = win.subwin(max_y - side_borders_width*2,
                              max_x - side_borders_width*2,
                              side_borders_width,
                              side_borders_width)

        self.offsetting_y = offsetting_y
        self.side_borders_width = side_borders_width

        self.deriv = self.win.subwin

    def disp_widget(self,
                    widget: Widget,
                    dimension: Dimension,
                    position: Optional[Position] = None,
                    *args,
                    **kwargs) -> Widget:
        """Return an instance of given ``widget`` class.

        The ``curse`` window object that passed to ``widget``initializer
        is create according given ``dimension`` and ``position``.
        """
        offsetting_y = self.offsetting_y
        side_borders_width = self.side_borders_width

        def calc_coord(dim: Dimension, pos: Position) -> Tuple[int]:
            if dim == "full":
                return (side_borders_width,
                        side_borders_width)
            elif dim == "half" and pos == "up":
                return (self.half_y + offsetting_y,
                        self.max_x,
                        side_borders_width,
                        side_borders_width)
            elif dim == "half" and pos == "down":
                return (self.half_y + 2 + offsetting_y,
                        side_borders_width)
            else:
                raise ValueError()

        win = self.deriv(*calc_coord(dimension, position))

        return widget(win, *args, **kwargs)


import curses
import textwrap
from typing import Any, Callable, Dict, List, Literal, Optional, Tuple, Union

from ..input import iterkey
from ..type import ConsoleEffect, CursesColor, CursesKey, CursesWin
from .widget import Widget


Justify = Union[Callable[[int], str],
                Callable[[str, int], str]]


class TextPad(Widget):
    """"Encapsulate a textpad."""
    margin_top = 1
    margin_side = 3

    def __init__(self,
                 win: CursesWin,
                 title: Optional[str] = None,
                 previous_key: CursesKey = curses.KEY_UP,
                 next_key: CursesKey = curses.KEY_DOWN,
                 end_key: CursesKey = "\n",
                 color_pair_nb: int = 0):
        self.win = win

        max_y, max_x = win.getmaxyx()

        self.char_per_line = max_x - 2*self.margin_side
        self.line_per_screen = max_y - 4*self.margin_top

        self.textbox = self.make_textbox(win)

        self.previous_key, self.next_key = previous_key, next_key
        self.end_key = end_key

        self.color_pair_nb = color_pair_nb

    def make_textbox(self, win: CursesWin) -> CursesWin:
        """Return a subwin from given window dedicates to display text.

        :raises ValueError: if ``self.line_per_screen`` <= 0
        :raises ValueError: if ``self.char_per_line`` <= 0
        """
        if self.line_per_screen <= 0:
            raise ValueError(f"textpad height must be superior to 0")
        elif self.char_per_line <= 0:
            raise ValueError(f"textpad width must be superior to 0")
        else:
            return self.win.derwin(self.line_per_screen,
                                   self.char_per_line,
                                   self.margin_top*2,
                                   self.margin_side)

    def show(self,
             text: str,
             *,
             justify: Justify = lambda x: x) -> ConsoleEffect:
        """Display a scrollable textbox until a key contained in
        ``self.pass_keys`` was pressed.
        """
        lines = self.wrap(text, justify)
        lines_nb = len(lines)

        cursor = 0
        cursor_max_y = lines_nb - self.line_per_screen

        self.draw_border()

        for key in iterkey(self.win, method="get_wch"):
            if key == self.end_key and cursor >= cursor_max_y:
                break
            else:
                if lines_nb <= self.line_per_screen:
                    self.display_line_by_line(lines)
                else:
                    if key == self.previous_key:
                        cursor = max(0, cursor - 1)
                    elif key == self.next_key:
                        cursor = min(cursor_max_y, cursor + 1)

                    lines_selection = lines[cursor:][:self.line_per_screen]
                    self.display_line_by_line(lines_selection)

    def display_line_by_line(self, lines: List[str]) -> ConsoleEffect:
        """Display given lines one by one. Clear screen before and
        refresh it after.
        """
        self.textbox.clear()

        for y, line in enumerate(lines):
            self.textbox.addstr(y, 0,
                                line,
                                curses.color_pair(self.color_pair_nb))

        self.textbox.refresh()

    def draw_border(self, *, border: bool = True) -> ConsoleEffect:
        """Draw border arround window."""
        if border:
            self.win.border("\\",
                            "\\",
                            "~",
                            "~",
                            "+",
                            "+",
                            "+",
                            "+")
            self.win.refresh()

    def wrap(self,
             text: str,
             justify: Union[Callable[[int], str],
                            Callable[[str, int], str]]) -> Tuple[str]:
        """Return given texte wrapped."""
        lines = textwrap.wrap(text, self.char_per_line)

        return tuple(justify(line, self.char_per_line) for line in lines)

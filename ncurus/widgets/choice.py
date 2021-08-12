
import curses
import curses.textpad
from typing import Any, Generator, Iterable, Optional, Tuple

from visualdialog import DialogBox

from ..core import TextAttr, iterkey
from ..type import CursesKey, CursesWin


Choices = Iterable[Tuple[str, Any]]


class ChoiceBox(DialogBox):
    """This class provides methods and attributs to manage a choice box.

    Base :class:`DialogBox`.
    """
    def __init__(self, *args, **kwargs):
        """Initializes instance of :class:`ChoiceBox`."""
        super().__init__(*args, **kwargs)

        self.choice_pos_y = self.end_indicator_pos_y + 3

        self.previous_key: CursesKey = "q"
        self.next_keys: CursesKey = "d"

    def give_choice(self,
                    win: CursesWin,
                    choices: Choices,
                    selected_colors_pair_nb: int = 0,
                    other_colors_pair_nb: int = 0) -> Any:
        """Returns the value correspond to choosed choice by user cursor.

        :param win: ``curses`` window object on which the method will
            have effect. If omitted, ``self.global_win`` is chosen.

        :param choices: an iterable of tuple composed of a choice and the value
            that will be returned if it choosen.

        :param selected_colors_pair_nb: Number of the curses color pair that
            will be used to color the choice under the cursor. The number zero
            corresponding to the pair of white color on black
            background initialized by ``curses``). This defaults to
            ``0``.

        :param other_colors_pair_nb: Number of the curses color pair that
            will be used to color choices which are not under the cursor. The
            number zero corresponding to the pair of white color on black
            background initialized by ``curses``). This defaults to
            ``0``.
        """
        for cursor in self._cursor_choice(win, len(choices) - 1):
            self._display_choice(win,
                                 choices,
                                 selected_colors_pair_nb,
                                 other_colors_pair_nb,
                                 cursor)
            win.refresh()

        return choices[cursor][1]

    def _display_choice(self,
                        win: CursesWin,
                        choices: Choices,
                        selected_colors_pair_nb: int,
                        other_colors_pair_nb: int,
                        hightlighted_choice: Optional[int] = None) -> None:
        """Displays given choices and their frame box."""
        side_borders_height = 2

        choice_height = sum(len(choice) + side_borders_height*2
                            for choice, _ in choices)
        start_x = (self.height - choice_height) // 2

        offsetting_x = 1
        for index, (choice, _) in enumerate(choices):
            curses.textpad.rectangle(win,
                                     self.choice_pos_y - 1,
                                     start_x + offsetting_x + 1,
                                     self.choice_pos_y + 1,
                                     start_x
                                        + offsetting_x
                                        + len(choice)
                                        + 2*side_borders_height)

            offsetting_x += side_borders_height

            attr = (curses.color_pair(selected_colors_pair_nb)
                    if index == hightlighted_choice
                    else curses.color_pair(other_colors_pair_nb))

            with TextAttr(win, attr):
                win.addstr(self.choice_pos_y,
                        self.pos_x + start_x + offsetting_x,
                        choice)

            offsetting_x += side_borders_height + len(choice)

    def _cursor_choice(self,
                       win: CursesWin,
                       cursor_max: int) -> Generator[None, int, None]:
        """Leaves the user until the enter key is pressed and returns the
        current cursor position as an integer.
        """
        cursor = 0

        for key in iterkey(win, exit_keys=("\n",)):
            if key == self.previous_key:
                cursor = max(0, cursor - 1)
            elif key == self.next_keys:
                cursor = min(cursor_max, cursor + 1)

            yield cursor

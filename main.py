
from ncurus.widgets import TextPad, Gallery, Dialogs
from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
import ncurus

from examples import scene


@ncurus.startup()
@ncurus.process_scene(scene.execute)
def main(win):
    layout = Layout(win)

    gallery = layout.disp_widget(Gallery, "half", "up")
    dialogs = layout.disp_widget(Dialogs, "half", "down")

    layout.draw_borders(sep_line=True)

    db_one = dialogs.disp_box("One")
    db_two = dialogs.disp_box("Two")

    return gallery, db_one, db_two


@ncurus.startup(smooth_crash=True)
def main2(win):
    layout = Layout(win)

    sign = layout.disp_widget(TextPad, "half", "up", color_pair_nb=4)
    sign.show("Il était une foo"*20, justify=str.ljust)

    layout.win.getch()


@ncurus.startup(smooth_crash=True)
def main3(win):
    choices = (
        ("Foo", 1),
        ("Bar", 2),
        ("Foobar2000", 3)
    )

    _, max_x = win.getmaxyx()

    dialog_box = ncurus.ChoiceBox(1, 1,
                                  max_x - 2, 5,
                                 "First",
                                 1)

    dialog_box.confirm_keys.append("\n")
    dialog_box.char_by_char("The first choice", win)

    dialog_box.give_choice(win, choices, 2, 6)


if __name__ == "__main__":
    main3()

    # TODO: Add param boolean ``no_input`` to visualdialog

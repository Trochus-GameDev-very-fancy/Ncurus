
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


if __name__ == "__main__":
    main2()

    #TODO: Implement ``user_decor`` decorator.

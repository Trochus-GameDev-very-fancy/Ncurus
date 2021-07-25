
from ncurus.pads import TextPad
from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
import ncurus

from examples import scene


@ncurus.startup
@ncurus.process_scene(scene.execute)
def main(win):
    layout = Layout(win)
    gallery, dialogs = layout.disp_widgets(offsetting_y=0)

    layout.draw_borders(sep_line=True)

    dialogs.one = dialogs.make_box("One")
    dialogs.two = dialogs.make_box("Two")

    return gallery, dialogs.one, dialogs.two


@ncurus.startup(smooth_crash=True)
def main2(win):
    def make_sign(win, *args, **kwargs):
        return TextPad(win, *win.getmaxyx())

    sign = make_sign(win, color_pair_nb=4)
    sign.show("Il était une foo"*20, justify=str.ljust)


if __name__ == "__main__":
    main2()

    # user_decor decorator

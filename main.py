# main.py

from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
from ncurus.pads import Dialogs, Gallery
import ncurus

from examples import scene


@ncurus.startup
def main(win):
    layout = Layout(win)
    top_win, bottom_win = layout.divide_window(4)
    gallery = Gallery(top_win)
    dialogs = Dialogs(bottom_win)

    dialogs.one = dialogs.box_factory("One")
    dialogs.two = dialogs.box_factory("Two")

    layout.routine()

    scene.execute(gallery, dialogs.one, dialogs.two)


if __name__ == "__main__":
    main()
    #TODO: make dialog box responsive.

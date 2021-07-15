
from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
import ncurus

from examples import scene


@ncurus.startup
@ncurus.process_scene(scene.execute)
def main(win):
    layout = Layout(win)
    gallery, dialogs = layout.disp_widgets(offsetting_y=4)

    layout.draw_borders()

    dialogs.one = dialogs.box_factory("One")
    dialogs.two = dialogs.box_factory("Two")

    return gallery, dialogs.one, dialogs.two


if __name__ == "__main__":
    main()
    #TODO: make dialog box responsive.


from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
import ncurus

from examples import scene

import functools
from typing import Callable, Optional


def use_scene(scene: Callable) -> Callable:
    """"""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Optional:
            return scene(*func(*args, **kwargs))

        return wrapper
    return decorator


@ncurus.startup
@use_scene(scene.execute)
def main(win):
    layout = Layout(win)
    gallery, dialogs = layout.disp_widgets(offsetting_y=4)

    dialogs.one = dialogs.box_factory("One")
    dialogs.two = dialogs.box_factory("Two")

    return gallery, dialogs.one, dialogs.two


if __name__ == "__main__":
    main()
    #TODO: make dialog box responsive.

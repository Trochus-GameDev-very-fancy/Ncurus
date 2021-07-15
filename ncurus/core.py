
from typing import Callable, Optional


def process_scene(scene: Callable) -> Callable:
    """Process scene function and return its result."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Optional:
            return scene(*func(*args, **kwargs))

        return wrapper
    return decorator

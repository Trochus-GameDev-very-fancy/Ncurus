# img.py

from typing import Any, Callable, Iterable, Literal, TextIO, Tuple, Union


class BaseImage:
    """An interface for image.

    Initializator takes an iterable of strings or a text mode file in
    parameter.
    """
    sep: str = "---\n"

    def __init__(self, iterable: Union[Iterable[str], TextIO]):
        self.content = self.is_valid(iterable)

        self.width = max(iterable, key=len)
        self.height = len(iterable)

    def __iter__(self) -> Iterable[str]:
        return iter(self.content)

    def is_valid(self,
                 iterable: Iterable[str],
                 key: Callable[[str], Any]) -> Tuple[str]:
        """Return a parsed iterable of string."""
        for index, line in enumerate(iterable):
            for position, char in enumerate(line):
                if not key(char):
                    raise ValueError(f"{char} is not a digit "
                                     f"(line {index}, position {position})")

        return tuple(iterable)

    @classmethod
    def from_path(cls, path: str, obj: "BaseImage") -> "BaseImage":
        """Return an image object from content of given file path."""
        content = open(path).read()

        try:
            start, content, end = content.split(cls.sep)
        except ValueError:
            raise ValueError("Invalid image format")

        return obj(content.rstrip("\n").split("\n"))


class ANSI(BaseImage):
    """Encapsulate an ANSI image.

    Example of valid format
    -----------------------
    >>> ANSI(["525",
              "313",
              "525"])
    """
    def is_valid(self, iterable: Iterable[str]) -> Tuple[str]:
        key = lambda char: char in "0123456"

        return BaseImage.is_valid(self, iterable, key=key)

    @staticmethod
    def from_path(path: str):
        return BaseImage.from_path(path, ANSI)


class ASCII(BaseImage):
    """Encapsulate an ASCII image.

    Example of valid format
    -----------------------
    >>> ASCII(["-.-",
               " I ",
               "o o"])
    """
    def is_valid(self, iterable: Iterable[str]) -> Tuple[str]:
        key = lambda char: True

        return BaseImage.is_valid(self, iterable, key=key)

    @staticmethod
    def from_path(path: str):
        return BaseImage.from_path(path, ASCII)

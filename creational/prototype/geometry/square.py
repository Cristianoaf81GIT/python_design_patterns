from typing import Self
from copy import copy
from interfaces import Shape #pyright: ignore

class Square(Shape):

    def __init__(self, points: list[int], width: int, height: int) -> None:
        super().__init__(points, width, height)
        self._width = width
        self._height = height
        self._points = points

    def clone(self) -> Self:
        return copy(self)

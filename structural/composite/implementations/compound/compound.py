from typing import List
from interfaces import Graphic  # pyright: ignore


class CompoundGraphic(Graphic):

    _children: List[Graphic] = []

    def add(self, child: Graphic) -> None:
        self._children.append(child)

    def remove(self, child: Graphic) -> None:
        self._children.remove(child)

    def move(self, x: int, y: int) -> None:
        [child.move(x, y) for child in self._children]

    def draw(self) -> None:
        [child.draw() for child in self._children]

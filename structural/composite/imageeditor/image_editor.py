from typing import List
from implementations import CompoundGraphic, Dot, Circle  # noqa # pyright: ignore
from interfaces import Graphic  # pyright: ignore


class ImageEditor:

    all: CompoundGraphic

    def load(self) -> None:
        self.all = CompoundGraphic()
        self.all.add(Dot(1, 2))
        self.all.add(Circle(5, 3, 10))

    def group_selected(self, components: List[Graphic]) -> None:  # noqa
        group = CompoundGraphic()
        for comp in components:
            group.add(comp)
            self.all.remove(comp)
        self.all = group
        self.all.draw()

from .TreeType import TreeType
from typing import Any


class Tree:
    x: int
    y: int
    tree_type: TreeType

    def __init__(self, x: int, y: int, type: TreeType) -> None:
        self.x = x
        self.y = y
        self.tree_type = type
        print(
            f"tree name = {type.name}, tree pos = x:{x},y:{y}, tree color = {type.color}"
        )

    def draw(self, canvas: Any) -> None:
        self.tree_type.draw(canvas)

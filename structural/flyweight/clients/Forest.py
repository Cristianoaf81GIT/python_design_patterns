from typing import Any, Union
from flyweight import TreeType  # pyright: ignore
from flyweight import Tree  # pyright: ignore
from factory import TreeFactory  # pyright: ignore


class Forest:
    trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        type: Union[TreeType, None] = TreeFactory.get_tree_type(name, color, texture)
        if type is not None:
            tree = Tree(x, y, type)
            self.trees.append(tree)
        else:
            print(f"type: {type} was not created...")

    def draw(self, canvas: Any) -> None:
        [tree.draw(canvas) for tree in self.trees]

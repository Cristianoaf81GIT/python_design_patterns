from typing import Union
from flyweight import TreeType  # pyright: ignore


class TreeFactory:
    tree_types: list[TreeType] = []

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> Union[TreeType, None]:
        type: Union[TreeType, None] = None
        for tree_type in TreeFactory.tree_types:
            if (
                tree_type is not None
                and tree_type.name == name
                and tree_type.color == color
                and tree_type.texture == texture
            ):
                type = tree_type
                # print("found type")

        if type is None:
            type = TreeType(name=name, color=color, texture=texture)
            TreeFactory.tree_types.append(type)

        return type

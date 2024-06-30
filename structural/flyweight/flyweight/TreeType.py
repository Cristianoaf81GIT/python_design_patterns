from typing import Any


class TreeType:
    name: str
    color: str
    texture: str

    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas: Any) -> None:
        print(f"drawing TreeType on canvas {canvas}")

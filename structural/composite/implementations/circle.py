import turtle
from .dot import Dot


class Circle(Dot):

    radius: float = 0.0

    def __init__(self, x: int, y: int, radius: float) -> None:
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        print(f"drawing {Circle.__qualname__}!")
        t = turtle.Turtle()
        t.circle(self.radius)

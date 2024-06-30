import turtle
from interfaces import Graphic  # pyright: ignore


class Dot(Graphic):

    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.y += y
        self.x += x
        print(f"moving: {Dot.__name__} X={self.x} , Y={self.y}")

    def draw(self) -> None:
        print(f"drawing a {Dot.__name__}!")
        t = turtle.Turtle()
        t.dot(self.x + self.y)

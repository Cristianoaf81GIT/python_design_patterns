from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

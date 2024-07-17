from abc import ABCMeta, abstractmethod
from typing import Self
from dataclasses import dataclass

@dataclass
class Shape(metaclass=ABCMeta):
    
    _points: list[int]
    _width: int
    _height: int 
    
    def __init__(self, points: list[int], width: int, height: int) -> None:
        self._width = width, #pyright: ignore
        self._height = height
        self._points = points
    
    @property 
    def get_points(self) -> list[int]:
        return self._points 

    @property 
    def get_width(self) -> int:
        return self._width

    @property
    def get_height(self) -> int:
        return self._height

    def set_points(self, points: list[int]) -> None:
        self._points = points

    def set_width(self, width: int) -> None:
        self._width = width
    
    def set_height(self, height: int) -> None:
        self._height = height

    @abstractmethod
    def clone(self) -> Self:
        pass



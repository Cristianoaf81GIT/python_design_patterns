from abc import ABCMeta, abstractmethod
from . shape import Shape

class ShapeRegister(metaclass=ABCMeta):

    _shapes: dict[str, Shape]
    
    @abstractmethod
    def add_shape(self, id: str, shape: Shape) -> None:
        pass

    @abstractmethod
    def get_shape_by_id(self, id: str) -> Shape | None:
        pass



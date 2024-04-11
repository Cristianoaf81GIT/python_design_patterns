from abc import ABCMeta, abstractmethod
from . house_interface import House

class AbsctractHouseBuilder(metaclass=ABCMeta):
    
    @abstractmethod
    def build_walls(self, walls: int) -> None:
        pass

    @abstractmethod 
    def build_doors(self, doors: int) -> None:
        pass

    @abstractmethod
    def build_window(self, windows: int) -> None:
        pass

    @abstractmethod
    def build_roof(self, has_roof: bool) -> None:
        pass

    @abstractmethod
    def build_garage(self, has_garage: bool) -> None:
        pass

    @abstractmethod
    def build_swimming_pool(self, has_swimming_pool: bool) -> None:
        pass

    @abstractmethod
    def get_result(self) -> House:
        pass



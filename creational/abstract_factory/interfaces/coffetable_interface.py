from abc import ABCMeta, abstractmethod

class CoffeTable(metaclass=ABCMeta):
    
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def cover(self) -> None:
        pass

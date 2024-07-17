from abc import ABCMeta, abstractmethod

class Sofa(metaclass=ABCMeta):

    @abstractmethod
    def seaters(self) -> int:
        pass
    
    @abstractmethod
    def seat(self) -> None:
        pass

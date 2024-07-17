from abc import ABCMeta, abstractmethod

class Transport(metaclass=ABCMeta):
    
    @abstractmethod
    def deliver(self) -> None:
        pass


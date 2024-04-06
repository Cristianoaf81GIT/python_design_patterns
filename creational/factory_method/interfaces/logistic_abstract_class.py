from abc import ABCMeta, abstractmethod
from . import Transport

class AbstractLogistic(metaclass=ABCMeta):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass 

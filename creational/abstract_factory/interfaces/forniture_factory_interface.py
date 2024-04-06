from abc import ABCMeta, abstractmethod
from . sofa_interface import Sofa
from . coffetable_interface import CoffeTable
from . chair_interface import Chair

class AbstractFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffe_table(self) -> CoffeTable:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass 

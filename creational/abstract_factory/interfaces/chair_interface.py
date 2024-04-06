from abc import ABCMeta, abstractmethod

class Chair(metaclass=ABCMeta):
    
    @abstractmethod 
    def has_legs(self) -> bool:
        pass 

    @abstractmethod
    def sit_on(self) -> None:
        pass 


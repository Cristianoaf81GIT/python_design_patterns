from abc import ABCMeta, abstractmethod


class AdapterInterface(metaclass=ABCMeta):

    @abstractmethod
    def exec_operation(self) -> None:
        pass

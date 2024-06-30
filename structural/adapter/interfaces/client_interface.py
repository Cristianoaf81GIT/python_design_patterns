from abc import ABCMeta, abstractmethod
from .adapter_interface import AdapterInterface


class ClientInterface(metaclass=ABCMeta):

    _adapter: AdapterInterface

    def __init__(self, adapter: AdapterInterface) -> None:
        self._adapter = adapter

    @abstractmethod
    def exec_operation(self) -> None:
        pass

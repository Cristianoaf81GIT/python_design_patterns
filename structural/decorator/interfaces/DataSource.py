from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class DataSource(metaclass=ABCMeta):

    @abstractmethod
    def write_data(self, data: Any) -> None:
        pass

    @abstractmethod
    def read_data(self) -> None:
        pass

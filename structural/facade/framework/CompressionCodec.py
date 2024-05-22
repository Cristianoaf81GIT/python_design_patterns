from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True)
class CompressionCodec(metaclass=ABCMeta):

    @abstractmethod
    def get_bit_rate(self) -> int:
        pass

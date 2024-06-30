from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from models import Channel  # pyright: ignore


@dataclass
class DeviceInterface(metaclass=ABCMeta):

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> float:
        pass

    @abstractmethod
    def set_volume(self, percent: float) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> str:
        pass

    @abstractmethod
    def set_channel(self, channel: Channel) -> None:
        pass

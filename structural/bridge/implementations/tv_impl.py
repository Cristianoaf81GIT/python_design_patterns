from interfaces import DeviceInterface  # pyright: ignore
from models import Channel  # pyright: ignore


class Tv(DeviceInterface):

    _enable: bool = False
    _volume: float = 0.25
    _channel: Channel = Channel(frequency=92, name="LifeInFarm")

    def is_enabled(self) -> bool:
        return self._enable

    def enable(self) -> None:
        self._enable = True

    def disable(self) -> None:
        self._enable = False

    def get_volume(self) -> float:
        return self._volume

    def set_volume(self, percent: float) -> None:
        self._volume = percent

    def get_channel(self) -> str:
        return self._channel.channel_name

    def set_channel(self, channel: Channel) -> None:
        self._channel = channel

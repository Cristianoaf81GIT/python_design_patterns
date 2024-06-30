from dataclasses import dataclass


@dataclass
class Channel:

    _frequency: float
    channel_name: str

    def __init__(self, frequency: float, name: str) -> None:
        self._frequency = frequency
        self.channel_name = name

    def get_frequency(self) -> float:
        return self._frequency

    def set_frequency(self, frequency: float) -> None:
        self._frequency = frequency

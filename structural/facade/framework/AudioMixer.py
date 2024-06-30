from dataclasses import dataclass
from typing import Any
from .BitRateReader import BitRateReader


@dataclass(kw_only=True)
class AudioMixer:

    @classmethod
    def fix(cls, data: BitRateReader) -> Any:
        print(f"fixing audio from file: {data.get_file()}")
        return cls

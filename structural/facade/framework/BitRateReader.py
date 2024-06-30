from __future__ import annotations
from dataclasses import dataclass
from .CompressionCodec import CompressionCodec


@dataclass(kw_only=True)
class BitRateReader:

    file_name: str

    def __init__(self, filename: str) -> None:
        self.file_name = filename

    def read(self, source_codec: CompressionCodec) -> None:
        print(
            f"reading bit data from {self.file_name}, at:{source_codec.get_bit_rate()} bits per Seconds"  # noqa
        )

    def convert(
        self, buffer: BitRateReader, destination_codec: CompressionCodec
    ) -> None:  # pyright: ignore
        print(
            f"converting buffer data {buffer.get_file()}, at:{destination_codec.get_bit_rate()} bits per Seconds"  # noqa
        )

    def get_file(self) -> str:
        return self.file_name

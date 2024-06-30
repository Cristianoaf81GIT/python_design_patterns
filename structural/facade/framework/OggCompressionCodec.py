from .CompressionCodec import CompressionCodec
from dataclasses import dataclass


@dataclass(kw_only=True)
class OggCompressionCodec(CompressionCodec):

    def get_bit_rate(self) -> int:
        return 123

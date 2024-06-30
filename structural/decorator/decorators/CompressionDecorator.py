from typing import Any
import base64
import zlib
from .DataSourceDecorator import DataSourceDecorator
from interfaces import DataSource  # pyright: ignore


class CompressionDecorator(DataSourceDecorator):

    _zipped_data: bytes

    def __init__(self, data_source: DataSource) -> None:
        self._wrappee = data_source

    def read_data(self) -> None:
        uncompressed = eval(zlib.decompress(self._zipped_data))
        print(f"uncompressed: {uncompressed.decode('utf-8', errors='ignore')}")  # noqa

    def write_data(self, data: Any) -> None:
        bytes_data = bytes(str(data), "utf-8")
        self._zipped_data = zlib.compress(bytes_data)
        data = base64.b64encode(self._zipped_data)
        self._wrappee.write_data(data)

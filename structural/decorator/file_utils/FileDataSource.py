from typing import Any
from interfaces import DataSource  # pyright: ignore


class FileDataSource(DataSource):

    _file_name: str

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def write_data(self, data: Any) -> None:
        with open(self._file_name, "+wb") as writer:
            str_data = str(data)
            byte_data = bytes(str_data, encoding="utf-8")
            writer.write(byte_data)

    def read_data(self) -> None:
        with open(self._file_name, "rb") as reader:
            data = reader.read()
            print(f"{data}")

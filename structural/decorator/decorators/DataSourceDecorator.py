from typing import Any
from interfaces import DataSource  # pyright: ignore


class DataSourceDecorator(DataSource):

    _wrappee: DataSource

    def __init__(self, data_source: DataSource) -> None:
        self._wrappee = data_source

    def write_data(self, data: Any) -> None:
        self._wrappee.write_data(data)

    def read_data(self) -> None:
        self._wrappee.read_data()

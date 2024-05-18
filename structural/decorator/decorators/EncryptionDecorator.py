from typing import Any
import rsa
from .DataSourceDecorator import DataSourceDecorator
from interfaces import DataSource  # pyright: ignore


class EncryptionDecorator(DataSourceDecorator):

    _public_key, _private_key = rsa.newkeys(nbits=512)
    _enc_data: bytes

    def __init__(self, data_source: DataSource) -> None:
        super().__init__(data_source)
        self._wrappee = data_source

    def write_data(self, data: Any) -> None:
        str_data = str(data)
        byte_data = bytes(str_data, encoding="utf-8")
        self._enc_data = rsa.encrypt(byte_data, self._public_key)
        print(f"saving data encripted: {str(self._enc_data)[:6]} ... too long")
        self._wrappee.write_data(self._enc_data)

    def read_data(self) -> None:
        dec_data = rsa.decrypt(self._enc_data, self._private_key)
        print(f"decripted data: {dec_data}")
        self._wrappee.read_data()

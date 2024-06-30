from typing import Dict
from file_utils import FileDataSource  # pyright: ignore
from decorators import (
    CompressionDecorator,
    EncryptionDecorator,
)  # pyright: ignore #noqa


def app_main() -> None:
    source = FileDataSource(file_name="file.dat")

    salary_data: Dict[str, float] = {
        "hr": 4300.24,
        "manager": 12000,
        "developer": 15000,
    }

    source.write_data(data=salary_data)

    compressed = CompressionDecorator(source)
    compressed.write_data(data=salary_data)

    encripted = EncryptionDecorator(compressed)
    encripted.write_data(data=salary_data)

    encripted.read_data()

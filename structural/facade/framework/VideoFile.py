from dataclasses import dataclass


@dataclass(kw_only=True)
class VideoFile:

    _file_name: str

    def __init__(self, filename: str) -> None:
        self._file_name = filename

    def get_file_name(self) -> str:
        return self._file_name

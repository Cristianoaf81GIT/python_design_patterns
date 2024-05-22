from dataclasses import dataclass


@dataclass(kw_only=True)
class File:

    _file_name: str

    def __init__(self, filename: str) -> None:
        self._file_name = filename

    def write(self) -> None:
        file_name = self._file_name.split(".")[0]
        extension = self._file_name.split(".")[1]
        new_extension = ""
        if "mp4" in extension:
            new_extension = "ogg"
        else:
            new_extension = "mp4"

        self._file_name = file_name + f".{new_extension}"
        print(f"writing file {self._file_name} into the disk...\n")

    def read(self, filename: str) -> None:
        print(f"reading {filename} ...")

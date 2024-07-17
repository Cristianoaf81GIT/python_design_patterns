from typing import NamedTuple

class HouseDirectorConfig(NamedTuple):
    doors: int = 2
    walls: int = 4
    roof: bool = True
    window: int = 2
    garage: bool = False
    swimming_pool: bool = False


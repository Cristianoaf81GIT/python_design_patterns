from interfaces import AbsctractHouseBuilder, House #pyright: ignore

class HouseBuilder(AbsctractHouseBuilder):

    _house: House 

    def __init__(self) -> None:
        super().__init__()
        self._house = House()

    def build_walls(self, walls: int) -> None:
        self._house.walls = walls
        return self._house

    def build_doors(self, doors: int) -> None:
        self._house.doors = doors
        return self._house

    def build_window(self, windows: int) -> None:
        self._house.windows = windows
        return self._house 

    def build_roof(self, has_roof: bool) -> None:
        self._house.roof = has_roof
        return self._house

    def build_garage(self, has_garage: bool) -> None:
        self._house.garage = has_garage
        return self._house

    def build_swimming_pool(self, has_swimming_pool: bool) -> None:
        self._house.swiming_pool = has_swimming_pool
        return self._house

    def get_result(self) -> House:
        return self._house 
        



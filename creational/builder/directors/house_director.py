from config import HouseDirectorConfig #pyright: ignore 
from interfaces import AbsctractHouseBuilder, House #pyright: ignore


class HouseDirector():

    _builder: AbsctractHouseBuilder

    def __init__(self, builder: AbsctractHouseBuilder) -> None:
        self._builder = builder

    def change_builder(self, builder: AbsctractHouseBuilder) -> None:
        self._builder = builder

    def make(self, config: HouseDirectorConfig) -> House:
        print(f'config: {config}')
        self._builder.build_walls(config[0])
        self._builder.build_doors(config[1])
        self._builder.build_roof(config[2])
        self._builder.build_window(config[3])
        self._builder.build_garage(config[4])
        self._builder.build_swimming_pool(config[5])

        return self._builder.get_result()

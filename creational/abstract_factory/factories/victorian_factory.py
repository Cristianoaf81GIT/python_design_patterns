from interfaces import AbstractFactory, Sofa, CoffeTable, Chair  # pyright: ignore
from fornitures import VictorianChair, VictorianSofa, VictorianCoffeTable #pyright: ignore

class VictorianFornitureFactory(AbstractFactory):

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffe_table(self) -> CoffeTable:
        return VictorianCoffeTable()



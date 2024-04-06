from interfaces import AbstractFactory, Sofa, Chair, CoffeTable #pyright: ignore
from fornitures import ModernChair, ModernCoffeTable, ModernSofa #pyright: ignore

class ModernFornitureFactory(AbstractFactory):

    def create_coffe_table(self) -> CoffeTable:
        return ModernCoffeTable()

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

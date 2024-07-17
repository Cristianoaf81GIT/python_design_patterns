from interfaces import (  # pyright: ignore
    AbstractFactory,
    Sofa,
    CoffeTable,
    Chair,
)


class FornitureFactory(AbstractFactory):

    _factory: AbstractFactory

    def __init__(self, factory: AbstractFactory) -> None:
        super().__init__()
        self._factory = factory

    def create_sofa(self) -> Sofa:
        return self._factory.create_sofa()

    def create_chair(self) -> Chair:
        return self._factory.create_chair()

    def create_coffe_table(self) -> CoffeTable:
        return self._factory.create_coffe_table()

    @property
    def factory(self) -> AbstractFactory:
        return self._factory

from interfaces import CoffeTable #pyright: ignore

class ModernCoffeTable(CoffeTable):

    def has_legs(self) -> bool:
        return True

    def cover(self) -> None:
        it_has_legs = self.has_legs()
        print(f'The {ModernCoffeTable.__name__} has legs ? {it_has_legs}')

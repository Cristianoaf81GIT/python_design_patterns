from interfaces import CoffeTable #pyright: ignore

class VictorianCoffeTable(CoffeTable):

    def has_legs(self) -> bool:
        return True

    def cover(self) -> None:
        it_has_legs = self.has_legs()
        print(f"The {VictorianCoffeTable.__name__}, has legs ? {it_has_legs}")

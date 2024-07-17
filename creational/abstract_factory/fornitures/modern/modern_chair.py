from interfaces import Chair #pyright: ignore

class ModernChair(Chair):

    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> None:
        it_has_legs = self.has_legs()
        print(f'sitting on: {ModernChair.__name__} has legs: {it_has_legs}')

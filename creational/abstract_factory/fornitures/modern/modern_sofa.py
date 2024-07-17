from interfaces import Sofa #pyright: ignore

class ModernSofa(Sofa):

    def seaters(self) -> int:
        return 5

    def seat(self) -> None:
        number_of_seats = self.seaters()
        print(f'Sitting on {ModernSofa.__name__}, with: {number_of_seats} seat(s)')



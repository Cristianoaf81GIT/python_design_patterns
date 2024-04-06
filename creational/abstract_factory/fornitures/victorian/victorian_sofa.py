from interfaces import Sofa  # pyright: ignore

class VictorianSofa(Sofa):

    def seaters(self) -> int:
        return 4

    def seat(self) -> None:
        number_of_seats = self.seaters()
        print(f'Sitting on {VictorianSofa.__name__}, with: {number_of_seats} seat(s)')

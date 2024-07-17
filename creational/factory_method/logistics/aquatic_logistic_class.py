from interfaces import AbstractLogistic, Transport #pyright: ignore
from transports import Ship #pyright: ignore

class AquaticLogistic(AbstractLogistic):

    def create_transport(self) -> Transport:
        return Ship()


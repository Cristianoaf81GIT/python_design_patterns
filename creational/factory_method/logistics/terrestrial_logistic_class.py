from interfaces import AbstractLogistic, Transport #pyright: ignore
from transports import Truck #pyright: ignore

class TerrestrialLogistic(AbstractLogistic):

    def create_transport(self) -> Transport:
        return Truck()

from  enums import TransportTypesEnum #pyright: ignore
from  interfaces import AbstractLogistic, Transport #pyright: ignore
from . aquatic_logistic_class import AquaticLogistic
from . terrestrial_logistic_class import TerrestrialLogistic

class LogisticFactory(AbstractLogistic):
    
    _transport: Transport
    _transport_type: TransportTypesEnum

    def plan_delivery(self, transport_type: TransportTypesEnum) -> None:
        super().__init__()
        self._transport_type = transport_type

    def create_transport(self) -> Transport:
        if self._transport_type == TransportTypesEnum.TERRESTRIAL:
            self._transport = TerrestrialLogistic().create_transport()
        elif self._transport_type == TransportTypesEnum.AQUATIC:
            self._transport = AquaticLogistic().create_transport()
        else:
            raise ValueError('Error the transport type is invalid!')

        return self._transport

        


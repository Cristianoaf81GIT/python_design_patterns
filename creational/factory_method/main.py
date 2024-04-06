from logistics import LogisticFactory #pyright: ignore
from enums import TransportTypesEnum #pyright: ignore

if __name__ == '__main__':
    terrestrial_logistic = LogisticFactory()
    terrestrial_logistic.plan_delivery(transport_type=TransportTypesEnum.TERRESTRIAL)
    truck = terrestrial_logistic.create_transport()
    truck.deliver()

    sea_logistic = LogisticFactory()
    sea_logistic.plan_delivery(transport_type=TransportTypesEnum.AQUATIC)
    ship = sea_logistic.create_transport()
    ship.deliver()






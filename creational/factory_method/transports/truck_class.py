from  interfaces import Transport #pyright: ignore

class Truck(Transport):

    def deliver(self) -> None:
        print(f'{Truck.__name__} start delivery process...')

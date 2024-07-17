from  interfaces import Transport #pyright: ignore

class Ship(Transport):

    def deliver(self) -> None:
        print(f'{Ship.__name__} start delivery process...')

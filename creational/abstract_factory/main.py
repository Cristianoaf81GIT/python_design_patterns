from factories import VictorianFornitureFactory, ModernFornitureFactory, FornitureFactory #pyright: ignore
from interfaces import AbstractFactory #pyright: ignore
from traceback import print_exception
from sys import exc_info, exit

def main() -> None:
    print('###############################################\n')
    print('# Witch forniture type would you like to buy: #\n')
    print('# 1 - Modern                                  #\n')
    print('# 2 - Victorian                               #\n')
    print('###############################################\n')

    option: int
    factory: AbstractFactory
    forniture_factory: AbstractFactory 

    try:
        option = int(input())
        
        if option == 1:
            factory = ModernFornitureFactory()
        elif option == 2:
            factory = VictorianFornitureFactory()
        else:
            raise ValueError(f'Invalid option {option}')

        forniture_factory = FornitureFactory(factory=factory)
        sofa = forniture_factory.create_sofa()
        sofa.seat()

        chair = forniture_factory.create_chair()
        chair.sit_on()
    
        coffe_table = forniture_factory.create_coffe_table()
        coffe_table.cover()
        
    except:
        print_exception(*exc_info())
    finally:
        exit()


if __name__ == '__main__':
    main()



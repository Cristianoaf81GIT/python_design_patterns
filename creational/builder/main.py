from directors import HouseDirector #pyright: ignore
from builders import HouseBuilder #pyright: ignore
from config import HouseDirectorConfig #pyright: ignore 

def main() -> None:
    # without director
    builder = HouseBuilder()
    builder.build_walls(4)
    builder.build_roof(True)
    builder.build_doors(3)
    builder.build_window(2)
    builder.build_garage(True)
    builder.build_swimming_pool(True)
    house = builder.get_result()
    
    # using director 
    director = HouseDirector(HouseBuilder())
    config: HouseDirectorConfig = HouseDirectorConfig(2, 4, True, 2, True)
    new_house = director.make(config) #pyright: ignore

    print(f'{house.__repr__()}')
    print(f'{new_house.__repr__()}')



if __name__ == '__main__':
    main()


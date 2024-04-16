from geometry import Square, Circle #pyright: ignore
from registers import ShapePrototypeRegister #pyright: ignore

def main() -> None:
    circle_prototype = Circle(width=100,height=100,points=[1,2,3,4,5,6])
    circle_cloned1 = circle_prototype.clone()

    square_prototype = Square(width=100,height=100,points=[10,20,30,40])
    square_cloned1 = square_prototype.clone()

    shape_register = ShapePrototypeRegister()

    print('circle info:\n')
    print(f'{circle_prototype.__repr__()}\n')
    print(f'{circle_cloned1.__repr__()}\n')

    print('square info:\n')
    print(f'{square_prototype.__repr__()}')
    print(f'{square_cloned1.__repr__()}')

    print('\nadd shapes to register:\n')
    shape_register.add_shape(id='circle_prototype',shape=circle_prototype)
    shape_register.add_shape(id='circle_cloned1',shape=circle_cloned1)

    shape_register.add_shape(id='square_prototype', shape=square_prototype)
    shape_register.add_shape(id='square_cloned1', shape=square_cloned1)

    print('getting a shape from shape_register\n')
    shape = shape_register.get_shape_by_id(id='circle_prototype')
    if shape is not None:
        print(f'shape founded: {shape.__repr__()}')


if __name__ == '__main__':
    main()



from interfaces import ShapeRegister, Shape #pyright: ignore

class ShapePrototypeRegister(ShapeRegister): 
    
    def __init__(self) -> None:
        super().__init__()
        self._shapes = {}

    def add_shape(self, id: str, shape: Shape) -> None:
        self._shapes[id] = shape

    def get_shape_by_id(self, id: str) -> Shape | None:
        return self._shapes.get(id, None)    

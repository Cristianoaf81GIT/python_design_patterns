from  typing import Optional
from dataclasses import dataclass

@dataclass
class House():
    walls: Optional[int | None] = None 
    doors: Optional[int | None] = None
    windows: Optional[int | None] = None 
    roof: Optional[bool | None] = None 
    garage: Optional[bool | None] = None 
    swiming_pool: Optional[bool | None] = None


    def __init__(self) -> None:
        pass


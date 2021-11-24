from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Route(Entity):
    start_town_id: str
    end_town_id: str
    price: float
    tow_way: bool

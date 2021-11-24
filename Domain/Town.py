from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Town(Entity):
    name: str
    type: str

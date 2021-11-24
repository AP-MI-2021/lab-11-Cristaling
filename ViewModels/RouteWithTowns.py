from dataclasses import dataclass

from Domain.Town import Town


@dataclass
class RouteWithTowns:
    id_entity: str
    start_town: Town
    end_town: Town
    price: float
    two_way: bool

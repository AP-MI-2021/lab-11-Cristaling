from Domain.Town import Town
from Domain.TownValidator import TownValidator
from Repository.repository import Repository


class TownService:

    def __init__(self,
                 town_repository: Repository,
                 town_validator: TownValidator):
        self.town_repository = town_repository
        self.town_validator = town_validator

    def add_town(self, town_id: str, name: str, town_type: str):
        town = Town(town_id, name, town_type)
        self.town_validator.validate(town)
        self.town_repository.create(town)

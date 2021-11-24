import json

from Domain.Route import Route
from Domain.RouteValidator import RouteValidator
from Repository.repository import Repository
from ViewModels.RouteWithTowns import RouteWithTowns


class RouteService:

    def __init__(self, route_repository: Repository, town_repository: Repository, route_validator: RouteValidator):
        self.route_repository = route_repository
        self.town_repository = town_repository
        self.route_validator = route_validator

    def add_route(self, route_id: str, start_town_id: str, end_town_id: str, route_price: float, route_two_way: bool):
        route = Route(route_id, start_town_id, end_town_id, route_price, route_two_way)
        self.route_validator.validate(route)

        errors = []

        if self.town_repository.read(start_town_id) is None:
            errors.append(f'Nu exista un oras cu id-ul {start_town_id}')
        if self.town_repository.read(end_town_id) is None:
            errors.append(f'Nu exista un oras cu id-ul {end_town_id}')
        if start_town_id == end_town_id:
            errors.append(f'O ruta nu poate sa se termine in acelasi oras din care porneste')

        if errors:
            raise ValueError(errors)

        self.route_repository.create(route)

    def get_towns_ordered_by_two_way_route_nr(self):

        result = []

        routes = self.route_repository.read()
        towns = self.town_repository.read()

        for town in towns:
            routes_starting_here = [route for route in routes if route.start_town_id == town.id_entity and
                                    route.tow_way]

            result.append((town, len(routes_starting_here)))

        return sorted(result, key=lambda x: x[1])

    def get_routes_ending_in_municipiu(self):

        result = []

        routes = self.route_repository.read()

        for route in routes:
            route_with_towns = RouteWithTowns(
                id_entity=route.id_entity,
                start_town=self.town_repository.read(route.start_town_id),
                end_town=self.town_repository.read(route.end_town_id),
                price=route.price,
                two_way=route.tow_way
            )
            if route_with_towns.end_town.type == 'municipiu':
                result.append(route_with_towns)

        return result

    def export_routes(self, file_name):

        result = {}

        routes = self.route_repository.read()
        towns = self.town_repository.read()

        for town in towns:
            destination_ids = [route.end_town_id for route in routes if route.start_town_id == town.id_entity]

            result[town.name] = [self.town_repository.read(town_id).name for town_id in destination_ids]

        with open(file_name, 'w') as f:
            json.dump(result, f)

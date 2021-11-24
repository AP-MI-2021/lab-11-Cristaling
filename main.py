from Domain.RouteValidator import RouteValidator
from Domain.TownValidator import TownValidator
from Repository.json_repository import JsonRepository
from Service.RouteService import RouteService
from Service.TownService import TownService
from UserInterface.Console import Console


def main():
    town_validator = TownValidator()
    route_validator = RouteValidator()

    town_repository = JsonRepository('towns.json')
    route_repository = JsonRepository('routes.json')

    town_service = TownService(town_repository, town_validator)
    route_service = RouteService(route_repository, town_repository, route_validator)

    console = Console(town_service, route_service)
    console.run_ui()


if __name__ == '__main__':
    main()

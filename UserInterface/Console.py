from Service.RouteService import RouteService
from Service.TownService import TownService


class Console:

    def __init__(self,
                 town_service: TownService,
                 route_service: RouteService):
        self.town_service = town_service
        self.route_service = route_service

    def show_menu(self):
        print('1 - Adauga localitate')
        print('2 - Adauga ruta')
        print('3 - Afisare localitati ordonate in functie de numarul de rute ce pornesc din ele')
        print('4 - Afisare rutelor care se termina intr-un municipiu')
        print('5 - Exporta rutele in fisier')
        print('x - Exit')

    def run_ui(self):

        while True:
            self.show_menu()
            option = input('Optiunea: ')

            if option == '1':
                self.handle_town_add()
            elif option == '2':
                self.handle_route_add()
            elif option == '3':
                self.handle_sorted_towns_by_routes()
            elif option == '4':
                self.handle_routes_ending_in_municipiu()
            elif option == '5':
                self.handle_export_routes_to_file()
            elif option == 'x':
                break
            else:
                print('Optiune invalida!')

    def handle_town_add(self):
        try:
            town_id = input('Id-ul localitatii: ')
            town_name = input('Numele localitatii: ')
            town_type = input('Tipul localitatii(sat, oras, municipiu): ')

            self.town_service.add_town(town_id, town_name, town_type)
        except ValueError as ve:
            print('Eroare validare: ', ve)
        except KeyError as ke:
            print('Eroare id: ', ke)
        except Exception as ex:
            print('Exceptie: ', ex)

    def handle_route_add(self):
        try:
            route_id = input('Id-ul rutei: ')
            town_start_id = input('Id-ul localitatii de pornire: ')
            town_end_id = input('Id-ul localitatii de final: ')
            route_price = float(input('Pretul rutei: '))
            route_two_way = bool(input('Ruta dus-intors(True/False): '))

            self.route_service.add_route(route_id, town_start_id, town_end_id, route_price, route_two_way)
        except ValueError as ve:
            print('Eroare validare: ', ve)
        except KeyError as ke:
            print('Eroare id: ', ke)
        except Exception as ex:
            print('Exceptie: ', ex)

    def handle_sorted_towns_by_routes(self):
        town_tuples = self.route_service.get_towns_ordered_by_two_way_route_nr()

        for town, route_nr in town_tuples:
            print(f'{route_nr} -> {town}')

    def handle_routes_ending_in_municipiu(self):
        routes_with_towns = self.route_service.get_routes_ending_in_municipiu()

        for route_with_town in routes_with_towns:
            print(f'Ruta cu id-ul {route_with_town.id_entity}: {route_with_town.start_town.name} -> '
                  f'{route_with_town.end_town.name}')

    def handle_export_routes_to_file(self):
        file_name = input('Nume fisier: ')

        self.route_service.export_routes(file_name)
        print('Fisier exportat!')

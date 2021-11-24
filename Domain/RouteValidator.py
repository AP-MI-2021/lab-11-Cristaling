from Domain.Route import Route


class RouteValidator:

    @staticmethod
    def validate(route: Route):
        errors = []

        if route.id_entity == '':
            errors.append('Id-ul rutei nu poate fi gol.')
        if route.start_town_id == '':
            errors.append('Id-ul localitatii de start nu poate fi gol.')
        if route.end_town_id == '':
            errors.append('Id-ul localitatii de final nu poate fi gol.')
        if route.price < 0:
            errors.append('Pretul rutei nu paote fi negativ.')

        if errors:
            raise ValueError(errors)

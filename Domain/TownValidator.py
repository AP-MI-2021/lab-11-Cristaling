from Domain.Town import Town


class TownValidator:

    @staticmethod
    def validate(town: Town):

        errors = []

        if town.id_entity == '':
            errors.append('Id-ul localitatii nu poate fi gol.')
        if town.name == '':
            errors.append('Numele localitatii nu poate fi gol.')
        if town.type not in ['sat', 'oras', 'municipiu']:
            errors.append('Tipul localitatii nu este valid. (sat, oras, municipiu)')

        if errors:
            raise ValueError(errors)

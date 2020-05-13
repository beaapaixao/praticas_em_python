class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        else:
            self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neandherthalensis'
        return self

# método estático não recebe nenhum parâmetro
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neardental(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    José = HomoSapiens('José')
    Pedro = Neardental('Pedro')
    # José.set_idade(-40) para simular o tratamento de exceção com o ValueError
    print(f'Evolução a partir da class: {", ".join(HomoSapiens.especies())}')
    print(f'Evolução a partir da instancia:{", ".join(José.especies())}')
    print(f'Homo Sapiens é evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal é evoluído? {Neardental.is_evoluido()}')

    José.idade = 40
    print(f'Nome: {José.nome} Idade: {José.idade}')

from .Pessoa import Pessoa


class Vendedor(Pessoa):

    salario = 0


def __init__(self, nome, idade, salario):
    super().__init__(nome, idade)
    self.salario = salario

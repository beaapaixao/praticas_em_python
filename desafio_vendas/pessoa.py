

class Pessoa:

    nome = ''
    idade = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return 'o nome é ' + self.nome + ' e a idade é ' + self.idade


def main():
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    pessoa = Pessoa(nome, idade)
    print(pessoa)


if __name__ == '__main__':
    main()

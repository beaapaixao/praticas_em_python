class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return 'o nome é ' + self.nome + ' e a idade é ' + str(self.idade)

    def eh_adulto(self):
        if (self.idade >= 18):
            print('Adulto')
        else:
            print('Menor de idade')


'''
def main():
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    pessoa = Pessoa(nome, idade)
    pessoa.eh_adulto()
    print(pessoa)


if __name__ == '__main__':
    main()
'''

from math import pi


# Uso de uma função retornando um valor


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Area do circulo é: ', area)

# ctrl + alt + n para executar ou ir no terminal
# entrar na pasta e digitar python nome do arquivo.py
# Um bloco é definido pela identação no Python

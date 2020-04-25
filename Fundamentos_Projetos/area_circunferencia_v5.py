from math import pi
import sys

# Uso de uma função retornando um valor


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o radio do círculo")
        print("Sintaxe: {} <raio>".format(sys.argv[0]))
else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo é: ', area)

    # ctrl + alt + n para executar ou ir no terminal
    # entrar na pasta e digitar python nome do arquivo.py
    # Um bloco é definido pela identação no Python

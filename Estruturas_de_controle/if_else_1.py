
def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Inválida'
    elif nota >= 9.1:
        return 'Sua nota é A'
    elif nota >= 8.1:
        return 'Sua nota é A-'
    elif nota >= 7.1:
        return 'Sua nota é B'
    elif nota >= 6.1:
        return 'Sua nota é B-'
    elif nota >= 5.1:
        return 'Sua nota é C'
    elif nota >= 4.1:
        return 'Sua nota é C-'
    elif nota >= 3.1:
        return 'Sua nota é D'
    elif nota >= 2.1:
        return 'Sua nota é D-'
    elif nota >= 1.1:
        return 'Sua nota é E'
    elif nota >= 0:
        return 'F'
    else:
        return 'Nota inválida'


if __name__ == "__main__":
    valor_informado = input('Digite a nota: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)

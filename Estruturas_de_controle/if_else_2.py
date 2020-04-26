def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 60):
        return 'Adulto'
    elif idade in range(61, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    # idades = (17, 35, 64, 62, 100, -2)
    # for idade in idades:
    # print(f'{idade:}: {faixa_etaria(idade)}')
    for idade in (17, 35, 64, 62, 100, -2):
        print(f'{idade:}: {faixa_etaria(idade)}')

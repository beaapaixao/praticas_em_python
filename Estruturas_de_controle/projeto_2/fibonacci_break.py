def fibonacci(quantidade):
    resultado = [0, 1]
    # _ pode representar uma variavel que não é usada
    # for _ in range(2,quantidade)
    while True:

        resultado.append(sum(resultado[-2:]))
        # usando o for eu tiro esse laço abaixo
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # lista a quantidade de números da série
    for fib in fibonacci(20):
        print(fib)

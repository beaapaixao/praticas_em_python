# contar quantas vezes o elemento de valor 10
# aparece na lista

lista = [1, 10, 2, 10, 3, 10, 4, 5, 6]

# contador = lista.count(10)

# print(f'o numero 10 apareceu {contador} vezes')

# ou usando laços como abaixo

cont = 0
for i in range(len(lista)):
    if lista[i] == 10:
        cont += 1
print(cont)


# concatenar listas
lista2 = [1, 2, 3]

# print(f'A nova lista é {lista+lista2}')

# ou usando laços como abaixo

for i in range(len(lista2)):
    lista.append(lista2[i])
print(lista)

# ou método extend(lista2)

lista.extend(lista2)
print(lista)

# inserir elemento 10 como terceiro elemento da lista

lista.append(0)
print(lista)

for i in range(len(lista)):
    lista[i+1] = lista[i]

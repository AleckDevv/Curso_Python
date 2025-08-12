notas = [30, 10, 7, 1, 5]
notas2 = [22, 33, 44, 55, 90]
print(notas)
print(notas[0])


juncao = notas + notas2
print(juncao)
print(type(juncao))


# acessando fatias (slice)
print(notas[:2])


# ordenando listas
crescente = sorted(notas)
print(crescente)

decrescente = sorted(notas2, reverse=True)
print(decrescente)

somatorio = sum(notas)
print(f"somatório: {somatorio}")

# menor valor da lista
menor_valor = min(notas)
print(menor_valor)

# maior valor da lista
maior_valor = max(notas)
print(maior_valor)

# adicionar valor ao final da lista
notas.append(100)
print(notas)

# removendo o último elemento
notas.pop()
print(notas)

# remover de uma posição especifica
notas.pop(2)
print(notas)

# inserindo em posição especifica
notas.insert(3, 90)
print(notas)

# verificando se exite um valor
verificar = 12 in notas
print(verificar)

# percorrer lista
for i in notas:
    print(i)

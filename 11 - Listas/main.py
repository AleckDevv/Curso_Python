notas = [10, 20, 30]
notas2 = [1, 2, 3, 4, 5]
print(notas)
print(notas[0])

# concatenação das listas
juncao = notas + notas2
print(juncao)
print(type(juncao))

# dessa forma, acessa a posição do elemento
print(notas[:2])

# sorted()
# função de ordem crescente
print(sorted(notas2))

# invertando a ordem da lista
print(sorted(notas, reverse=True))

# fazer somatório total dos valores da lista
print(sum(notas))

# saber o valor minimo e máximo
print(min(notas))
print(max(notas))

# add novo valor ao final da lista
notas.append(100)

# removendo o ultimo elemento
notas.pop()

# removendo na posição especifica
notas.pop(2)

# inserindo em uma posição especifica seguido de qual valor
notas.insert(4, 80)
print(notas)

# verificando se tem o valor na lista
print(12 in notas)


planetas = ["Mercúrio", "Vênus", "Saturno", "Urano", "Neturno"]
# iterando sobre os elementos da lista
for planeta in planetas:
    print(planeta)

# prática
bebidads = []
for i in range(5):
    print("Digite uma bebida: ")
    bebida = input()
    bebidads.append(bebida)

bebidads.sort()
print(f"bebidas escolhidas")

for bebida in bebidads:
    print(bebida)

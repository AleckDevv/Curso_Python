numeros = [1, 2, 3, 4, 5]
print(numeros[1])
verificar = 6 in numeros
if verificar == True:
    print("tem sim")
else:
    print("tem não")

cidades = ["Sp", "Rg", "Mg"]
print(cidades[0], cidades[2])

numeros2 = [10, 20, 30]
concatenados = numeros + numeros2
print(concatenados[0:3])


numeros3 = [5, 4, 3, 2, 1]
crescente = sorted(numeros3)
print(crescente)

reverso = sorted(numeros3, reverse=True)
print(reverso)


valores = [10, 20, 30, 40]
somatorio = sum(valores)
print(somatorio)

menor_valor = min(valores)
print(menor_valor)

maior_valor = max(valores)
print(maior_valor)

frutas = ["pêra", "uva", "maçã"]
frutas.append("goiaba")
frutas.pop()
frutas.insert(1, "melância")
print(frutas)

planetas = ["terra", "mercurio", "uranio"]
for planeta in planetas:
    print(f"o planeta é: {planeta}")


bebidas = []
for bebida in range(4):
    valor = input("digite uma bebida: ")
    bebidas.append(valor)

bebidas.sort()
print(bebidas)

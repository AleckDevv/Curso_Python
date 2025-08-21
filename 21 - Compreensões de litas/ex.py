# forma padrão de percorrer lista

numeros = []

for i in range(5):
    numeros.append(i**2)

print(numeros)

# essa forma em uma única linha

numeros2 = [i**2 for i in range(5)]
print(numeros2)


quadrados = [x**2 for x in range(6)]
print(quadrados)


pares = [x for x in range(10) if x % 2 == 0]
print(pares)

palavras = ["python", "java", "c", "javascript"]
maiusculas = [p.upper() for p in palavras]
print(maiusculas)

preco = [100, 200, 300, 400]
descontos = [p * 0.9 for p in preco]
print(descontos)


matriz = [[i for i in range(3) for j in range(3)]]
print(matriz)
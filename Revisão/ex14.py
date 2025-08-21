# funções com lambda
num = lambda x: x**2
print(num(4))


texto = lambda t, x: max(t, x, key=len)
print(texto("scasc", "csaclcml"))

numero = lambda x: x % 2 == 0

n = 2

if numero(n):
    print("é par")
else:
    print("é impar")

# função com map
numeros = [10, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))

print(quadrados)


palavras = ["python", "java", "c", "javascript"]

mais = list(map(str.upper, palavras))
print(mais)

precos = [10, 20, 30, 40]
desconto = list(map(lambda x: x - (x * 0.10), precos))
print(desconto)

# função com filter
idades = [12, 18, 20, 16, 30, 14]
maiores = list(filter(lambda x: x > 18, idades))
print(maiores)


palavras = ["oi", "python", "sol", "programação"]
caracteres = list(filter(lambda x: len(x) > 3, palavras))
print(caracteres)


# função com reduce
from functools import reduce

numeros = [1, 2, 3, 4, 5]


def mult(x, y):
    return x * y


total = reduce(mult, numeros)
print(total)


palavras2 = ["Python", "é", "muito", "bom"]
composta = reduce(lambda x, y: x + " " + y, palavras2)
print(composta)

# funções lambda = função anônima
quadros = lambda x: x**2
print(quadros(2))

for i in range(1, 11):
    print(quadros(i))

par = lambda x: x % 2 == 0
print(par(9))

f_c = lambda f: (f - 32) * 5 / 9
print(f_c(212))


# função map
num = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, num))
print(dobro)


palavras = ["São", "Paulo", "Futebol", "Clube"]
mais = list(map(str.upper, palavras))
print(mais)


# função filter
def num_pares(n):
    return n % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(num_pares, numeros))
print(pares)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)


# função reduce
from functools import reduce


def mult(x, y):
    return x * y


numeros = [1, 2, 3, 4]
total = reduce(mult, numeros)
print(total)


total2 = reduce(lambda x, y: x**2 + y**2, numeros)
print(total2)

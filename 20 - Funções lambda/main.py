# #! funções lambda
num = int(input("digite um número: "))
quadrado = lambda num: num**2
print(quadrado(num))


for i in range(1, 11):
    print(quadrado(i))


par = lambda x: x % 2 == 0
print(par(8))

# #! lambda no js seria assim:
""" par = () => {
    
} """

f_c = lambda f: (f - 32) * 5 / 9
print(f_c(200))


# #! função map()
num = [1, 2, 3, 4, 5, 6, 7]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

palavras = ["python", "é", "uma", "linguagem", "de", "programação"]

maiusculas = list(map(str.upper, palavras))
print(maiusculas)


# #! função filter()
def numeros_pares(n):
    return n % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
num_par = list(filter(numeros_pares, numeros))
print(num_par)

num_impar = list(lambda x: x % 2 != 0, numeros)
print(num_impar)


# #! função reduce()
from functools import reduce


def mult(x, y):
    return x * y


numeros2 = [1, 2, 3, 4, 5, 6, 7, 8]
total = reduce(mult, numeros)
print(total)


# #! reduce com lambda
total = reduce(lambda x, y: x**2 + y**2, numeros2)
print(total)

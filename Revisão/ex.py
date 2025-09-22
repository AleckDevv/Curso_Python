nome = "usuario"
idade = 100
altura = 1.90

print(f"{nome} - tipo {type(nome)}")
print(f"{idade} - tipo {type(idade)}")
print(f"{altura} - tipo {type(altura)}")


num1 = 10
num2 = 20
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
resto = num1 % num2
div_int = num1 // num2

print(soma)
print(sub)
print(mult)
print(div)
print(resto)
print(div_int)

print(num1 > num2)
print(num2 < num1)
print(num1 == num2)
print(num2 == num1)
print(num1 != num2)
print(num2 != num1)

idade = 16
cidada = True

if (idade >= 16) & (cidada == True):
    print("Pode votar")
else:
    print("não pode")


verificar = 10
if verificar < 0:
    print("é um número negativo")
elif verificar > 0:
    print("é um número positivo")
elif verificar == 0:
    print("é igual a zero")


contador = 0

while contador < 10:
    contador += 1
    print(contador)

for i in range(2, 21):
    print(i)

for x in range(1, 11):

    for y in range(1, 11):
        print(f"{x} x {y} = {x * y}")

import random


while True:
    num = random.randint(1, 100)
    escolha_usuario = input("Escolha um número inteiro de 1 a 100: ")

    if escolha_usuario.lower() == "sair":
        print("Você saiu do programa")
        break

    if escolha_usuario == num:
        print("Você acertou")
    else:
        print(f"Você errou. O número era {num} - Escolha novamente")


frutas = ["pêra", "manga", "uva", "kiwi", "goiaba"]
frutas.append("melância")
frutas.pop()
print(frutas)
frutas.sort()
print(frutas)

coordenadas = (100, 20)
print(f"latitude: {coordenadas[0]} - longitude: {coordenadas[1]}")

from math import sqrt

raiz = 10
print(sqrt(raiz))
print(abs(raiz))


vogais = ["a", "e", "i", "o", "u"]
frase_user = input("digite uma frase: ")

for i in vogais:
    if i in frase_user.lower():
        print(f"tem as seguintes vogais: {i}")


livro_autor = {"nome_livro": "O ladrão de raios", "genero": "ficção", "isbn": 123332113}

livro_autor["descricao"] = "um livro muito top"
print(livro_autor)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
print(set1.intersection(set2))


def saudacao(nome):
    return f"Olá, {nome}"


print(saudacao("Alex"))

try:
    num1 = int(input("digite um número: "))
    num2 = int(input("digite outro número: "))

    div = num1 / num2
    print(f"Resultado: {div}")
except ZeroDivisionError as erro:
    print("Não pode divisão por 0")


def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n - 1)


print(fat(5))

quadrado = lambda num: num**2
print(quadrado(7))


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def get_mostrar_carro(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"


carro1 = Carro("Renaut", "Prisma", 2025)
print(carro1.get_mostrar_carro())

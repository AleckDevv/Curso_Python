"""contador = 0

while contador < 10:
    contador += 1
    print(contador)

senha = 1234

while True:
    entrada = int(input("digite a senha: "))
    if entrada == senha:
        print("entrada ok")
        break
    else:
        print("não pode entrar..")


"""

""" nomes = ["Ana", "Bruno", "Carlos"]

for n in nomes:
    print(nomes)
    
for i in range(3):
    nome = input("digite o seu nome: ")
    print(nome) """

""" for i in range(1, 6):
    print(i)
     """

""" for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}") """


""" for numero in range(1, 4):
    print(f"tabuada do {numero}")
    for mult in range(1, 10):
        print(f"{numero} x {mult} = {numero * mult}") """

import random


""" numero = random.randint(0, 10)
print(numero)

n2 = random.uniform(5, 10)
print(n2)

cores = ["vermelho", "azul", "verde"]
escolha = random.choice(cores)
print(escolha)
random.shuffle(cores)
print(cores)

numero_secreto = random.randint(1, 10)
tentativa = int(input("escolha de 1 a 10: "))

if tentativa == numero_secreto:
    print("ok")
else:
    print(f"erro... o número era: {numero_secreto}") """


notas = [50, 40, 30, 20, 10]

print(notas)
print(notas[0])


print(notas[:2])


print(sorted(notas, reverse=True))

# somatório total
total = sum(notas)
menor_valor = min(notas)
maior_valor = max(notas)

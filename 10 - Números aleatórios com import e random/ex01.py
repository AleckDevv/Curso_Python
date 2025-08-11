import random

# gera um número inteiro.
# usa dois parâmetros o ponto de inicio e o
# ponto de parada
numero = random.randint(1, 10)
print(numero)


# gerar número aleatório decimal
n1 = random.uniform(1, 10)
print(n1)

# escolher um item aleatório de uma lista
cores = ["vermelho", "azul", "verde"]
print(random.choice(cores))

# embaralhar itens da lista
cartas = ["A", "k", "Q", "J"]
random.shuffle(cartas)
print(cartas)


numero_secreto = random.randint(1, 10)
tentativa = int(input("adivinhe um número entre 1 e 10: "))


if tentativa == numero_secreto:
    print("Acertou")
else:
    print(f"errou, o número era: {numero_secreto}")

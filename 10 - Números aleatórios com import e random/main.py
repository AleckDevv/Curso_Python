import random

""" valores = random.randint(1, 10)
print(valores) """


# print("gerar números entre 1 e 50")
# valores aleatórios inteiros
""" for i in range(5):
    n = random.randint(1, 50)
    print(f"número gerado: {n}") """


# valores aleatórios flaot

valor = random.random()
print(f"Número gerado: {valor}")
print(f"Número gerado: {round(valor * 10), 2}")

valor2 = random.uniform(1, 100)
print(f"Número: {round(valor2, 4)}")


l = [2, 4, 6, 9, 10]

n = random.choice(l)
print(f"número escolhido: {n}")

n = random.shuffle(l)
print(l)

z = random.sample(l, 3)
print(z)

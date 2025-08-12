# adivinha
import random

num_aleatorio = random.randint(1, 10)

tentativas = 0

while True:
    tentativa = int(input("digite um número: "))
    tentativas += 1

    print(f"{tentativa} tentativa feita")
    if tentativa == num_aleatorio:
        print(f"Acertou! Número escolhido: {tentativa}")
        break
    else:
        print("Número errado")


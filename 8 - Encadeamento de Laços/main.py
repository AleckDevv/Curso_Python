import random

for cont_ex in range(1, 6):
    print(f" \nRodada: {cont_ex}")

for cont_in in range(5, 0, -1):
    print(f"valor: {cont_in}")


for a in range(1, 6):
    print(f"\nConjunto: {a}")

    for b in range(5):
        num = random.randint(1, 100)
        print(f"Valor: {num}")



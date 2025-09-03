for cont_ex in range(1, 6):
    print(f"rodou {cont_ex}")

    for cont_in in range(6, 0, -1):
        print(f"Valor: {cont_in}")


import random

for a in range(1, 6):
    print(f"conjunto {a}")
    for b in range(6):
        num = random.randint(1, 100)
        print(num)

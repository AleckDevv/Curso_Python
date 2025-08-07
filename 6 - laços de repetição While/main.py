"""num = 0

while num < 10:
    num += 1
    print(num)
print("Laço encerrado")"""

""" aluno = input("Digite seu nome: ")
while aluno == "x":
    print(f"Seja bem vindo {aluno}") """

nome = None
while True:
    print("Digite seu nome ou x para parar: ")
    nome = input()

    if nome.lower() == "x" or nome.upper() == "X":
        break

    if not nome.replace(" ", "").isalpha():
        print("Não pode digitar números")
        continue

    print(f"Bem vindo: {nome}")

print("Até logo")

nomes = ["Ana", "Bruno", "Carlos"]

for i in nomes:
    print(i)

# range
# range(inicio, fim, paso)

""" for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(10, -1, -2):
    print(i)

nomes = []
for i in range(2):
    nome = input("Digite o nome: ")
    nomes.append(nome)

print(nomes) """

for x in range(11):
    for y in range(11):
        print(f"a tabuada de {x} x {y} é igual a: {x * y}")

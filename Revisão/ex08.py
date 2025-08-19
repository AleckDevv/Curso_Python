numeros = [1, 2, 3]
print(numeros[:1])
print(numeros[2:3])
print(len(numeros))
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

lista_nomes = []
for i in range(5):
    nome = input("digite 5 nomes: ")
    lista_nomes.append(nome)
print(lista_nomes)

frutas = ["pera", "uva", "maçã", "morango", "kiwi"]

while True:
    fruta_user = input("qual fruta você quer saber: ")

    if fruta_user in frutas:
        print("fruta disponivel")
        continue
    elif fruta_user == "sair":
        print("você saiu do sistema")
        break
    else:
        print("fruta não disponivel... tente novamente")


lista_numeros = []

for i in range(10):
    numeros_user = int(input("digite um número: "))
    lista_numeros.append(numeros_user)

inverso = sorted(lista_numeros, reverse=True)
somatorio = sum(inverso)
print(somatorio)
print(inverso)


notas_aluno = []

for i in range(5):
    nota_aluno = int(input("digite 5 notas: "))
    notas_aluno.append(nota_aluno)
    somatorio = sum(notas_aluno)
    media = somatorio / 5

if media >= 7:
    print("aprovado")
else:
    print("reprovado")


lista_compras = []

while True:
    compra_user = str(input("qual a compra: "))
    lista_compras.append(compra_user)

    if compra_user == "sair":
        print("compras add ao carrinho")
        print(f"seu carrinho: {lista_compras}")
        break

num1 = [1, 2, 3, 4, 5]
num2 = [2, 5, 10, 8, 1]

juntar = num1 + num2
print(set(juntar))

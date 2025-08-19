<<<<<<< HEAD
import random

# escolher aluno aleatório para responder uma pergunta
lista = []
for i in range(5):
    nome = input("digite 5 nomes: ")
    lista.append(nome)


escolher_aluno = random.choice(lista)
print(f"Aluno {escolher_aluno} deve responder uma pergunta")


# add comprar e mostar elas em ordem aleatória
compras = []
for i in range(5):
    produto = str(input("digite 5 produtos: "))
    compras.append(produto)


random.shuffle(compras)
print(f"as compras em ordem aleatória fica assim: {compras}")


# jogo cara ou cora
cara_coroa = ["cara", "coroa"]

while True:
    escolha = random.choice(cara_coroa)
    valor = input("qual você escolhe: ")
    if valor == escolha:
        print(f"acertou! o valor certo era: {valor}")
        break
    else:
        print("errado... tente novamente")


# gerar senha embaralhada
senha = "eoicc81"

lista = list(senha)
random.shuffle(lista)
embaralhar = "".join(lista)
print(embaralhar)
=======
lista = [1, 2, 3, 4]
incremento = 1

for i in lista:
    i += incremento
    print(i)


for i in range(4):
    print(lista[i])

for i in range(1, 11):
    print(i)


""" 
o range funciona da seguinte forma
rage(inicio, fim, de quanto em quanto)
"""
for n in range(0, 11, 2):
    print(n)
    

nome = "Alex"
for letra in nome:
    print(letra)

>>>>>>> 85681606e5d58da60150053cb02e167353662b6a

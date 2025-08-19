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

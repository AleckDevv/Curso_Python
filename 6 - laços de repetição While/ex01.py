# verificação de senha
senha = None

while True:
    print("Digite a senha: ")
    senha = int(input())

    if senha != 1234:
        print("senha incorreta. Digite novamente")
        continue
    elif senha == 1234:
        print("Acesso permitido")
        break
print("entrou no sistema...")


# verificar nome válido

nome = None

while True:
    print("Digite seu nome ou x par sair: ")
    nome = input()

    if not nome.replace(" ", "").isalpha():
        print("Não pode digitar números ou simbolos")
        continue

    if (nome.lower() == "x") or (nome.upper() == "X"):
        print("Saiu do programa")
        break

    print(f"✅ Bem-vindo(a), {nome}!\n")


# variável que armazena os números digitados
numeros = []

while True:
    # salvando os números em uma variável
    numeros_digitado = int(input("Digite um número:"))

    # verifican do se quando a pessoa digita zero, para encerrar o loop
    if numeros_digitado == 0:
        break

    # add os números digitado para dentro do array numeros
    numeros.append(numeros_digitado)

# variável contadora que soma ao total dos números
# que foram add ao array
soma_total = 0
for n in numeros:
    soma_total += n

print(f"Você digitou os números: {numeros}")
print(f"A soma total é: {soma_total}")

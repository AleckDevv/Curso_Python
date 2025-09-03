contador = 0
while contador < 10:
    contador += 1
    print(contador)


senha_correta = "1234"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("digite a senha: ")
    if senha_digitada != senha_correta:
        print("senha incorreta")
print("aceso permitido")

while True:
    comando = input("digite 'sair' para encerrar: ")
    if comando.lower() != "sair":
        print("comando errado, tente novamente")
        continue
    elif comando.lower() == "sair":
        break
print(f"você digitou {comando}")

# cria um array vazio
numeros = []
while True:
    numeros_digitado = int(input("digite um número ou 0 para sair: "))

    # se digitar 0, o programa fecha
    if numeros_digitado == 0:
        break

    # pega os números digitados e add ao array vazio
    numeros.append(numeros_digitado)

# variável contadora para somar em +1 com os números dentro do array
soma_total = 0
for i in numeros:
    soma_total += i

print(f"Você digitou os números: {numeros}")
print(f"A soma total é: {soma_total}")


codigos_pedidos = [150, 300, -50, 400, 0, 80, -20]
total_pedidos = 0
pedidos_cancelados = 0

for i in codigos_pedidos:
    if i == 0:
        print("Código 0 encontrado. Parando processamento")
        break

    elif i < 0:
        print(f"Pedido com código {i} é inválido (cancelado). Ignorando...")
        pedidos_cancelados += 1
        continue

    total_pedidos += 1
    print(f"pedido {i} processado. Total atual: {total_pedidos}")

print("\n--- Relatório Final ---")
print(f"Valor total dos pedidos processados: {total_pedidos}")
print(f"Quantidade de pedidos cancelados ignorados: {pedidos_cancelados}")


for i in range(1, 11):
    if i == 5:
        continue
    elif i > 8:
        break

    print(i)

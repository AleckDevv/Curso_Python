"""contador = 0

while contador < 5:
    contador += 1
    print(contador)"""

senha_correta = 1234
senha_digitada = ""

# o while verifica se a condição vai ser verdadeira
# ou falsa, enquanto não for verdadeira, o loop
# não para.
""" while senha_digitada != senha_correta:
    senha_digitada = int(input("digite a senha: "))

    if senha_digitada != senha_correta:
        print("errada")
print("ok")


while True:
    comando = input("digite 'sair para parar: ")
    if comando == "sair":
        break
print(f"você digitou: {comando}") """


""" contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f"número: {contador}") """

senha = ""

while True:
    print("digite a senha: ")
    senha = int(input())

    if senha != 1234:
        print("senha incorreta. digite novamente")
        continue
    elif senha == 1234:
        print("acesso permitido")
        break
print("entrou no sistema")



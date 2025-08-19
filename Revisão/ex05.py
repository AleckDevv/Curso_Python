contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f"contando: {contador}")
""" 
o continue pula a execução do próximo laço
nesse exemplo de cima, quando a condição for
igual a 3, ele pula o 3 e passa para a próxima execução
"""


""" 
se não tiver um incremento no laço
pode dar loop infinito
"""

senha_correta = 1234
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = int(input("Digite a senha: "))
    if senha_digitada != senha_correta:
        print("Senha incorreta, tente novamente.")

print("Acesso permitido!")


while True:
    comando = input("digite 'sair' para parar: ")
    if comando.lower() == "sair":
        break
print(f"você digitou: {comando}")

tem_cnh = False
idade = 18

idade_usuario = int(input("Digite sua idade: "))
if (idade >= 18) and (tem_cnh == True):
    print("Pode dirigir")
else:
    print("Não pode dirigir")



tem_ingresso = "n"
esta_lista = "n"

verificar_entrada = input("Tem ingresso? ")
if tem_ingresso or esta_lista:
    print("pode entrar")
else:
    print("não pode entrar")

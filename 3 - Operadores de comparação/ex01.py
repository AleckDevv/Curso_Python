idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você já pode tirar a carteira de habilitação!")
else:
    print("Você ainda não pode tirar a carteira de habilitação.")

senha_permitida = 1234
senha = int(input("Dite a senha: "))
if senha == senha_permitida:
    print("acesso permitido")
else:
    print("acesso negado")


nome_permitido = "Alex"
nome_digitado = input("digite seu nome: ")
if nome_digitado != nome_permitido:
    print("você não é Alex")
else:
    print(f"Bem vindo {nome_digitado}")


valor_produto = 100
valor_carteira = float(input("Qual o seu saldo? "))

if valor_carteira < valor_produto:
    print("Não é possivel comprar")
else:
    print("Pode comprar")

nota1 = int(input("digite uma nota: "))
nota2 = int(input("digite outa nota: "))

if nota2 > nota1:
    print("você melhorou!")
else:
    print("precisa melhorar mais!")

idade = int(input("digite a idade: "))
if idade <= 12:
    print("você paga meia entrada")
else:
    print("você paga entada inteira")

carga_suportada = 500
peso_atual = float(input("Qual seu peso atual? "))
if peso_atual >= carga_suportada:
    print("limite execedido, o elevador não pode subir")
else:
    print("elevador liberado")

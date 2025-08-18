idade = 20
possui_carteira = True

# ambas as condições tem que ser true
if idade >= 18 and possui_carteira:
    print("pode dirigir")
else:
    print("não pode dirigir")


# basta apenas uma condição ser verdadeira para que
# seja true
tem_ingresso = False
nome_na_lista = True

if tem_ingresso or nome_na_lista:
    print("entrada liberada")
else:
    print("sem entrada")

# inverte a condição
# se for true vira false
# se for false vira true
tem_passagem = False
if not tem_passagem:
    print("você precisa comprar a passagem")
else:
    print("boa viagem")


idade = int(input("digite sua idade: "))
tem_convite = input("você tem convite (s/n)").lower()

if idade >= 18 and (tem_convite == "s" or tem_convite == "sim"):
    print("entrada permitida")
else:
    print("entrada negada")

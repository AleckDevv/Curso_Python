maior_idade = True
exame_medico_aprovado = False
if (maior_idade == True) and (exame_medico_aprovado == True):
    print("apto para tirar a carteira de motorista")
else:
    print("inapto")

fim_de_semana = True
tem_passe = False

if (fim_de_semana == True) or (tem_passe == True):
    print("entrada gratuita")
else:
    print("entrada não permitida")


media_final = 8.6
numeros_faltas = 7
atleta = False

if (media_final > 8) and (numeros_faltas < 6) or (atleta == False):
    print("elegivel para bolsa")
else:
    print("não elegivel")


numeros = int(input("digite um número de 0 a 10"))
if (numeros < 0) or (numeros > 10):
    print("número válido")
else:
    print("número válido")

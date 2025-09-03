# operadores lógicos

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = "pode participar: " + str(resultado)
print(msg)


porta = "f"
janela = "f"

alarme = (porta == "a") or (janela == "a")
msg2 = "alarme disparado: " + str(alarme)
print(msg2)


tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg3 = "tem dinheiro: " + str(tem_dinheiro)
print(msg3)

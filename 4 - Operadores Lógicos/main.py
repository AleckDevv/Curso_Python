"""
com operadores & and, ambas as condições devem ser verdadeiras
"""

idade = 11
altura = 1.75

resultado = (idade >= 18) & (altura >= 1.70)
print(resultado)


""" 
operador or
se uma condição for satifeita, retorna true
"""
porta = "a"
janela = "f"
alarme = (porta == "a") or (janela == "a")
print(f"alarme disparado? {alarme}")


""" 
operador not
ele inverte o resultado da operação
se era True, passa a ser False e vice versa
"""
tem_dinheiro = False

msg = f"tem dinheiro? {not tem_dinheiro}"
print(msg)

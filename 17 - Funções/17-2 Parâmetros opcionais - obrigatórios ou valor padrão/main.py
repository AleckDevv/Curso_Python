# parâmetros obrigatórios


def saudacao(nome):
    print(f"olá {nome}")


saudacao("alex")
# saudacao() erro - precisa
# do parâmetro nome, se não passar gera erro


# parâmetro opcional
# pode ser passado ou não
def saudacao2(nome, msg="bem vindo"):
    print(f"{msg}, {nome}")


saudacao2("alex")
saudacao2("alex", "oi")


# valor padrão
def potencia(numero, expoente=2):
    return numero**expoente


print(potencia(3))
print(potencia(3, 3))
# é quando define um valor inicial
# e esse valor pode ser alterado

""" 
obs: parâmetros obrigratórios devem
vir antes que os opcionais
"""

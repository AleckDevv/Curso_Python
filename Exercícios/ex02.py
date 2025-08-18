"""letra = input("digite f ou m: ")
if letra.lower() == "f" or letra.upper() == "F":
    print(f"é feminino")
elif letra.lower() == "m" or letra.upper() == "M":
    print(f"é masculino")
else:
    print("gênero não identificado")"""

""" entrada = input("digite uma letra: ")
vogais = ["a", "e", "i", "o", "u"]

if entrada in vogais:
    print("é vogal")
else:
    print("é consoante") """


""" nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite outra nota: "))

media = (nota2 + nota2) / 2

if media >= 7:
    print("aprovado")
elif media < 7:
    print("reprovado")
elif media == 10:
    print("aprovado") """


""" num1 = int(input("digite um número: "))
num2 = int(input("digite outro número: "))
num3 = int(input("digite outro número: "))

maior = max(num1, num2, num3)
print(f"o maior é {maior}") """

""" numeros = [
    int(input("digite um número: ")),
    int(input("digite outo número: ")),
    int(input("digite mais um número: ")),
]

ordenado = sorted(numeros, reverse=True)
print(ordenado) """


""" turno = input("qual turno vc estuda")
if turno.lower() == "m" or turno.upper() == "M":
    print("bom dia")
elif turno.lower() == "v" or turno.upper() == "V":
    print("boa tarde")
elif turno.lower() == "n" or turno.upper() == "N":
    print("boa noite")
else:
    print("turno não encontrado") """


""" 
. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input("Digite o salário atual do colaborador: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após aumento: R$ {novo_salario:.2f}")

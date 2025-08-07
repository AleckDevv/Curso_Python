n1 = n2 = 0.0

media = 0.0

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print("aprovado")
elif media >= 5:
    print("está de recuperação")
else:
    print("reprovado")

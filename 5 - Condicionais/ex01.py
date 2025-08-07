peso_usuario = float(input("Qual o seu peso: "))
altura_usuario = float(input("Qual a sua altura: "))
imc = peso_usuario / (altura_usuario**2)

if imc < 18.5:
    print("Abaixo do peso")
elif (imc >= 18.5) & (imc <= 24.9):
    print("Peso normal")
elif (imc >= 25.0) & (imc <= 29.9):
    print("Sobrepeso")
elif (imc >= 30.0) & (imc <= 39.9):
    print("Obsesidade")
else:
    print("obesidade grave")

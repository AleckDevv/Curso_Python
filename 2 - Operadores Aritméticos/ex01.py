# soma de dois números
n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))
soma = n1 + n2
print(f"a soma é: {soma}")

# calculo de média
nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite outra nota: "))
media = (nota1 + nota2) / 2
print(f"a media é: {media}")

# Calculando idade com base no ano de nascimento
ano_idade = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2025

idade = ano_atual - ano_idade
print(f"você tem {idade} anos")

# area do retângulo
altura = int(input("digite a altura do retângulo: "))
largura = int(input("digite a largura do retângulo: "))
area = altura * largura
print(f"area tototal {area}")

# Divisão com resultado inteiro
n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))

divisao_inteira = n1 // n2
resto_divisao = n1 % n2
print(f"divisão inteira: {divisao_inteira}")
print(f"resto divisão: {resto_divisao}")


# Valor total da compra
produtos = [
    {"nome": "Bolsa", "qt": 3, "preco": 100},
    {"nome": "Têncis", "qt": 10, "preco": 50},
    {"nome": "Blusa", "qt": 7, "preco": 20},
    {"nome": "Meia", "qt": 1, "preco": 10},
    {"nome": "Cueca", "qt": 5, "preco": 45},
]

for produto in produtos:
    total = produto["qt"] * produto["preco"]
    print(
        f"Produto comprado: {produto['nome']}, Quantidade: {produto['qt']}, Preço unitário: R${produto['preco']}, Total a pagar: R${total}"
    )

# verificador de par ou impar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("É par")
else:
    print("É impar")



# potência
n1 = int(input("Digite um número"))
print(f"seu número elevado ao quadrado {n1 ** 2} e seu número elevado ao cubo {n1 ** 3}")



# tempo de viagem
distancia = int(input("Qual a distância do destino? "))
velocidade = int(input("Qual a sua velocidade atual? "))

tempo = distancia / velocidade
print(f"tempo estimado {tempo}")


# conversor de temperatura
temp = float(input("Digite a temporatura em graus Celsius: "))
graus_f = temp * 1.8 + 32
print(f"A temperatura em Fahrenheit é: {graus_f}")

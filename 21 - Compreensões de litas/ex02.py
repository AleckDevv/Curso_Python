quadros = [x**2 for x in range(11)]
print(quadros)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in nums if x % 2 == 0]
print(pares)


palavras = ["casa", "carro", "bicicleta"]
maiusculas = [m.upper() for m in palavras]
print(maiusculas)

nomes = ["Ana", "Roberto", "Clara", "João", "Fernanda"]
maiores_quatro = [letra for letra in nomes if len(letra) > 4]
print(maiores_quatro)

a = [1, 2, 3]
b = [4, 5, 6]

resultado = [x * y for x in a for y in b]
print(resultado)


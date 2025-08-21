# compreensão de listas
"""
é basicamente uma outra forma de
percorrer listas

mas dependendo de como é feito o
código, pode ser que não seja uma boa
usar esse tipo de algoritmo
"""


numeros = [1, 4, 7, 9, 12, 21]

quadros = list(map(lambda x: x**2, numeros))
print(quadros)


quadros2 = [num**2 for num in numeros]
print(quadros2)


pares = [num for num in range(11) if num % 2 == 0]
print(pares)


frase = "teste de compreensão de listas"
vogais = ["a", "e", "i", "o", "u"]

lista_vogais = [v for v in frase if v in vogais]
print(f"a frase possui {len(lista_vogais)} vogais")


distributiva = [k * m for k in [2, 3, 4] for m in [10, 20, 30]]
print(distributiva)

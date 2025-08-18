# lambda é uam função anônima
"""
sintaxe:
lambda argumentos: expressão
"""

dobro = lambda x: x * 2
print(dobro(5))


nome = input("nome: ")
mostrar_nome = lambda n: f"seu nome é {n}"
print(mostrar_nome(nome))

"""
exmplo de como seria em js:

(n) => {
    return 
}
 """


def quadros(x):
    return x * x


numeros = [1, 2, 3, 4, 5]
resultado = map(quadros, numeros)
print(list(resultado))

par = lambda x: x % 2 == 0
print(par(10))

primeira_letra = lambda texto: texto[0]
print(primeira_letra("Alex"))


juntar = lambda a, b: f"{a} {b}"
print(juntar("Alex", "Soares"))


pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

nomes = ["ana", "carlos", "beatriz", "joao"]
ordenados = sorted(nomes, key=lambda x: x[-1])
print(ordenados)


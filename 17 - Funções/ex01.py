def saudacao(nome):
    boas_vindas = f"bem vindo {nome}"
    print(boas_vindas)


saida = saudacao("Teste")
print(saida)


def maior_numero(numeros):
    lista = []
    for i in numeros:
        lista.append(i)
    return max(lista)


if __name__ == "__main__":
    valores = [1, 10, 2, 30, 100]
    resultado = maior_numero(valores)
    print(resultado)

from math import factorial


def fat(num):
    resultado = factorial(num)
    return resultado


saida = fat(10)
print(saida)


def ordenar(numeros):
    lista = []

    for i in numeros:
        lista.append(i)
    return lista


if __name__ == "__main__":
    valores = [8, 7, 6, 5, 4, 3, 2, 1]
    resultado = ordenar(valores)
    resultado.sort()
    print(resultado)

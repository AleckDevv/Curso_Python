"""
Exercício — Soma de Números com Recursão e Try/Except
Crie uma função recursiva chamada soma_lista que:

Receba uma lista de números inteiros.

Some todos os elementos usando recursão (não pode usar sum() ou for).

Trate os seguintes erros com try/except:

TypeError: Caso algum elemento da lista não seja um número, mostrar "A lista deve conter apenas números".

RecursionError: Caso a lista seja muito grande, mostrar "Lista muito grande para processar recursivamente".
"""

def soma_lista(lista):
    try:
        if len(lista) == 1:
            return lista[0]

        return lista[0] + soma_lista(lista[1:])

    except TypeError:
        print("a lista deve conter apenas números")
    except RecursionError:
        print("lista muito grande para processar recursivamente")


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5]
    resultado = soma_lista(valores)

    if resultado is not None:
        print(f"a soma da lista é: {resultado}")

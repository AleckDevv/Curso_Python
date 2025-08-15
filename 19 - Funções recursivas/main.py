# função recursiva
# contagem regressiva


def contagem_regressiva(n):
    if n == 0:
        print("acabou")
    else:
        print(n)
        contagem_regressiva(n - 1)


contagem_regressiva(10)


# função recursiva fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


if __name__ == "__main__":
    x = int(input("Digite um número inteiro para calcular o fatorial: "))
    try:
        res = fatorial(x)
    except RecursionError:
        print("Valor muito grande... não foi possível calcular o fatorial")
    else:
        print(f"o fatorial de {x} é {res}")

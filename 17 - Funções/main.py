"""# sintaxe:
def nome_função():
    # sequência de argumentos
    # pode ter ou não return
# chamada da função
nome_função()"""

def msg(mensagem):
    return mensagem


resultado = msg("Teste")
print(resultado)


def soma(n1, n2):
    resultado = n1 + n2
    return resultado


saida = soma(10, 20)
print(saida)


def div(k, j):
    if j != 0:
        # verificação para não deixar
        # dividir por 0
        # pois dar erro se tentar divir por 0
        return k / j
    else:
        print("não dá pra dividir por zero")


if __name__ == "__main__":
    a = int(input("digite um número: "))
    b = int(input("outro número: "))

    r = div(a, b)
    print(r)


def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x**2)
    return quadrados


if __name__ == "__main__":
    valores = [2, 4, 5, 6, 7, 8]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)

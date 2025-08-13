# exceção é um objeto que representar um erro
# que ocorreu ao executar o programa.

# blocos try... except

"""
alguns tipos de exceção que o py já fornece
Exception
ArithmeticError
OverflowError
ZeroDivisionError
ImportError
NameError
IOError
IdentationError
RecursionError
TypeError
"""


def div(k, j):
    return round(k / j, 2)


if __name__ == "__main__":
    while True:
        try:
            n1 = int(input("digite um número: "))
            n2 = int(input("digite outro número: "))
            break
        except ValueError:
            print("Ocorreu um erro ao ler o valor. Tente novamente")
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print("não é possivel divir por zero")
    except:
        print("ocorreu um erro desconhecido")
    else:
        print(f"resultrado {r}")
    finally:
        print("fim do cálculo...")

""" 
o que tiver dentro do try, vira global
ou seja, não pode acessar de fora desse bloco
"""

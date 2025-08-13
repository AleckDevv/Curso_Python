from math import sqrt

if __name__ == "__main__":
    try:
        num = int(input("digite um número positivo"))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print("número negativo não permitido")
    else:
        print(f"{num} {sqrt(num)}")
    finally:
        print("fim do cálculo")


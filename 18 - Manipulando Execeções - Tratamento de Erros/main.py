"""try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    divisao = num1 / num2
    print(f"a divisão é: {divisao}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero")
except ValueError:
    print("Erro: Digite apenas números")
except Exception as generica:
    print(f"Ocorreu algum erro inesperado {generica}")
finally:
    print("programa encerrado...")

lista = ["carro", "jato", "ônibus", "moto", "avião"]

try:
    escolha = int(input(f"escolha um indice de 0 a {len(lista)-1}: "))
    print(f"escolhido: {lista[escolha]}")
except IndexError:
    print("indice não encontrado")
except ValueError:
    print("digite apenas números")
except KeyboardInterrupt:
    print("tecla não reconhecida...")
finally:
    print("programa encerrado..")

while True:
    try:
        num1 = int(input("digite um número: "))
        num2 = int(input("digite outro número: "))
        divisao = num1 / num2

    except ValueError:
        print("erro ao ler o valor")

    except ZeroDivisionError:
        print("não pode divir por 0")

    except KeyboardInterrupt:
        print("você esbarrou no teclado")
        break

    else:
        print(f"a divisão é: {divisao}")
        break
    finally:
        print("programa encerrado")

# forçar uma exceção
from math import sqrt

if __name__ == "__main__":
    try:
        num3 = int(input("digite um número positivo: "))
        if num3 < 0:
            raise ArithmeticError
    except AttributeError:
        print("fornecido um número negativo")
    else:
        print(f"{num3} {sqrt(num3)}")
    finally:
        print("fim do cálculo")
"""


def validar_senha(senha):
    if len(senha) < 8:
        raise ValueError("A senha deve ter no mínimo 8 caracteres")

    if not any(char.isdigit() for char in senha):
        raise ValueError("A senha deve ter pelo menos 1 número")

    if not any(char.isupper() for char in senha):
        raise ValueError("A senha deve conter pelo menos 1 letra maiúscula")


if __name__ == "__main__":
    while True:
        senha = input("Digite uma senha: ")
        try:
            validar_senha(senha)
            print("Senha válida")
            break  # sai do loop se a senha estiver correta
        except ValueError as e:
            print("Erro:", e)

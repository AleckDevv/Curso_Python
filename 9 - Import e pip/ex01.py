# importando somente a função do módulo
# from math import sqrt
import meu_modulo

# importando o módulo completo e dando uma apelido
# assim, não fica repetindo o nome do módulo
# import math as mtm

# import universal - importando tudo do math
# não é uma forma muito usada
# from math import *

# num1 = 16

""" print(sqrt(num1))
print(mtm.exp2(num1)) """


if __name__ == "__main__":
    num2 = 10
    num3 = 3

    resultado = meu_modulo.soma(num2, num3)
    print(resultado)
    

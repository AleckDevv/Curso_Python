"""
== -> verifica o tipo do dado
!= -> diferente igual
> maior
< menor
>= maior ou igual
<= menor ou igual
"""

x = y = z = False

n1 = n2 = 0


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

x = n1 == 2
print(f"São iguais? {x}")
z = n1 > n2
print(f"{n1} é maior que {n2}: {z}")
y = n1 != n2
print(f"São diferentes? {y}")
"""
operadores aritméticos
+ mais
- menos
* vezes
/ divisão
// divisão inteira
% resto da divisão
** exponenciação
"""

# soma
preco_protudo = 100
frete = 15
total = preco_protudo + frete
print(f"valor total {total}")

# subtração
saldo = 500
gasto = 120
restante = saldo - gasto
print(restante)

# multiplicação
quantidade = 4
preco = 25
total = quantidade * preco
print(total)

# na divisão, sempre vai dar float
media = (8 + 7 + 9) / 3
print(media)

# divisão inteira
dias = 7
pessoas = 2
turnos = dias // pessoas
print(turnos)

# resto da divisão
print(10 % 3)

# exponenciação
print(2**3)

# verificar se é impar ou par
numero = 7
if numero % 2 == 0:
    print("é par")
else:
    print("é impar")

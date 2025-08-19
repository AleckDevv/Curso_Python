"""
uma tupla é imutável
não pode valores e nem modificar

mas ela é mais rápida que uma lista
"""

# criando uma tupla

tupla = (10, True, "item")
print(tupla)

# acessar os valoree é da mesma forma que acessa
# um array []

print(tupla[0])

# desempacotamento
pessoa = ("Alex", 25, "Brasil")
nome, idade, pais = pessoa
print(f"{nome} {idade} {pais}")

""" 
só usar as tuplas se formos querer que os valores
não vão se alterar
"""


cores = ("vermelho", "verde", "azul", "amarelo")
print(cores[0])
print(cores[-1])

numeros = (10, 20, 30, 40, 50)
print(numeros[:3])
print(numeros[2:])


tupla = (1, 2, 2, 3, 4, 2, 5)
print(tupla.count(2))
print(tupla.index(3))
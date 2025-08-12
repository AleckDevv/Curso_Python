"""
uma tupla não pode ter o seu conteúdo
alterado, a não ser que essa tupla seja
convertida em uma lista.

Em questões de desempenho, uma tupla é mais
rápida que uma lista
"""

# da mesma forma que o acessa uma lista,
# é igual para a tupla
tupla = (1, 2, 3, 4)
print(tupla)
print(tupla[0])


# desempacotamento dos dados
pessoa = ("Alex", 25, "Brasil")
nome, idade, pais = pessoa
print(f"{nome}, {idade}, {pais}")

# tentando alterar o valor da tupla
""" tupla[0] = "teste"
print(tupla) """

# converter uma tupla em lista
conversao = list(tupla)
print(conversao)

# depois que converte a tupla pra lista
# é possivel reatribuir valores

conversao[0] = "teste"
print(conversao)


frutas = ("uva", "pêra", "kiwi")
print(frutas[0], frutas[2])

nomes = ("ana", 10, "sp")
nome, idade, cidade = nomes
print(nomes)

valores = (1, 3, 5, 3, 7, 3, 9)
print(valores.count(3))

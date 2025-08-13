frutas = {"maçã", "banana", "uva"}
print(frutas)
""" 
tentando add o mesmo item
# frutas.add("maçã")
não vai dar nenhum erro, porén, o set ignora essa adição
"""

# pode criar um set vazio, mas não deve usar {}
# pois assim, vai estar criando um dicionário
# tem que usar o método set()
meu_set = set()
print(type(meu_set))
meu_set.add("teste")
meu_set.add("teste2")
print(meu_set)

# criar um set aparti de uma lista
numeros = set([1, 1, 1, 2, 3, 3, 4])
print(numeros)

""" 
caracteristicas:
não permite elementos repetidos
gera os elementos com a ordem aleatória
pode adicionar e remover elementos
não pode ter listas ou outros sets dentro de um mesmo set
"""

# métodos comuns
# adiconar um elemento
frutas.add("pêra")
print(frutas)

# remover elemento
frutas.remove("pêra")
print(frutas)

# limpar todo o set
frutas.clear()
print(frutas)

# mostrar quais elementos tem em comum com outro set
# intersection()
elementos1 = {1, 2, 3, 4, 5, 6}
elementos2 = {2, 1, 7, 7, 8, 10}
print(elementos1.intersection(elementos2))

# fazer união sem repetir os elementos
uniao = elementos1.union(elementos2)
print(uniao)

# saber a diferença que tem de um set para outro
diferenca = elementos1.difference(elementos2)
print(diferenca)

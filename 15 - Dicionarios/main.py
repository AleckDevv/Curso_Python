elemento = {"Z": 3, "nome": "Lítio", "grupo": "Metais Alcalinos", "densidade": 0.534}

print(elemento["nome"])
print(elemento["densidade"])
print(len(elemento))

# atualizar o valor da chave
elemento["nome"] = "Barro"
print(elemento["nome"])

# adicionar um novo objeto
""" 
caso essa chave não exista, ele vai ser criada
"""
elemento["periodo"] = 1
print(elemento)

# exclusão de itens
""" del elemento["nome"]
print(elemento) """

# apagar todos os objetos
""" 
todos os objetos agora foram apagados
mas ele ainda ficam na memória para cas
queira adicionar outros valores
"""
#! elemento.clear()
# print(elemento)

# removendo o objeto da memória
""" 
quando remove o objeto e tenta
acessar ele, vai der o erro de que
ele não está definido
"""
# del elemento
# print(elemento)


# retornando os itens do dicionário
print(elemento.items())
for i in elemento.items():
    print(i)


# retornando o valor das chaves dos dicionário
print(elemento.keys())
for i in elemento.keys():
    print(i)

# retornando os valores das chaves
print(elemento.values())
for i in elemento.values():
    print(i)

# desempacotando as chaves e os valores
""" 
gera como se fosse um relatório em
formato de tabela
"""
for i, j in elemento.items():
    print(f"{i}: {j}")

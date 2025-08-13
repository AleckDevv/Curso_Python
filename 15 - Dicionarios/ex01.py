# sintaxe
dicionario = {"chave1": "valor1", "chave2": "valor2"}

# criando um dict
pessoa = {"nome": "Alex", "idade": 25, "cidade": "São Paulo"}

print(pessoa)
# acessando os valores
print(pessoa["cidade"])

# alterando os valores
pessoa["idade"] = 30
print(pessoa)

# adicionando novos valores
pessoa["nome"] = "Pedro"
print(pessoa)

# removendo os elementos
# pessoa.pop("nome")
# print(pessoa)

# usando del para remover
# del pessoa["idade"]
# print(pessoa)

# remove o dicionário completamente
# pessoa.clear()
# print(pessoa)


# percorrer o dicionário
for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
print(pessoa.keys())
print(pessoa.values())


# tem como ter um dicionário dentro de outro
alunos = {
    "aluno1": {"nome": "Alex", "nota": 8},
    "aluno2": {"nome": "Ana", "nota": 10}
}

print(alunos)
print(alunos["aluno2"])
print(alunos["aluno1"]["nome"])
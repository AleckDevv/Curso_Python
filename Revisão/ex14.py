pessoa = {"nome": "Alex", "idade": 15, "cidade": "teresina"}
# acessando a propriedade nome do objeto pessoa
print(pessoa["nome"])


# alterando valores
pessoa["nome"] = "maria"
print(pessoa)


# removendo elementos
# dos mesmo jeito que se remove em lista
# da pra remover com dicionários

pessoa.pop("cidade")  # removendo pelo nome da chave
del pessoa["nome"]  # removendo pela propriedade nome
pessoa.clear()  # remove tudo do dicionário


for chave in pessoa:
    print(chave, pessoa[chave])

print(pessoa.keys())  # pega as chaves do objeto
print(pessoa.values())  # pega os valores das chaves dos objetos


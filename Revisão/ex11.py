# dicionários

pessoa = {"nome": "alex", "idade": 25}

print(pessoa)
print(pessoa["idade"])

# caso uma chave não exista, podemos passar uma mensagem de erro

print(pessoa.get("profissão", "Não informado"))
print(pessoa.get("nome"))

pessoa["nome"] = "maria"
print(pessoa)

# remover elementos
# o pop aqui no py não remove o ultimo
# tem que passar o nome da propriedade
# pessoa.pop("nome")
# print(pessoa)
del pessoa["idade"]
print(pessoa)
pessoa.clear()
print(pessoa)

# percorrer um obejeto

pessoa2 = {"nome": "Alex", "idade": 24, "cidade": "São Paulo"}


for chave in pessoa2:
    print(chave, pessoa2[chave])

for chave, valor in pessoa2.items():
    print(f"{chave}: {valor}")
    

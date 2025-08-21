from functools import reduce

# Base de dados
produtos = [
    {"nome": "Notebook", "preco": 3000, "qtd": 4},
    {"nome": "Mouse", "preco": 100, "qtd": 10},
    {"nome": "Teclado", "preco": 200, "qtd": 6},
    {"nome": "Monitor", "preco": 1200, "qtd": 3},
    {"nome": "Cadeira Gamer", "preco": 1500, "qtd": 2},
]

faturamentos = list(map(lambda p: p["preco"] * p["qtd"], produtos))
print("Faturamento de cada produto:", faturamentos)

acima_2000 = list(filter(lambda p: p["preco"] * p["qtd"] > 2000, produtos))
print("Produtos com faturamento > 2000:", acima_2000)

total = reduce(lambda x, y: x + y, faturamentos)
print("Faturamento total:", total)

nomes_maiusculos = list(map(lambda p: p["nome"].upper(), produtos))
print("Nomes em maiúsculas:", nomes_maiusculos)

mais_vendido = reduce(lambda x, y: x if x["qtd"] > y["qtd"] else y, produtos)
print("Produto mais vendido em quantidade:", mais_vendido["nome"])


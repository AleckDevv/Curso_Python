produtos_loja = {
    "maçã": 2.50,
    "banana": 3.25,
    "pão": 1.50,
    "maizena": 100,
    "goma": 45.50,
    "azeite": 33.25,
}

carrinho = []


def adicionar_produto(nome):
    if nome in produtos_loja:
        valor = produtos_loja[nome]
        carrinho.append((nome, valor))
        return True, valor
    else:
        return False, None

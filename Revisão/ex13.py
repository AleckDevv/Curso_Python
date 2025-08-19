prudutos_loja = {
    "maçã": 2.5, 
    "banana": 3.0, 
    "pão": 1.5
}


def loja():
    saida = "========================\n"
    saida += "LOJA CEV\n"
    saida += "========================\n"
    saida += "NOSSOS PRODUTOS\n"

    for chave, valor in prudutos_loja.items():
        saida += f"Produto: {chave}: valor: {valor}R$\n"
    
    return saida


mostrar_produtos = loja()
print(mostrar_produtos)

if __name__ == "__main__":
    while True:
        try:
            produto_escolhido = input("Qual produto você quer? ")
            valor = prudutos_loja[produto_escolhido]
            print(f"Você escolheu {produto_escolhido}: {valor} R$")
        except KeyError:
            print("Produto inválido")
            
            
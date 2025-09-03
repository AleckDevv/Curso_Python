endereco_completo = "Rua das Flores, 123, Bairro Jardim, Cidade Exemplo - UF, 12345-678"

separar = endereco_completo.split(",")
rua = separar[0]
numero = separar[1]
cep = separar[4]
converter_numero = int(numero)

endereco_formatado = f"{rua}, {numero}, {cep}"
print(endereco_formatado)


preco_produtos = [10.4, 8.2, 7, 2.5, 50, 12.3]
total_produtos = round(sum(preco_produtos), 2)
mais_caro = max(preco_produtos)
mais_barato = min(preco_produtos)
print(total_produtos)
print(mais_caro, mais_barato)

dados_misturados = [10, True, "teste"]

for i in dados_misturados:
    verificar_tipo = type(i)
    print(verificar_tipo)


alunos = [("Ana", 95), ("Bruno", 7.0), ("Carla", 8.8)]
aluno2 = alunos[1]
print(aluno2)

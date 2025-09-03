import random

linhas = 5
colunas = 5

tesouro_linha = random.randint(0, linhas - 1)
tesouro_coluna = random.randint(0, colunas - 1)

print(f"O tesouro foi escondido na linha {tesouro_linha} e coluna {tesouro_coluna}.")
print("--- Iniciando a busca ---")

tesouro_encontrado = False

for linha_atual in range(linhas):

    for coluna_atual in range(colunas):

        print(f"Procurando na linha {linha_atual}, coluna {coluna_atual}...")

        if linha_atual == tesouro_linha and coluna_atual == tesouro_coluna:
            print("TESOURO ENCONTRADO!")

            tesouro_encontrado = True
            break

    if tesouro_encontrado:
        break

print("\nBusca encerrada.")

# listas

notas = [10, 20, 30, 12, 1, 3, 4, 5, 6]
print(notas[:2])  # tudo a direita a partir do indice 2 não é exibido
print(notas[0:4])  # da mesma forma, porém só pega os quatro primeiros elementos


# ordenar listas
ordenar = sorted(notas)
print(ordenar)
# deixar em ordem reversa
reverso = sorted(notas, reverse=True)
print(reverso)


# funções matemáticas
total = sum(notas)
print(total)
menor_valor = min(notas)
print(menor_valor)
maior_valor = max(notas)
print(maior_valor)

# adicionar valores em lista
nome = "teste"
notas.append(nome)
print(notas)

# remover da lista
notas.pop()
print(notas)

# removendo por posição
notas.pop(3)
print(notas)

# verificar se existe algum valor
print(not 12 in notas)  # só fazendo um teste para ficar true
print(12 in notas)


planetas = ["Mercúrio", "Vênus", "Saturno", "Urano", "Neturno"]

for p in planetas:
    print(p)

bebidas = []
for i in range(3):
    print("digite uma bebida: ")
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()
print("escolha: ")
for b in bebidas:
    print(b)

pontuacoes = []

for p in range(5):
    pontuacao = int(input("Digite 5 pontuações: "))
    pontuacoes.append(pontuacao)
    print(f"pontuações enseridas: {pontuacoes}")

maior_pontuacao = max(pontuacoes)
print(f"a maior pontuação é: {maior_pontuacao}")
menor_pontuacao = min(pontuacoes)
print(f"a menor pontuação foi: {menor_pontuacao}")
calculo_total = sum(pontuacoes)
print(f"somatório total das pontuações: {calculo_total}")

ranking_pontuacoes = sorted(pontuacoes, reverse=True)
print(f"ranking geral das pontuações: {ranking_pontuacoes}")

pontuacao_especifica = int(input("Digite uma pontuação: "))

if pontuacao_especifica in pontuacoes:
    print(f"a pontuação {pontuacao_especifica} está no ranking")
else:
    print(f"a pontução {pontuacao_especifica} não está no ranking")

ranking_final = pontuacoes[:3]
print(f"As maiores pontuações foram: {ranking_final}")

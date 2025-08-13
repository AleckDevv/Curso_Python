"""
Exercício 1 — Removendo duplicatas
Peça ao usuário para digitar 5 nomes.
Coloque todos em um set e mostre apenas os nomes únicos.
"""

""" nomes = set()
for i in range(5):
    nome = input("digite um nome: ")
    nomes.add(nome)
print(nomes) """

""" 
Exercício 2 — Conferindo presença
Crie um set com os nomes dos alunos que compareceram à aula.
Depois, peça o nome de um aluno e verifique se ele está presente no set.
"""

""" alunos_presentes = {"pedro", "ana", "maria", "alex"}
while True:
    print("verificar alunos presentes")
    aluno = input("Qual aluno você quer ver se está presente? ")

    if aluno.lower() == "sair":
        break

    if aluno in alunos_presentes:
        print(f"o aluno {aluno} está presente...")
    else:
        print("o aluno não veio") """


""" 
Exercício 3 — União de listas
Dadas duas listas de números, converta ambas para sets e mostre a união entre elas.
"""
numeros1 = set([1, 2, 3, 4, 5])
numeros2 = set([6, 7, 8, 9, 20])

uniao = numeros1.union(numeros2)
print(uniao)


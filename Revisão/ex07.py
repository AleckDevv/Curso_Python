<<<<<<< HEAD
notas = [10, 20, 30]
notas2 = [1, 2, 3, 4, 5, ["alex", "soares", "lopes"]]
print(notas)
""" 
acessando o primeiro elemento da lista
"""
print(notas2[0])


juntar = notas + notas2
""" 
juntando as duas listas
"""
print(juntar)

print(notas2[5][1])
""" 
acessando a segunda lista dentro do array
e pegando o primeiro elemento dessa lista secundária
"""

print(notas2[3:4])
""" 
fazendo uma fatia nos elementos da lista
tira os 3 primeiros elementos e exibe somente o elemento desejado. ou seja, [3:4] o três é o ínicio do corte, e o 4 é o fim. Que é o elemento que vai ser
exibido
"""
print(notas2[:])
""" 
dessa forma, exibe todos os elementos
"""

nomes = ["pedro", "bruna", "ana", "neide"]
ordenada = sorted(nomes)

""" 
o sorted retorna uma lista ordenada em ordem
alfabética ou em ordem crescente
"""
print(ordenada)


reveso = sorted(nomes, reverse=True)
""" 
para deixar em ordem reversa, a gente usa o sorted
passando a lista que vair ser ordenada e como segundo
parâmetro, habilita o reverse=True
"""
print(reveso)


""" 
fazer um somatório total
"""
numeros = [1, 2, 5, 6, 8, 10]
soma = sum(numeros)
print(soma)

""" 
saber o valor maior
"""
maior = max(numeros)
print(maior)

""" 
saber o menor número
"""
menor = min(numeros)
print(menor)

""" 
add um novo valor ou elemento a lista
dessa forma ele add ao final do elemento
"""
numeros.append(40)
print(numeros)

""" 
remover o último elemento
"""
numeros.pop()
print(numeros)


=======
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


for numero in range(1, 11):
    print(f"Tabuada do Número: {numero}")

    for multiplicar in range(1, 11):
        print(f" {numero} x {multiplicar} = {numero * multiplicar}")
        print("-" * 20)
>>>>>>> 85681606e5d58da60150053cb02e167353662b6a

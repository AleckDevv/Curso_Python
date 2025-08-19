<<<<<<< HEAD
"""
importando a biblioteca random e renomendo o nome
dela
"""

import random as aleatorios

numeros = aleatorios.randint(1, 10)
print(numeros)
""" 
gerando um número aleatório inteiro de 1 a 10
isso inclui o próprio 10
"""

n1 = aleatorios.random()
print(n1)
""" 
gerando um número decimail
"""

n2 = aleatorios.uniform(5, 10)
print(n2)
""" 
gerando um número decial entre 5 e 10
"""

cores = ["preto", "azul", "verde"]
pegar_cor_aleatoria = aleatorios.choice(cores)
print(pegar_cor_aleatoria)
""" 
com o choice, é possível selecinar aleatoriamente um 
elemento de uma lista. e como parâmetro desse choice
a gente passa os elemento que contem dentro da lista
"""


cartas = ["a", "b", "c", "d"]
embaralahr = aleatorios.shuffle(cartas)
print(embaralahr)
""" 
o shuffle() embaralha a ordem dos elementos
e como parâmetro, a gente passa a lista que contem
os elementos
"""

numero_secreto = aleatorios.randint(1, 10)
tentativa = int(input("adivinhe um número de 1 a 10: "))

if tentativa == numero_secreto:
    print("acertou")
else:
    print(f"errou... o número era {numero_secreto}")
""" 
teste de gerador de número aleatório
onde a pessoa tem que escolher um número e ver se 
era o certo.

nesse exemplo, eu crio uma variável para guardar
o momento em que o número é gerado.
pois quando for verificar no if, o número que o user
digitou, vai ser comparado com o número aleatório que foi gerado e quardado na variável. Dessa forma, é
possivel acertar o número. 
"""
=======
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f"contando: {contador}")
""" 
o continue pula a execução do próximo laço
nesse exemplo de cima, quando a condição for
igual a 3, ele pula o 3 e passa para a próxima execução
"""


""" 
se não tiver um incremento no laço
pode dar loop infinito
"""

senha_correta = 1234
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = int(input("Digite a senha: "))
    if senha_digitada != senha_correta:
        print("Senha incorreta, tente novamente.")

print("Acesso permitido!")


while True:
    comando = input("digite 'sair' para parar: ")
    if comando.lower() == "sair":
        break
print(f"você digitou: {comando}")
>>>>>>> 85681606e5d58da60150053cb02e167353662b6a

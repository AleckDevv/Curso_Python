lista = [1, 2, 3, 4]
contador = 0

for n in lista:
    print(n)


for i in range(0, 11, 2):
    print(i)

n1 = int(input("Digite um número: "))

for b in range(0, n1 + 1):
    print(b)


# tabuada
# pede para o usuário digitar a tabuada
numero = int(input("Digite um número: "))

# faz um loop começando do 1 e parando no 10
for i in range(1, 11):

    # cria uma variável resultado que vai pegar o número que o user
    # digitou e vai multiplicar pela iteração atual do for
    resultado = numero * i

    # exibindo em tela o número que o user digitou
    # exibindo o i com a iteração da multiplicação com o número digitado
    print(f"{numero} x {i} = {resultado}")


regressiva = int(input("digite uma contagem regressiva: "))

for n in range(regressiva, -1, -1):
    print(n)

n1 = int(input("digite um número:"))
n2 = int(input("digite um número:"))
n3 = int(input("digite um número:"))
n4 = int(input("digite um número:"))
n5 = int(input("digite um número:"))


lista = [n1, n2, n3, n4, n5]
contador = 0

for n in lista:
    contador += n
print(contador)

# versão com sum()
lista = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}° número: "))
    lista.append(numero)
print(f"a soma total é: {sum(lista)}")

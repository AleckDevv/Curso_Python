# definindo variáveis em python
nome = "Alex"
idade = 25
altura = 1.75
tem_carteira = True
print(f"Nome:{nome.upper()}, Idade: {idade}, Altura{altura}, CNH: {tem_carteira}")

# converter strig para maiúsculas ou minúsculas
# .upper() .lower() -> Métodos que convertem string para maiúsculas ou minúsculas

# método len() que mostrar o tamanho de uma string
print(len(nome))

# Tipos de dados
# 1 -> str = String
# o método type() exibe o tipo de dados
print(type(nome))

# 2 -> int = Inteiro
print(type(idade))

""" 
Pode ser usado os operadores matemáticos para fazer operações
+ Adição
- Subtração
* Multiplicação
/ Divisão
% Resto da divisão
// Divisão inteira
** Exponenciação
"""
# adição
n1 = 10
n2 = 5
adicao = n1 + n2
subracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto_divisao = n1 % n2
divisao_inteira = n1 // n2
exponenciacao = n1**n2
print(f"Adição: {adicao}")
print(f"Subtração: {subracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da Divisão: {resto_divisao}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Exponenciação: {exponenciacao}")

# 3 -> float = Ponto flutuante
altura2 = 1.80
print(type(altura2))

# 4 -> bool = Booleano - verdadeiro ou falso
tem_carteira2 = False
esta_chobendo = False
""" 
Tipo bool muito usado em condições com if else ou elif
exemplo rápido
"""
if tem_carteira2:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# 5 -> list = Lista ou array
frutas = ["banana", "uva", "Maçã", [1, 2, 3, 4, 5]]
print(frutas)
# acessando os elementos da lista
print(frutas[0])
# acessando array dentro de outro
print(frutas[3][2])

# 6 -> Dicionário ou objeto
usuario = {"nome": "Maria", "idade": 50, "email": "maria@email.com"}
# acessando os elemento
""" 
ao contrário do js que a gente acessa as propriedades com . aqui é com [] chaves
"""
print(usuario["email"])

# Conversão de tipos de dados
idade2 = "15"
print(type(idade2))
idade2 = int(idade2)
print(type(idade2))
""" 
da pra fazer com outros tipos, basta usar:
str()
int()
float()
Passando a variável como parâmetro
"""
a = 10
b = "teste"
print(isinstance(a, int))
""" 
isinstance() verifica o tipo de dado passado, ela recebe
dois parâmetros. O primeiro é o valor da variáveis salva
e o segundo é qual tipo que vai ser verificado. E retorna
verdaderio ou falso
"""


# Prática

nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: "))

if idade2 >= 18:
    print(f"{nome2}, você é maior de idade")
else:
    print(f"{nome2}, você é menor de idade")

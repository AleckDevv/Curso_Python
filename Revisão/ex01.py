nome = "ana"
idade = 22
print(idade + 1)
altura = 1.75
tem_carteira = False

if __name__ == "__main__":
    print(type(nome))
    print(type(idade))
    print(type(altura))
    print(type(tem_carteira))
    # funções de string
    # print(nome.upper())
    print(nome.lower)
    # saber o tamanho
    print(len(nome))

# listas
frutas = ["maçã", "uva", "pêra"]
print(frutas)
# acessar por indice
print(frutas[0])

# dicionário ou objeto
usuario = {"nome": "alex", "idade": 25, "email": "alex@gmail.com"}
# acessando o dicionário
print(usuario["nome"])
print(usuario["email"])
print(usuario["idade"])

# conversão de tipos
idade = "24"
idade_int = int(idade)
# outros exemplos
str(123)
# vira string

int("100")
# vira inteiro

# vira float
float("9.5")



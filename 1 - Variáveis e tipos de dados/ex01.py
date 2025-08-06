# Cadastro de usuário simples
nome = "bruno"
idade = 10
matriculado = True
status = f"{nome}, {idade}, {matriculado}"
print(status)

# conversão de tipos
valor = input("digite um valor: ")
print(f"valor antes da conversão {type(valor)}")
dobro_idade = idade * 2
print(f"Idade ao quadrado: {dobro_idade}")
conversao = int(valor)
print(f"valor depois da conversão {type(conversao)}")


# operações com vairáveis
n1 = 10
n2 = 5
n3 = 4
soma = n1 + n2 + n3
mult = n1 * n2 + n3
print(soma)
print(mult)

# validação de tipo
dado = input("Digite um valor: ")
if isinstance(dado, str):
    conv = int(dado)
    print(f"antes de converter o tipo era: {type(dado)}")
    print(f"depois de converter o tipo agora é: {type(conv)}")


# função de validação
def validadar_dado(dado):
    if type(dado) == int:
        print("É um número inteiro")
    elif type(dado) == str:
        print("É um texto")
    else:
        print("Tipo não encontrado")


validadar_dado(10)

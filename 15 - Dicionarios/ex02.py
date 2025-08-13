pessoa = {"nome": "Ana", "idade": 22, "cidade": "Teresina"}

print(pessoa["nome"])
pessoa["idade"] = 25
pessoa["profissao"] = "Auxiliar"
print(pessoa)


frase_dict = {}

frase = input("Digite uma frase: ")
palavras = frase.split()


for palavra in palavras:
    if palavra in frase_dict:
        frase_dict[palavra] += 1
    else:
        frase_dict[palavra] = 1
print(frase_dict)

pessoa_contatos = {}


nome = input("Digite o seu nome: ")
telefone = int(input("Digite o seu telefone: "))
pessoa_contatos[nome] = telefone


for i in range(3):
    nome = input(f"Digite o nome do contato {i+1}: ")
    telefone = int(input(f"Digite o telefone do contato {i+1}: "))
    pessoa_contatos[nome] = telefone

while True:
    print("VERIFICAR O CONTATO NA LISTA")
    verificacao = input("Digite o nome de um contato: ")

    if verificacao.lower() == "sair":
        break

    if verificacao in pessoa_contatos:
        print(f"o contato {verificacao} tem o telefone; {pessoa_contatos[verificacao]}")
    else:
        print("contato não existe...")


print(pessoa_contatos)

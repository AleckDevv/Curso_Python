with open("./tarefas.txt", "w") as arquivo:
    arquivo.write("testando manipulação de arquivos")
print("arquivo de tarefas criado com suceso")

with open("./tarefas.txt", "a") as arquivo2:
    arquivo2.write("tomar café")
print("sucesso")

with open("tarefas.txt", "r+") as arquivo3:
    conteudo_completo = arquivo3.read()
print("---conteúdo completo---")
print(conteudo_completo)

print("\n --- lendo linha por linha---")
with open("tarefas.txt", "r") as arquivo4:
    for linha in arquivo4:
        print(f"tarefa: {linha.strip()}")

with open("tarefas.txt", "r") as arquivo5:
    lista_de_tarefa = arquivo5.readlines()
print("\n---conteúdo em formato de lista")
print(lista_de_tarefa)

print(f"a primeira tarefa é: {lista_de_tarefa[0].strip()}")

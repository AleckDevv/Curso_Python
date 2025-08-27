# manipulação de arquivos de texto

"""manipulador = open("arquivo.txt", "r", encoding="utf-8")"""
""" print(f"Método read(): ")
print(manipulador.read()) """


""" print(f"Método readline(): ")
print(manipulador.readline()) """

""" print(f"Método readline(): ")
print(manipulador.readlines()) """

""" texto = input("qual termo você quer procurar no arquivo: ") """
"""manipulador = open("arquivos.txt", "r", encoding="utf-8")"""
""" try:
    manipulador = open("C:\\Users\\alex.lopes\\Documents", "r", encoding="utf-8")

    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print(f"a string foi encontrada")
            print(linha)
        else:
            print("string não encontrada")
except IOError:
    print("Não foi possivel ler o arquivo")
else:
    manipulador.close() """

texto = "Texto de add texto no arquivo"
try:
    manipulador = open("arquivo.txt", "w" ,encoding="utf-8")

    manipulador.write("Alex Soares Lopes\n")
    manipulador.write("Texto de texto")
    manipulador.write(texto)
except IOError:
    print("Não foi possivel ler o arquivo")
else:
    manipulador.close()

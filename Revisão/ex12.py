# tuplas

"""
uma tupla não pode ter seu valor alterado
ou seja, é imutavel
"""

times = ("Barça", "Real M", "Manchester")
print(times)

# da pra fazer acesso igual com listas
print(times[0])

# desempacotamento de tuplas
pessoa = ("alex", 24, "brasil")
nome, idade, pais = pessoa

print(nome)
print(idade)
print(pais)


catalogo_estelar = [
    ("Sirius", "Cão Maior", 8.6),
    ("Betelgeuse", "Órion", 642.5),
    ("Vega", "Lira", 25.04),
]

for registro in catalogo_estelar:
    print(
        f"Estrela: {registro[0]} | Constelação: {registro[1]} | Distância: {registro[2]} anos-luz"
    )
    print("-------------------------------------------")

estrela = str(input("digite uma estrela: "))

tupla_encontrada = None

for registro in catalogo_estelar:
    tupla_encontrada = registro

    if registro[0] == estrela:
        tupla_encontrada = registro
        break


if estrela in catalogo_estelar:
    nome, constelacao, distancia = tupla_encontrada
    print(
        f"A estrela {estrela}, que pertence à constelação {constelacao} está a {distancia} anos luz da terra"
    )
else:
    print("estrela não identificada...")

teste = {"teste1", "teste1", "teste1", "teste1", "teste2", "teste3"}
transformar_set = set(teste)

print(transformar_set)
""" 
um set remove duplicados
só aceita números, strings e tuplas
"""

numeros = set(
    [
        1,
        2,
        3,
        4,
        5,
        5,
        5,
        6,
        7,
    ]
)

print(numeros)

s = {1, 2, 2, 3}
print(s)
s.add(4)
print(s)

s.remove(2)
s.discard(4)
print(s)
s.clear()
print(s)
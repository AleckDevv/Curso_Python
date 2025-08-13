planeta_anao = {"plutão", "ceres", "eris", "haumea", "makemake"}
print(planeta_anao)

print(len(planeta_anao))

print("ceres" in planeta_anao)
print("lua" in planeta_anao)

print("lua" not in planeta_anao)

for astro in planeta_anao:
    print(astro.upper())

astros = ["lua", "vênus", "cirius", "marte", "lua"]
print(astros)
astros_set = set(astros)
print(astros_set)


astros1 = {"lua", "vênus", "cirius", "marte", "lua", "io"}
astros2 = {"lua", "vênus", "cirius", "marte", "lua", "harlley"}

print(astros1 == astros2)
print(astros1 != astros2)
print(astros1.union(astros2))

print(astros1.intersection(astros2))
print(astros1.symmetric_difference(astros2))

astros1.add("urano")
astros1.add("sol")
print(astros1)

astros1.remove("io")
print(astros1)

# remove um item aleatório
astros1.pop()
print(astros1)

# excluir todo o set
astros1.clear()
print(astros1)
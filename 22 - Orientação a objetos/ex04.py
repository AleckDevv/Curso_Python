class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

    def desativar(self):
        self.ativo = True

        if self.ativo == False:
            print("pessoa desativada com sucesso")
        elif self.ativo == True:
            print("A pessoa foi ativada novamente")
        else:
            print("Erro não reconhecido")


if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "12234")
    print(pessoa1.nome)
    print(pessoa1.cpf)
    print(pessoa1.sexo)

    pessoa1.desativar()

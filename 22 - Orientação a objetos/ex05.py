class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def saudacao(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"


pessoa1 = Pessoa("Pedro", 25, "pedro@teste.com")
print(pessoa1.saudacao())

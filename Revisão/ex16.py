class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá {self.nome} você tem {self.idade}"


pessoa1 = Pessoa("Alex", 19)
print(pessoa1.apresentar())


class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        return valor

    def mostrar_saldo(self):
        return f"saldo: {self.__saldo}"


conta1 = Conta(1000)
valor_retornado = conta1.depositar(200)
saldo = conta1.mostrar_saldo()

print(f"valor depositado {valor_retornado}")
print(f"saldo total da conta {saldo}")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @property.getter
    def get_exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class ContaBancaria:
    def __init__(self, saldo):
        # encapsulando o atributo
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def ver_saldo(self):
        return self.__saldo


class Veiculo:
    def __init__(self, rodas):
        self.rodas = rodas


class Carro2(Veiculo):
    def __init__(self, rodas, marca):
        super().__init__(rodas)
        self.marca = marca


class Passaro:
    def falar(self):
        print("piu")


class Gato:
    def falar(self):
        print("miau")


if __name__ == "__main__":
    carro1 = Carro("Honda", "Marea")
    carro1.get_exibir_informacoes()

    conta1 = ContaBancaria(1000)
    print(conta1.ver_saldo())

    passaro = Passaro()
    gato = Gato()

    print(passaro.falar())
    print(gato.falar())

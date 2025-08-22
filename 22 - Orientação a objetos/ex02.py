class Veiculo:
    # construtor
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.__numero_registro = None  # encapsulamento

    # aqui é uma ação que a classe pode fazer
    def movimentar(self):
        print("O carro está ligado")

    # métodos acessores get e set
    def get_fabr_modelo(self):
        """Retorna fabricante e modelo"""
        return f"Fabricante: {self.fabricante}, Modelo: {self.modelo}"

    def set_numero_registro(self, numero):
        """Define o número de registro"""
        self.__numero_registro = numero

    def get_numero_registro(self):
        """Retorna o número de registro"""
        return self.__numero_registro


class Carro(Veiculo):
    # o método init será herdado

    def ligar(self):
        print("Girou a chave do carro")


class Motocicleta(Veiculo):
    def movimentar(self):
        print(f"carro a 100km/h")


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def categoria(self):
        return self.__cat

    def movimentar(self):
        print("está voando")


if __name__ == "__main__":
    veiculo1 = Veiculo("GM", "Cadillac")

    # usando os métodos
    veiculo1.movimentar()
    print(veiculo1.get_fabr_modelo())  # mostra fabricante e modelo

    veiculo1.set_numero_registro("29822-0")
    print(f"O número do registro é {veiculo1.get_numero_registro()}")

    carro1 = Carro("Volkswagen", "Polo")
    carro1.ligar()
    carro1.get_fabr_modelo()

    carro2 = Carro("Audi", "A5 Sportback")
    carro2.ligar()
    carro2.get_fabr_modelo()

    moto = Motocicleta("Harley-Davidson", "Nigthster Special")
    moto.movimentar()
    moto.get_fabr_modelo()

    aviao = Aviao("Boeing", "745", "Comercial")
    aviao.movimentar()
    print(f"{aviao.get_fabr_modelo()}")
    print(f"{aviao.categoria()}")

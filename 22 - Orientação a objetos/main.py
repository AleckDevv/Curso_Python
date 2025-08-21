class Veiculo:
    def movimento(self):
        print("Carro ligado")

    # def __init__ é o construtor da classe
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        # criar encapsulamento
        self.__numero_registro = None

    # criando métodos especiais acessores get e set
    def get_registro(self):
        print(f"modelo: {self.__numero_registro}")

    def set_registro(self, registro):
        self.__numero_registro = registro

    def get_num_registro(self):
        return self.__numero_registro

# herança
class Carro(Veiculo):
    def movimento(self):
        return super().movimento()


if __name__ == "__main__":
    veiculo = Veiculo("Gm", "Cadillac Escalade")
    veiculo.movimento()

    # acessar dessa forma, não é o ideal
    # pra isso cria os métodos acessores; get e set
   """  print(f"Nome do fabricante: {veiculo.fabricante}")
    print(f"Nome do modelo: {veiculo.modelo}")
    veiculo.set_registro("293893-9")
    veiculo.get_registro() """
    
    carro = Carro("Volkswagen" ,"polo")
    carro.movimento()
    carro.get_num_registro()

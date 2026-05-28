class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

    def exibir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


class CarroEletrico(Carro):

    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)

        self.autonomia_bateria = autonomia_bateria

    def exibir_bateria(self):
        print("Autonomia:", self.autonomia_bateria, "km")


carro1 = Carro("Toyota", "Corolla")

print(carro1)

tesla = CarroEletrico("Tesla", "Model S", 600)

tesla.exibir_info()
tesla.exibir_bateria()
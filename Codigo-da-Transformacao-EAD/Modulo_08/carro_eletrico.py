"""
Atividade 2 — Herança: CarroEletrico herda de Carro
Adiciona autonomia_bateria e método carregar().
"""


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_info(self):
        print(f"  Marca:  {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Ano:    {self.ano}")
        print(f"  Cor:    {self.cor}")

    def buzinar(self):
        print(f"🚗 {self.marca} {self.modelo}: Beep beep!")


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, cor, autonomia_bateria):
        super().__init__(marca, modelo, ano, cor)  # herda atributos do Carro
        self.autonomia_bateria = autonomia_bateria  # atributo exclusivo

    def exibir_info(self):
        print("=" * 40)
        print("     INFORMAÇÕES DO CARRO ELÉTRICO")
        print("=" * 40)
        super().exibir_info()  # chama o exibir_info do Carro
        print(f"  🔋 Autonomia: {self.autonomia_bateria} km")
        print("=" * 40)

    def carregar(self):
        print(f"⚡ {self.marca} {self.modelo} está carregando a bateria...")
        print(f"   Autonomia após carga: {self.autonomia_bateria} km")


# --- Testando ---
carro_normal = Carro("Toyota", "Corolla", 2022, "Prata")
carro_eletrico = CarroEletrico("Tesla", "Model 3", 2024, "Branco", 560)

print("\n🚗 Carro Normal:")
carro_normal.exibir_info()

print("\n⚡ Carro Elétrico:")
carro_eletrico.exibir_info()
carro_eletrico.carregar()
carro_eletrico.buzinar()  # método herdado do Carro

"""
Atividade 1 — Classe Carro
Representa um veículo com marca, modelo, ano e cor.
"""


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_info(self):
        print("=" * 40)
        print("       INFORMAÇÕES DO CARRO")
        print("=" * 40)
        print(f"  Marca:  {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Ano:    {self.ano}")
        print(f"  Cor:    {self.cor}")
        print("=" * 40)

    def buzinar(self):
        print(f"🚗 {self.marca} {self.modelo}: Beep beep!")


# --- Testando a classe ---
carro1 = Carro("Toyota", "Corolla", 2022, "Prata")
carro2 = Carro("Honda", "Civic", 2023, "Preto")

carro1.exibir_info()
carro2.exibir_info()

carro1.buzinar()
carro2.buzinar()

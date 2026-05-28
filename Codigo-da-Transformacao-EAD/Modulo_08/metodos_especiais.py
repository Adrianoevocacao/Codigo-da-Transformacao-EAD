"""
Atividade 3 — Métodos Especiais: __init__ e __str__
Personaliza inicialização e representação de objetos como string.
"""


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        """Inicializa os atributos do carro."""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __str__(self):
        """Retorna uma representação legível do objeto."""
        return f"🚗 {self.marca} {self.modelo} ({self.ano}) — Cor: {self.cor}"

    def __repr__(self):
        """Retorna uma representação técnica do objeto."""
        return f"Carro(marca='{self.marca}', modelo='{self.modelo}', ano={self.ano}, cor='{self.cor}')"

    def exibir_info(self):
        print("=" * 40)
        print(f"  {self}")
        print("=" * 40)


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, cor, autonomia_bateria):
        super().__init__(marca, modelo, ano, cor)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        """Sobrescreve o __str__ para incluir a bateria."""
        return (f"⚡ {self.marca} {self.modelo} ({self.ano}) — "
                f"Cor: {self.cor} | Bateria: {self.autonomia_bateria} km")


# --- Testando os métodos especiais ---
carro1 = Carro("Ford", "Mustang", 2021, "Vermelho")
carro2 = CarroEletrico("Tesla", "Model S", 2024, "Cinza", 650)

print("🔎 Usando print() — chama o __str__:")
print(carro1)
print(carro2)

print("\n🔎 Usando repr() — chama o __repr__:")
print(repr(carro1))

print("\n🔎 Usando em lista:")
frota = [carro1, carro2]
for c in frota:
    print(f"  → {c}")

print("\n🔎 Usando exibir_info():")
carro1.exibir_info()
carro2.exibir_info()

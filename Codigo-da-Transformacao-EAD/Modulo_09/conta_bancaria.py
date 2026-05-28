"""
Atividade 2 — Exceção Personalizada: SaldoInsuficienteError
Simula operações bancárias com exceções customizadas.
"""


# --- Exceção personalizada ---
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado
        super().__init__(
            f"Saldo insuficiente! Saldo: R$ {saldo_atual:.2f} | "
            f"Solicitado: R$ {valor_solicitado:.2f}"
        )


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("❌ O valor do depósito deve ser positivo!")
        self.saldo += valor
        self.extrato.append(f"  ➕ Depósito:  R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado! Saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("❌ O valor do saque deve ser positivo!")
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        self.extrato.append(f"  ➖ Saque:     R$ {valor:.2f}")
        print(f"✅ Saque de R$ {valor:.2f} realizado! Saldo: R$ {self.saldo:.2f}")

    def ver_extrato(self):
        print(f"\n📋 EXTRATO — {self.titular}")
        print("=" * 40)
        if not self.extrato:
            print("  Nenhuma movimentação.")
        for linha in self.extrato:
            print(linha)
        print(f"  {'─' * 30}")
        print(f"  💰 Saldo atual: R$ {self.saldo:.2f}")
        print("=" * 40)


# --- Testando ---
conta = ContaBancaria("Ana Silva", saldo_inicial=500.0)

print("=" * 40)
print("     SIMULAÇÃO BANCÁRIA")
print("=" * 40)

# Depósito normal
conta.depositar(200.0)

# Saque normal
conta.sacar(100.0)

# Saque com saldo insuficiente — captura a exceção personalizada
try:
    conta.sacar(1000.0)
except SaldoInsuficienteError as e:
    print(f"❌ Erro: {e}")

# Depósito inválido — captura ValueError
try:
    conta.depositar(-50)
except ValueError as e:
    print(e)

# Extrato final
conta.ver_extrato()

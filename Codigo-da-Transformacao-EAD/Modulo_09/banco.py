class SaldoInsuficienteError(Exception):
    pass


saldo = 100
saque = 200

try:

    if saque > saldo:
        raise SaldoInsuficienteError

    saldo -= saque

    print("Saque realizado!")

except SaldoInsuficienteError:

    print("ERRO: saldo insuficiente!")
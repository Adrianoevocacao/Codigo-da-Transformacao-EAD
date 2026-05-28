"""
Atividade 1 — Try-Except: Calculadora com tratamento de erros
Trata divisão por zero e entradas inválidas.
"""


def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "❌ Erro: Divisão por zero não é permitida!"


def calculadora():
    print("=" * 40)
    print("     CALCULADORA COM TRY-EXCEPT")
    print("=" * 40)

    operacoes = {
        "1": ("Soma",        lambda a, b: a + b),
        "2": ("Subtração",   lambda a, b: a - b),
        "3": ("Multiplicação", lambda a, b: a * b),
        "4": ("Divisão",     dividir),
    }

    while True:
        print("\nEscolha a operação:")
        for k, (nome, _) in operacoes.items():
            print(f"  {k}. {nome}")
        print("  0. Sair")

        opcao = input("\nOpção: ").strip()
        if opcao == "0":
            print("👋 Encerrando calculadora.")
            break
        if opcao not in operacoes:
            print("⚠️  Opção inválida!")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
            continue

        nome, func = operacoes[opcao]
        resultado = func(a, b)
        print(f"\n✅ {nome} de {a} e {b} = {resultado}")


if __name__ == "__main__":
    calculadora()

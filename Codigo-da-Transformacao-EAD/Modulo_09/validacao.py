"""
Atividade 3 — Validação de Entradas do Usuário
Garante que os dados fornecidos sejam válidos antes de processar.
"""


def validar_idade(idade_str):
    """Valida que a idade é um número inteiro positivo."""
    try:
        idade = int(idade_str)
        if idade <= 0:
            raise ValueError("A idade deve ser um número positivo.")
        if idade > 130:
            raise ValueError("Idade inválida: valor muito alto.")
        return idade
    except ValueError as e:
        raise ValueError(f"❌ Idade inválida: {e}")


def validar_nome(nome):
    """Valida que o nome tem pelo menos 2 caracteres e só letras/espaços."""
    nome = nome.strip()
    if len(nome) < 2:
        raise ValueError("❌ Nome inválido: deve ter pelo menos 2 caracteres.")
    if not all(c.isalpha() or c.isspace() for c in nome):
        raise ValueError("❌ Nome inválido: use apenas letras e espaços.")
    return nome.title()


def validar_email(email):
    """Validação básica de email."""
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("❌ Email inválido: formato esperado usuario@dominio.com")
    return email.lower()


def validar_salario(salario_str):
    """Valida que o salário é um número positivo."""
    try:
        salario = float(salario_str)
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        return salario
    except ValueError:
        raise ValueError("❌ Salário inválido: digite um número válido.")


def cadastrar_usuario():
    print("=" * 45)
    print("     CADASTRO COM VALIDAÇÃO DE DADOS")
    print("=" * 45)

    campos = [
        ("Nome completo", validar_nome),
        ("Idade",         validar_idade),
        ("Email",         validar_email),
        ("Salário (R$)",  validar_salario),
    ]

    dados = {}
    for campo, validador in campos:
        while True:
            entrada = input(f"\n{campo}: ").strip()
            try:
                dados[campo] = validador(entrada)
                print(f"✅ {campo} válido!")
                break
            except ValueError as e:
                print(e)
                print("   Tente novamente.")

    print("\n" + "=" * 45)
    print("     ✅ CADASTRO REALIZADO COM SUCESSO!")
    print("=" * 45)
    for campo, valor in dados.items():
        if campo == "Salário (R$)":
            print(f"  {campo}: R$ {valor:.2f}")
        else:
            print(f"  {campo}: {valor}")
    print("=" * 45)


if __name__ == "__main__":
    cadastrar_usuario()

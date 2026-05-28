"""
Desafio Extra — Sistema de Login
Trata credenciais inválidas e permite múltiplas tentativas.
"""


# --- Exceções personalizadas ---
class CredenciaisInvalidasError(Exception):
    def __init__(self, tentativas_restantes):
        self.tentativas_restantes = tentativas_restantes
        super().__init__(
            f"Usuário ou senha incorretos! "
            f"Tentativas restantes: {tentativas_restantes}"
        )


class ContaBloqueadaError(Exception):
    def __init__(self):
        super().__init__("🔒 Conta bloqueada após 3 tentativas incorretas!")


# --- Banco de usuários (simulado) ---
USUARIOS = {
    "ana@email.com":    "senha123",
    "carlos@email.com": "abc456",
    "admin":            "admin2024",
}

MAX_TENTATIVAS = 3


def fazer_login(usuario, senha, tentativas_restantes):
    """Verifica as credenciais e lança exceções personalizadas."""
    if usuario not in USUARIOS or USUARIOS[usuario] != senha:
        raise CredenciaisInvalidasError(tentativas_restantes)


def sistema_login():
    print("=" * 45)
    print("         🔐 SISTEMA DE LOGIN")
    print("=" * 45)
    print("Usuários disponíveis para teste:")
    print("  ana@email.com    → senha: senha123")
    print("  carlos@email.com → senha: abc456")
    print("  admin            → senha: admin2024")
    print("=" * 45)

    tentativas = 0
    bloqueado = False

    while tentativas < MAX_TENTATIVAS:
        tentativas_restantes = MAX_TENTATIVAS - tentativas

        print(f"\n🔑 Tentativa {tentativas + 1} de {MAX_TENTATIVAS}")
        usuario = input("Usuário: ").strip()
        senha   = input("Senha:   ").strip()

        try:
            fazer_login(usuario, senha, tentativas_restantes - 1)
            print(f"\n✅ Login realizado com sucesso! Bem-vindo, {usuario}!")
            return

        except CredenciaisInvalidasError as e:
            tentativas += 1
            print(f"❌ {e}")

            if tentativas == MAX_TENTATIVAS:
                bloqueado = True

    if bloqueado:
        try:
            raise ContaBloqueadaError()
        except ContaBloqueadaError as e:
            print(f"\n{e}")
            print("Entre em contato com o suporte para desbloquear.")


if __name__ == "__main__":
    sistema_login()

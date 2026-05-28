"""
Atividade 2 - Biblioteca Externa: Faker
Gera dados falsos como nomes, emails, endereços e datas.
Para instalar: pip install faker
"""

from faker import Faker
from datetime import datetime

fake = Faker("pt_BR")  # Faker em português do Brasil

print("=" * 45)
print("   GERADOR DE DADOS COM FAKER")
print("=" * 45)

print("\n👤 PESSOAS GERADAS ALEATORIAMENTE:")
print("-" * 45)
for i in range(3):
    print(f"\nPessoa {i + 1}:")
    print(f"  Nome:     {fake.name()}")
    print(f"  Email:    {fake.email()}")
    print(f"  Telefone: {fake.phone_number()}")
    print(f"  CPF:      {fake.cpf()}")
    print(f"  Cidade:   {fake.city()} - {fake.state_abbr()}")
    print(f"  Endereço: {fake.street_address()}")

print("\n📅 DATA E HORA ATUAL (datetime):")
print("-" * 45)
agora = datetime.now()
print(f"  Data:  {agora.strftime('%d/%m/%Y')}")
print(f"  Hora:  {agora.strftime('%H:%M:%S')}")
print(f"  Dia da semana: {agora.strftime('%A')}")

print("\n✅ Biblioteca Faker utilizada com sucesso!")

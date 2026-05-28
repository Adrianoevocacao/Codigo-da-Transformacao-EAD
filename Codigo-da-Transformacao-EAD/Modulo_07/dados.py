"""Funções de geração de dados do pacote gerador."""

from faker import Faker
from datetime import datetime

fake = Faker("pt_BR")


def gerar_pessoa():
    return {
        "nome": fake.name(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "cidade": f"{fake.city()} - {fake.state_abbr()}"
    }


def gerar_data():
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y às %H:%M:%S")

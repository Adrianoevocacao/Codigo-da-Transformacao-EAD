"""
Atividades 1, 2 e 3 — API OpenWeatherMap
- Consome a API para obter previsão do tempo
- Exibe temperatura, condições climáticas e mais
- Trata erros de conexão e respostas inválidas

Para instalar: pip install requests
Cadastre-se em https://openweathermap.org/api para obter sua API Key gratuita.
"""

import requests

# ⚠️ Substitua pela sua chave de API gratuita do OpenWeatherMap
API_KEY = "SUA_CHAVE_AQUI"
URL_BASE = "https://api.openweathermap.org/data/2.5/weather"


def buscar_clima(cidade):
    """
    Faz a requisição à API do OpenWeatherMap e retorna os dados da cidade.
    Trata erros de conexão, timeout e respostas inválidas.
    """
    params = {
        "q":     cidade,
        "appid": API_KEY,
        "units": "metric",   # Celsius
        "lang":  "pt_br",    # Descrição em português
    }

    try:
        response = requests.get(URL_BASE, params=params, timeout=10)
        response.raise_for_status()  # Lança erro para status 4xx/5xx
        return response.json()

    except requests.exceptions.ConnectionError:
        raise ConnectionError("❌ Erro de conexão: verifique sua internet.")
    except requests.exceptions.Timeout:
        raise TimeoutError("❌ Tempo esgotado: a API demorou para responder.")
    except requests.exceptions.HTTPError as e:
        codigo = e.response.status_code
        if codigo == 401:
            raise ValueError("❌ Chave de API inválida. Verifique sua API Key.")
        elif codigo == 404:
            raise ValueError(f"❌ Cidade '{cidade}' não encontrada.")
        else:
            raise ValueError(f"❌ Erro HTTP {codigo}: {e}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"❌ Erro inesperado na requisição: {e}")


def exibir_clima(dados):
    """Filtra e exibe os dados relevantes da API de forma organizada."""
    cidade      = dados["name"]
    pais        = dados["sys"]["country"]
    temperatura = dados["main"]["temp"]
    sensacao    = dados["main"]["feels_like"]
    temp_min    = dados["main"]["temp_min"]
    temp_max    = dados["main"]["temp_max"]
    umidade     = dados["main"]["humidity"]
    descricao   = dados["weather"][0]["description"].capitalize()
    vento       = dados["wind"]["speed"]
    visib       = dados.get("visibility", 0) // 1000  # metros → km

    print("\n" + "=" * 45)
    print(f"   🌍 CLIMA EM {cidade.upper()}, {pais}")
    print("=" * 45)
    print(f"  🌡️  Temperatura:    {temperatura:.1f}°C")
    print(f"  🤔 Sensação:       {sensacao:.1f}°C")
    print(f"  🔽 Mínima:         {temp_min:.1f}°C")
    print(f"  🔼 Máxima:         {temp_max:.1f}°C")
    print(f"  💧 Umidade:        {umidade}%")
    print(f"  💨 Vento:          {vento} m/s")
    print(f"  👁️  Visibilidade:   {visib} km")
    print(f"  ☁️  Condição:       {descricao}")
    print("=" * 45)


def main():
    print("=" * 45)
    print("   🌤️  PREVISÃO DO TEMPO — OpenWeatherMap")
    print("=" * 45)

    while True:
        cidade = input("\nDigite o nome da cidade (ou 0 para sair): ").strip()
        if cidade == "0":
            print("👋 Encerrando.")
            break
        if not cidade:
            print("⚠️  Digite um nome válido.")
            continue

        try:
            dados = buscar_clima(cidade)
            exibir_clima(dados)
        except (ConnectionError, TimeoutError, ValueError, RuntimeError) as e:
            print(e)


if __name__ == "__main__":
    main()

"""
Desafio Extra — API TMDB: Busca de Filmes
Exibe título, gênero, sinopse, nota e data de lançamento.

Para instalar: pip install requests
Cadastre-se em https://www.themoviedb.org/settings/api para obter sua API Key gratuita.
"""

import requests

# ⚠️ Substitua pela sua chave de API gratuita do TMDB
API_KEY  = "SUA_CHAVE_AQUI"
URL_BASE = "https://api.themoviedb.org/3"

# Busca os gêneros uma vez para traduzir os IDs
def buscar_generos():
    """Retorna um dicionário {id: nome} com todos os gêneros."""
    try:
        url = f"{URL_BASE}/genre/movie/list"
        params = {"api_key": API_KEY, "language": "pt-BR"}
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        generos = r.json().get("genres", [])
        return {g["id"]: g["name"] for g in generos}
    except requests.exceptions.RequestException:
        return {}


def buscar_filmes(titulo):
    """Busca filmes pelo título na API do TMDB."""
    url = f"{URL_BASE}/search/movie"
    params = {
        "api_key":  API_KEY,
        "query":    titulo,
        "language": "pt-BR",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("results", [])

    except requests.exceptions.ConnectionError:
        raise ConnectionError("❌ Erro de conexão: verifique sua internet.")
    except requests.exceptions.Timeout:
        raise TimeoutError("❌ Tempo esgotado: a API demorou para responder.")
    except requests.exceptions.HTTPError as e:
        codigo = e.response.status_code
        if codigo == 401:
            raise ValueError("❌ Chave de API inválida. Verifique sua API Key.")
        else:
            raise ValueError(f"❌ Erro HTTP {codigo}.")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"❌ Erro inesperado: {e}")


def exibir_filmes(filmes, generos_dict):
    """Exibe os dados relevantes de cada filme encontrado."""
    if not filmes:
        print("🎬 Nenhum filme encontrado.")
        return

    # Exibe no máximo os 5 primeiros resultados
    for i, filme in enumerate(filmes[:5], 1):
        titulo       = filme.get("title", "Sem título")
        titulo_orig  = filme.get("original_title", "")
        data         = filme.get("release_date", "Data desconhecida")
        nota         = filme.get("vote_average", 0)
        sinopse      = filme.get("overview", "Sinopse não disponível.")
        ids_generos  = filme.get("genre_ids", [])
        nomes_generos = [generos_dict.get(g, "?") for g in ids_generos] or ["Não informado"]

        print(f"\n{'=' * 50}")
        print(f"  🎬 {i}. {titulo}")
        if titulo_orig and titulo_orig != titulo:
            print(f"     ({titulo_orig})")
        print(f"  📅 Lançamento: {data}")
        print(f"  ⭐ Nota:       {nota:.1f}/10")
        print(f"  🎭 Gêneros:    {', '.join(nomes_generos)}")
        print(f"  📝 Sinopse:")
        # Quebra a sinopse em linhas de até 60 chars
        palavras = sinopse.split()
        linha = "     "
        for palavra in palavras:
            if len(linha) + len(palavra) > 63:
                print(linha)
                linha = "     " + palavra + " "
            else:
                linha += palavra + " "
        if linha.strip():
            print(linha)
    print("=" * 50)


def main():
    print("=" * 50)
    print("   🎬 BUSCADOR DE FILMES — TMDB API")
    print("=" * 50)

    generos = buscar_generos()

    while True:
        titulo = input("\nBuscar filme (ou 0 para sair): ").strip()
        if titulo == "0":
            print("👋 Encerrando.")
            break
        if not titulo:
            print("⚠️  Digite um título válido.")
            continue

        try:
            filmes = buscar_filmes(titulo)
            exibir_filmes(filmes, generos)
        except (ConnectionError, TimeoutError, ValueError, RuntimeError) as e:
            print(e)


if __name__ == "__main__":
    main()

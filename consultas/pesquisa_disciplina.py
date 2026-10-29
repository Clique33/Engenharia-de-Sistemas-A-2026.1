import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def pesquisar_disciplina(termo_busca):
    caminho_json = caminho_raiz / "dados" / "Disciplinas_SistemasComputacao.json"

    if not caminho_json.exists():
        print(f"Erro: Arquivo não encontrado em {caminho_json}")
        return []

    with open(caminho_json, "r", encoding="utf-8") as f:
        disciplinas = json.load(f)

    resultados = []
    termo_busca = termo_busca.lower()

    for disc in disciplinas:
        nome = disc.get("nome", "").lower()
        codigo = disc.get("codigo", "").lower()

        if termo_busca in nome or termo_busca in codigo:
            resultados.append(disc)

    return resultados


if __name__ == "__main__":
    termo = input("Digite o nome ou código da disciplina: ")
    encontradas = pesquisar_disciplina(termo)

    print(f"\n--- Resultados da pesquisa para '{termo}' ---")
    if encontradas:
        for disc in encontradas:
            print(f"[{disc.get('codigo')}] {disc.get('nome')} | CH: {disc.get('ch')}h | Semestre: {disc.get('semestre')}")
    else:
        print("Nenhuma disciplina encontrada.")
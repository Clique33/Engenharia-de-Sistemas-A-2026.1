import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def carregar_grafo_pre_requisitos():
    caminho_json = caminho_raiz / "dados" / "Disciplinas_SistemasComputacao.json"
    if not caminho_json.exists():
        raise FileNotFoundError(f"Arquivo de disciplinas não encontrado em: {caminho_json}")

    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    grafo = {}
    for disc in data:
        nome = disc.get("nome")
        reqs = disc.get("pre_requisitos", [])
        grafo[nome] = reqs

    return grafo


if __name__ == "__main__":
    grafo = carregar_grafo_pre_requisitos()
    print("--- Visualização de Pré-Requisitos ---")
    for disc, reqs in grafo.items():
        if reqs:
            print(f"{disc} <-- {', '.join(reqs)}")
        else:
            print(f"{disc} (Sem pré-requisitos)")
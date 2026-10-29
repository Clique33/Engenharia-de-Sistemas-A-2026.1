import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def obter_status_disciplinas_fluxograma(matricula):
    caminho_historico = caminho_raiz / "dados" / "historico_alunos.json"

    if not caminho_historico.exists():
        print(f"Erro: Arquivo não encontrado em {caminho_historico}")
        return {}

    with open(caminho_historico, "r", encoding="utf-8") as f:
        historico = json.load(f)

    aluno = historico.get(matricula)
    if not aluno:
        return {}

    status_mapa = {}
    for disc in aluno.get("disciplinas", []):
        nome = disc.get("nome")
        status = disc.get("status", "pendente")
        status_mapa[nome] = status

    return status_mapa


if __name__ == "__main__":
    mat = "matricula_201020668899"
    status = obter_status_disciplinas_fluxograma(mat)
    print(f"--- Status das Disciplinas do Aluno ({mat}) ---")
    for disc, st in status.items():
        print(f"{disc}: {st}")
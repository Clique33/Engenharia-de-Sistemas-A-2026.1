import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def adicionar_disciplina_curriculo(nova_disciplina, caminho_curriculo=None):
    if caminho_curriculo is None:
        caminho_curriculo = caminho_raiz / "dados" / "curriculo.json"
    else:
        caminho_curriculo = Path(caminho_curriculo)

    curriculo = []
    if caminho_curriculo.exists():
        with open(caminho_curriculo, "r", encoding="utf-8") as f:
            curriculo = json.load(f)

    curriculo.append(nova_disciplina)

    with open(caminho_curriculo, "w", encoding="utf-8") as f:
        json.dump(curriculo, f, ensure_ascii=False, indent=2)

    return True


if __name__ == "__main__":
    nova = {
        "nome": "Tópicos Especiais em Sistemas",
        "codigo": "ES001",
        "ch": 60,
        "semestre": 8,
        "pre_requisitos": []
    }
    adicionar_disciplina_curriculo(nova)
    print("Disciplina adicionada ao currículo com sucesso.")
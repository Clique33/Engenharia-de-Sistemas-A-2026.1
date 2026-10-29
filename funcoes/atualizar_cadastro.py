import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def atualizar_dados_aluno(matricula, novos_dados, caminho_cadastro=None):
    if caminho_cadastro is None:
        caminho_cadastro = caminho_raiz / "dados" / "cadastro_alunos.json"
    else:
        caminho_cadastro = Path(caminho_cadastro)

    if not caminho_cadastro.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_cadastro}")

    with open(caminho_cadastro, "r", encoding="utf-8") as f:
        cadastros = json.load(f)

    if matricula in cadastros:
        cadastros[matricula].update(novos_dados)
        with open(caminho_cadastro, "w", encoding="utf-8") as f:
            json.dump(cadastros, f, ensure_ascii=False, indent=2)
        return True, "Cadastro atualizado com sucesso!"

    return False, "Matrícula não encontrada."


if __name__ == "__main__":
    sucesso, msg = atualizar_dados_aluno("matricula_201020668899", {"email": "novoemail@ufrj.br"})
    print(msg)
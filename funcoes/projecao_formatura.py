import json
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))

from consultas.calcula_disciplinas_disponiveis import disciplinas_disponiveis


class ProjecaoFormatura:
    def __init__(self, matricula, caminho_historico=None, caminho_curriculo=None):
        self.caminho_historico = caminho_historico or (caminho_raiz / "dados" / "historico_alunos.json")
        self.caminho_curriculo = caminho_curriculo or (caminho_raiz / "dados" / "curriculo.json")
        self.matricula = matricula

    def calcular_semestres_restantes(self, limite_disciplinas_por_semestre=5):
        if not Path(self.caminho_historico).exists() or not Path(self.caminho_curriculo).exists():
            print("Arquivos de dados não encontrados.")
            return 0, []

        with open(self.caminho_historico, "r", encoding="utf-8") as f:
            historico = json.load(f)

        with open(self.caminho_curriculo, "r", encoding="utf-8") as f:
            curriculo = json.load(f)

        aluno = historico.get(self.matricula)
        if not aluno:
            return 0, []

        concluidas = {d["nome"] for d in aluno.get("disciplinas", []) if d.get("status") == "concluida"}
        todas_disciplinas = {d["nome"]: d.get("pre_requisitos", []) for d in curriculo}

        semestres = 0
        plano_estudo = []

        while len(concluidas) < len(todas_disciplinas):
            disponiveis = disciplinas_disponiveis(todas_disciplinas, concluidas)
            if not disponiveis:
                break

            a_cursar = disponiveis[:limite_disciplinas_por_semestre]
            concluidas.update(a_cursar)
            semestres += 1
            plano_estudo.append((f"Semestre {semestres}", a_cursar))

        return semestres, plano_estudo


if __name__ == "__main__":
    projecao = ProjecaoFormatura("matricula_201020668899")
    qtd, plano = projecao.calcular_semestres_restantes()
    print(f"Previsão de semestres restantes: {qtd}")
    for sem, disciplinas in plano:
        print(f"{sem}: {', '.join(disciplinas)}")
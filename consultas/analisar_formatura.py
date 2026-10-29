import json
import os
import sys
from pathlib import Path

# Configuração do caminho da raiz do projeto
caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))


def carregar_dados():
    caminho_json = caminho_raiz / "dados" / "historico_alunos.json"
    if not caminho_json.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_json}")

    with open(caminho_json, "r", encoding="utf-8") as f:
        return json.load(f)


def analisar_formatura(matricula, ch_obrigatoria_total=2000, ch_optativa_total=300):
    dados = carregar_dados()

    aluno = dados.get(matricula)
    if not aluno:
        print(f"Aluno com matrícula {matricula} não encontrado.")
        return

    ch_obrigatoria_integralizada = 0
    ch_optativa_integralizada = 0

    for disc in aluno.get("disciplinas", []):
        if disc.get("status") == "concluida":
            ch = disc.get("ch", 0)
            tipo = disc.get("tipo")
            if tipo == "OB":
                ch_obrigatoria_integralizada += ch
            elif tipo == "OP":
                ch_optativa_integralizada += ch

    pct_ob = (ch_obrigatoria_integralizada / ch_obrigatoria_total) * 100
    pct_op = (ch_optativa_integralizada / ch_optativa_total) * 100

    print(f"--- Análise de Formatura: {aluno.get('nome')} ---")
    print(f"Carga Horária Obrigatória: {ch_obrigatoria_integralizada}/{ch_obrigatoria_total} h ({min(pct_ob, 100):.1f}%)")
    print(f"Carga Horária Optativa: {ch_optativa_integralizada}/{ch_optativa_total} h ({min(pct_op, 100):.1f}%)")

    if pct_ob >= 100 and pct_op >= 100:
        print("Status: O aluno cumpre os requisitos para formatura!")
    else:
        print("Status: Faltam disciplinas para a integralização do curso.")


if __name__ == "__main__":
    analisar_formatura("matricula_201020668899")
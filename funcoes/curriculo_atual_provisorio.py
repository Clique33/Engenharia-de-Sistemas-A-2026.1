import json
from pathlib import Path
from typing import Dict, Optional

# Importando a classe Disciplina do seu arquivo disciplina.py
from disciplina import Disciplina

class Curriculo:

    def __init__(self):
        self.disciplinas: Dict[str, Disciplina] = {}

    def adicionar_disciplina(self, disciplina: Disciplina) -> None:
        self.disciplinas[disciplina.codigo] = disciplina

    def obter_disciplina(self, codigo: str) -> Optional[Disciplina]:
        return self.disciplinas.get(codigo)

    @classmethod
    def carregar_de_arquivo(cls, caminho_arquivo: str | Path) -> "Curriculo":
        caminho = Path(caminho_arquivo)
        if not caminho.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {caminho_arquivo}"
            )

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        curriculo = cls()
        for item in dados:
            # A nova classe Disciplina exige os parâmetros abaixo nesta ordem ou nomeados:
            disciplina = Disciplina(
                codigo=item["codigo"],
                nome=item["nome"],
                carga_horaria=item["carga_horaria"],
                periodo_recomendado=item["periodo"], # Adaptado de "periodo" para "periodo_recomendado"
                pre_requisitos=item.get("pre_requisitos", []),
            )
            curriculo.adicionar_disciplina(disciplina)

        return curriculo
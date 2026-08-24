from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Disciplina:
    codigo: str
    nome: str
    periodo: int
    creditos: int
    carga_horaria: int
    pre_requisitos: List[str] = field(default_factory=list)


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
            disciplina = Disciplina(
                codigo=item["codigo"],
                nome=item["nome"],
                periodo=item["periodo"],
                creditos=item["creditos"],
                carga_horaria=item["carga_horaria"],
                pre_requisitos=item.get("pre_requisitos", []),
            )
            curriculo.adicionar_disciplina(disciplina)

        return curriculo
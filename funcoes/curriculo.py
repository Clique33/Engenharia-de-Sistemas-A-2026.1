import json
from pathlib import Path
from typing import Dict, Optional
from funcoes.disciplina import Disciplina

class Curriculo:
    def __init__(self, curso="Engenharia de Computação"):
        self.curso = curso
        self.disciplinas: Dict[str, Disciplina] = {}

    def adicionar_disciplina(self, disciplina: Disciplina):
        if disciplina.codigo in self.disciplinas:
            print("A disciplina já existe")
            return -1
        self.disciplinas[disciplina.codigo] = disciplina

    def obter_disciplina(self, codigo: str) -> Optional[Disciplina]:
        return self.disciplinas.get(codigo)

    def buscar_disciplina(self, codigo: str):
        # Mantido para compatibilidade com trechos mais antigos
        disciplina = self.disciplinas.get(codigo)
        return disciplina if disciplina else -1

    def disciplinas_por_periodo(self, periodo: int):
        print(f"Disciplinas do {periodo}º período:")
        for disciplina in self.disciplinas.values():
            if periodo == getattr(disciplina, 'periodo_recomendado', None):
                print(f"Código: {disciplina.codigo} | Nome: {disciplina.nome}")

    def mostrar_disciplinas(self):
        if not self.disciplinas:
            print("Curso sem disciplinas\n")
            return -1
        
        print(f"\nImprimindo disciplinas do curso de {self.curso}:")
        for disciplina in self.disciplinas.values():
            periodo = getattr(disciplina, 'periodo_recomendado', 'N/A')
            print(f"Código: {disciplina.codigo} | Nome: {disciplina.nome} | Período: {periodo}")

    @classmethod
    def carregar_de_arquivo(cls, caminho_arquivo: str = None, curso="Engenharia de Computação") -> "Curriculo":
        if caminho_arquivo is None:
            caminho_base = Path(__file__).resolve().parent.parent
            caminho = caminho_base / "dados" / "curriculo.json"
        else:
            caminho = Path(caminho_arquivo)

        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        curriculo = cls(curso)
        for item in dados:
            disciplina = Disciplina(
                codigo=item["codigo"],
                nome=item["nome"],
                carga_horaria=item["carga_horaria"],
                pre_requisitos=item.get("pre_requisitos", []),
            )
            setattr(disciplina, 'periodo_recomendado', item.get("periodo"))
            curriculo.adicionar_disciplina(disciplina)

        return curriculo
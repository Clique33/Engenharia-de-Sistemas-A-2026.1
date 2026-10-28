import json
from pathlib import Path
from typing import Dict, Optional
from disciplina import Disciplina

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
            if periodo == disciplina.periodo_recomendado:
                print(f"Código: {disciplina.codigo} | Nome: {disciplina.nome}")

    def mostrar_disciplinas(self):
        if not self.disciplinas:
            print("Curso sem disciplinas\n")
            return -1
        
        print(f"\nImprimindo disciplinas do curso de {self.curso}:")
        for disciplina in self.disciplinas.values():
            print(f"Código: {disciplina.codigo} | Nome: {disciplina.nome} | Período: {disciplina.periodo_recomendado}")

    @classmethod
    def carregar_de_arquivo(cls, caminho_arquivo: str, curso="Engenharia de Computação") -> "Curriculo":
        caminho = Path(caminho_arquivo)
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        curriculo = cls(curso)
        for item in dados:
            disciplina = Disciplina(
                codigo=item["codigo"],
                nome=item["nome"],
                carga_horaria=item["carga_horaria"],
                periodo_recomendado=item["periodo"],
                pre_requisitos=item.get("pre_requisitos", []),
            )
            curriculo.adicionar_disciplina(disciplina)

        return curriculo
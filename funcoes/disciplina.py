import json
import os

class Disciplina:
    def __init__(self, codigo, nome, carga_horaria, equivalente=None, pre_requisitos=None, cor=None, status="pendente"):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.equivalente = equivalente if equivalente else []
        self.pre_requisitos = pre_requisitos if pre_requisitos else []
        self.cor = cor
        self.status = status

    @classmethod
    def carregar_disciplinas(cls, caminho_json=None):
        if caminho_json is None:
            caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            caminho_json = os.path.join(caminho_base, "dados", "Disciplinas_SistemasComputacao.json")

        with open(caminho_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        disciplinas = []
        for item in dados:
            disc = cls(
                codigo=item['codigo'],
                nome=item['nome'],
                carga_horaria=item['carga_horaria'],
                equivalente=item.get('equivalente'),
                pre_requisitos=item.get('pre_requisitos'),
                cor=item.get('cor'),
                status=item.get('status', 'pendente')
            )
            disciplinas.append(disc)
        return disciplinas

    def __repr__(self):
        return f"<Disciplina {self.codigo} - {self.nome}>"
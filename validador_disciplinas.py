from curriculo import Curriculo

class ValidadorDisciplinas:
    def __init__(self, curriculo: Curriculo):
        self.curriculo = curriculo
        self.historico_aluno = set()

    def carregar_historico(self, codigos_cursados: list):
        self.historico_aluno = set(codigos_cursados)

    def _obter_pre_requisitos_limpos(self, codigo_disciplina: str) -> list:
        disciplina = self.curriculo.obter_disciplina(codigo_disciplina)
        if not disciplina:
            return []

        reqs_limpos = []
        for pre in disciplina.pre_requisitos:
            if "," in pre:
                reqs_limpos.extend(p.strip() for p in pre.split(","))
            else:
                reqs_limpos.append(pre.strip())
        return reqs_limpos

    def verificar_permissao(self, codigo_disciplina: str) -> bool:
        if codigo_disciplina in self.historico_aluno:
            return False

        if not self.curriculo.obter_disciplina(codigo_disciplina):
            return False

        pre_reqs = self._obter_pre_requisitos_limpos(codigo_disciplina)
        return all(req in self.historico_aluno for req in pre_reqs)

    def disciplinas_disponiveis(self) -> list:
        disponiveis = []
        for codigo in self.curriculo.disciplinas:
            if self.verificar_permissao(codigo):
                disponiveis.append(codigo)
        return disponiveis
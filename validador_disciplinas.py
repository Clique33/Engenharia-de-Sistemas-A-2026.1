class ValidadorDisciplinas:
    def __init__(self):
        # Dicionário de pré-requisitos (Código da Disciplina -> Lista de Códigos Exigidos)
        self._pre_requisitos = {
            "ENG456": ["ELE123"],
            "PROG02": ["PROG01", "MAT101"],
            "FIS002": ["FIS001", "MAT101"]
        }
        self._historico_aluno = []

    def carregar_historico(self, disciplinas_cursadas):
        self._historico_aluno = disciplinas_cursadas

    def consultar_pre_requisitos(self, codigo_disciplina):
        # Retorna a lista de pré-requisitos. Se não existir, retorna lista vazia.
        return self._pre_requisitos.get(codigo_disciplina, [])

    def verificar_permissao(self, codigo_disciplina):
        pre_reqs = self.consultar_pre_requisitos(codigo_disciplina)
        
        # Validação: Se não há pré-requisitos, permissão concedida
        if not pre_reqs:
            return True
        
        # Validação: Verifica se todos os itens exigidos estão no histórico do aluno
        for requisito in pre_reqs:
            if requisito not in self._historico_aluno:
                return False
                
        return True
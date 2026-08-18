class Disciplina:
    def __init__(self, codigo: str, nome: str, carga_horaria: int, periodo_recomendado: int, pre_requisitos: list = None):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.periodo_recomendado = periodo_recomendado
        self.pre_requisitos = pre_requisitos 
        if pre_requisitos is None:
            self.pre_requisitos = []

    def obter_informações(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "carga_horaria": self.carga_horaria,
            "periodo": self.periodo_recomendado,
            "pre_requisitos": self.pre_requisitos,
            }

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.carga_horaria}h)"

    def adicionar_pre_requisito(self, disciplina_codigo: str):
        """Adiciona o código de uma disciplina pré-requisito."""
        if disciplina_codigo not in self.pre_requisitos:
            self.pre_requisitos.append(disciplina_codigo)

    def tem_pre_requisitos(self) -> bool:
        """Verifica se a disciplina possui pré-requisitos."""
        return len(self.pre_requisitos) > 0

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.carga_horaria}h)"
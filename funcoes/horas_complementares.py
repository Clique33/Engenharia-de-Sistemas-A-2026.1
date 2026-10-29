from enum import Enum


class TipoAtividade(Enum):
    """Tipos de atividades que integram a carga de horas complementares."""
    CARGA_EXTENSAO = "Carga de Extensão"
    ATIVIDADE_COMPLEMENTAR = "Atividade Complementar"
    ATIVIDADE_CURRICULAR_EXTENSAO = "Atividade Curricular de Extensão"


class AtividadeComplementar:
    """Representa uma atividade complementar registrada."""

    def __init__(self, nome: str, horas: int, tipo: TipoAtividade):
        self.nome = nome
        self.horas = horas
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo.value}: {self.nome} ({self.horas}h)"


class HorasComplementares:
    def __init__(self, meta_horas):
        self.meta_horas = meta_horas
        self.atividades = []

    def registrar_atividade(self, nome_atividade, horas, tipo=TipoAtividade.ATIVIDADE_COMPLEMENTAR):
        if horas <= 0:
            return False
        self.atividades.append({"atividade": nome_atividade, "horas": horas, "tipo": tipo})
        return True

    def registrar_carga_extensao(self, nome_atividade, horas):
        """Cadastra uma Carga de Extensão."""
        return self.registrar_atividade(
            nome_atividade, horas, TipoAtividade.CARGA_EXTENSAO
        )

    def registrar_atividade_complementar(self, nome_atividade, horas):
        """Cadastra uma Atividade Complementar."""
        return self.registrar_atividade(
            nome_atividade, horas, TipoAtividade.ATIVIDADE_COMPLEMENTAR
        )

    def registrar_atividade_curricular_extensao(self, nome_atividade, horas):
        """Cadastra uma Atividade Curricular de Extensão."""
        return self.registrar_atividade(
            nome_atividade, horas, TipoAtividade.ATIVIDADE_CURRICULAR_EXTENSAO
        )

    def calcular_total(self, tipo=None):
        if tipo is None:
            return sum(item["horas"] for item in self.atividades)
        return sum(
            item["horas"] for item in self.atividades if item["tipo"] == tipo
        )

    def meta_atingida(self):
        return self.calcular_total() >= self.meta_horas

    def horas_faltantes(self):
        faltam = self.meta_horas - self.calcular_total()
        return faltam if faltam > 0 else 0

    def obter_atividades_por_tipo(self, tipo: TipoAtividade):
        """Retorna apenas as atividades de um tipo específico."""
        return [item for item in self.atividades if item["tipo"] == tipo]

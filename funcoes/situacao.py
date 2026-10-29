from enum import Enum


class Situacao(Enum):
    """Situação de uma disciplina do currículo para um aluno."""

    APROVADA = "aprovada"
    REPROVADA = "reprovada"
    CURSANDO = "cursando"
    NAO_CONCLUIDA = "nao_concluida"
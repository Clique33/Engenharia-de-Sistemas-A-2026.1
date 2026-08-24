import unicodedata

from src.situacao import Situacao

# Precedência: quanto maior, mais forte. Aprovação prevalece sobre
# qualquer registro anterior da mesma disciplina.
_PRECEDENCIA = {
    Situacao.APROVADA: 3,
    Situacao.CURSANDO: 2,
    Situacao.REPROVADA: 1,
}

_SINONIMOS = {
    "aprovado": Situacao.APROVADA,
    "aprovada": Situacao.APROVADA,
    "ap": Situacao.APROVADA,
    "reprovado": Situacao.REPROVADA,
    "reprovada": Situacao.REPROVADA,
    "rep": Situacao.REPROVADA,
    "reprovado por falta": Situacao.REPROVADA,
    "cursando": Situacao.CURSANDO,
    "em andamento": Situacao.CURSANDO,
    "matriculado": Situacao.CURSANDO,
}


def _normalizar(texto):
    """Remove acentos, espaços extras e caixa alta."""
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = sem_acento.encode("ASCII", "ignore").decode("ASCII")
    return sem_acento.strip().lower()


def interpretar_situacao(texto):
    """Converte o texto do histórico em um Situacao.

    Levanta ValueError se o texto não for reconhecido, para que um
    histórico com formato inesperado falhe de forma visível em vez de
    classificar errado em silêncio.
    """
    chave = _normalizar(texto)
    if chave not in _SINONIMOS:
        raise ValueError(f"Situação não reconhecida no histórico: {texto!r}")
    return _SINONIMOS[chave]


def classificar_disciplinas(historico, codigos_curriculo):
    """Classifica cada disciplina do currículo na situação do aluno.

    Args:
        historico: iterável de dicts com as chaves 'codigo' e 'situacao'.
            Pode conter mais de um registro para a mesma disciplina.
        codigos_curriculo: iterável com os códigos de todas as
            disciplinas do currículo.

    Returns:
        dict que mapeia código da disciplina para Situacao. Disciplinas
        do currículo ausentes no histórico recebem NAO_CONCLUIDA.

    Observação: quando há mais de um registro da mesma disciplina,
    prevalece a situação de maior precedência (aprovada > cursando >
    reprovada).
    """
    resultado = {codigo: Situacao.NAO_CONCLUIDA for codigo in codigos_curriculo}

    for registro in historico:
        codigo = registro["codigo"]
        if codigo not in resultado:
            continue  # disciplina fora do currículo (ex.: eletiva livre)

        nova = interpretar_situacao(registro["situacao"])
        atual = resultado[codigo]

        if _PRECEDENCIA.get(nova, 0) > _PRECEDENCIA.get(atual, 0):
            resultado[codigo] = nova

    return resultado


def filtrar_por_situacao(classificacao, situacao):
    """Retorna a lista ordenada de códigos em uma dada situação."""
    return sorted(c for c, s in classificacao.items() if s == situacao)
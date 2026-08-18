import pytest  # type: ignore

from classificador import (
    classificar_disciplinas,
    filtrar_por_situacao,
    interpretar_situacao,
)
from situacao import Situacao

CURRICULO = ["MAT001", "MAT002", "FIS001", "COMP001"]


def test_identifica_disciplina_aprovada():
    historico = [{"codigo": "MAT001", "situacao": "Aprovado"}]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert resultado["MAT001"] == Situacao.APROVADA


def test_identifica_disciplina_reprovada():
    historico = [{"codigo": "MAT002", "situacao": "Reprovado"}]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert resultado["MAT002"] == Situacao.REPROVADA


def test_identifica_disciplina_em_andamento():
    historico = [{"codigo": "FIS001", "situacao": "Cursando"}]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert resultado["FIS001"] == Situacao.CURSANDO


def test_disciplina_ausente_no_historico_nao_e_concluida():
    resultado = classificar_disciplinas([], CURRICULO)
    assert resultado["COMP001"] == Situacao.NAO_CONCLUIDA


def test_reprovacao_seguida_de_aprovacao_prevalece_aprovada():
    historico = [
        {"codigo": "MAT001", "situacao": "Reprovado"},
        {"codigo": "MAT001", "situacao": "Aprovado"},
    ]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert resultado["MAT001"] == Situacao.APROVADA


def test_ordem_dos_registros_nao_altera_o_resultado():
    historico = [
        {"codigo": "MAT001", "situacao": "Aprovado"},
        {"codigo": "MAT001", "situacao": "Reprovado"},
    ]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert resultado["MAT001"] == Situacao.APROVADA


def test_disciplina_fora_do_curriculo_e_ignorada():
    historico = [{"codigo": "LIVRE999", "situacao": "Aprovado"}]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert "LIVRE999" not in resultado


def test_situacao_desconhecida_levanta_erro():
    historico = [{"codigo": "MAT001", "situacao": "Trancado"}]
    with pytest.raises(ValueError):
        classificar_disciplinas(historico, CURRICULO)


def test_variacoes_de_texto_sao_interpretadas():
    assert interpretar_situacao("APROVADO") == Situacao.APROVADA
    assert interpretar_situacao(" em andamento ") == Situacao.CURSANDO


def test_consulta_por_situacao():
    historico = [
        {"codigo": "MAT001", "situacao": "Aprovado"},
        {"codigo": "MAT002", "situacao": "Aprovado"},
        {"codigo": "FIS001", "situacao": "Cursando"},
    ]
    resultado = classificar_disciplinas(historico, CURRICULO)
    assert filtrar_por_situacao(resultado, Situacao.APROVADA) == ["MAT001", "MAT002"]
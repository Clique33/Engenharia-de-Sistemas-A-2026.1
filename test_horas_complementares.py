from horas_complementares import (
    HorasComplementares,
    TipoAtividade,
)

if __name__ == '__main__':
    print("Iniciando testes...")

    # ------------------------------------------------------------------
    # Critério 1: Total de horas (compatibilidade com a API original)
    # ------------------------------------------------------------------
    sistema = HorasComplementares(meta_horas=100)

    sistema.registrar_atividade("Curso de Python", 40)
    sistema.registrar_atividade("Semana de Engenharia", 15)

    total = sistema.calcular_total()
    if total != 55:
        print(f"ERRO CRÍTÉRIO 1: Esperava 55, mas o sistema retornou {total}")
        exit()

    # ------------------------------------------------------------------
    # Critério 2: Listar atividades registradas
    # ------------------------------------------------------------------
    atividades = sistema.atividades
    if len(atividades) != 2 or atividades[0]["atividade"] != "Curso de Python":
        print("ERRO CRÍTÉRIO 2: Falha ao listar as atividades registradas.")
        exit()

    # ------------------------------------------------------------------
    # Critério 3: Cadastrar Carga de Extensão
    # ------------------------------------------------------------------
    carga = HorasComplementares(meta_horas=200)
    ok = carga.registrar_carga_extensao("Estágio Supervisionado", 120)
    if not ok:
        print("ERRO CRÍTÉRIO 3: Falha ao cadastrar Carga de Extensão.")
        exit()

    tipo_carga = carga.atividades[0]["tipo"]
    if tipo_carga != TipoAtividade.CARGA_EXTENSAO:
        print(f"ERRO CRÍTÉRIO 3: Tipo esperado Carga de Extensão, recebido {tipo_carga}")
        exit()

    if carga.calcular_total(TipoAtividade.CARGA_EXTENSAO) != 120:
        print("ERRO CRÍTÉRIO 3: Total de Carga de Extensão incorreto.")
        exit()

    # ------------------------------------------------------------------
    # Critério 4: Cadastrar Atividade Curricular de Extensão
    # ------------------------------------------------------------------
    atv_curricular = HorasComplementares(meta_horas=50)
    ok = atv_curricular.registrar_atividade_curricular_extensao(
        "Projeto de Extensão I", 30
    )
    if not ok:
        print("ERRO CRÍTÉRIO 4: Falha ao cadastrar Atividade Curricular de Extensão.")
        exit()

    esperado_ce = TipoAtividade.ATIVIDADE_CURRICULAR_EXTENSAO
    if atv_curricular.atividades[0]["tipo"] != esperado_ce:
        print("ERRO CRÍTÉRIO 4: Tipo de Atividade Curricular de Extensão incorreto.")
        exit()

    # ------------------------------------------------------------------
    # Critério 5: Cadastrar Atividade Complementar
    # ------------------------------------------------------------------
    atv_complementar = HorasComplementares(meta_horas=100)
    ok = atv_complementar.registrar_atividade_complementar("Palestra de TI", 8)
    if not ok:
        print("ERRO CRÍTÉRIO 5: Falha ao cadastrar Atividade Complementar.")
        exit()

    if atv_complementar.atividades[0]["tipo"] != TipoAtividade.ATIVIDADE_COMPLEMENTAR:
        print("ERRO CRÍTÉRIO 5: Tipo de Atividade Complementar incorreto.")
        exit()

    # ------------------------------------------------------------------
    # Critério 6: Soma por tipo e filtragem
    # ------------------------------------------------------------------
    completo = HorasComplementares(meta_horas=100)
    completo.registrar_carga_extensao("Estágio 1", 40)
    completo.registrar_atividade_complementar("Palestra", 10)
    completo.registrar_atividade_curricular_extensao("Projeto Extensão", 15)
    completo.registrar_carga_extensao("Estágio 2", 20)

    if completo.calcular_total() != 85:
        print(f"ERRO CRÍTÉRIO 6: Total geral esperado 85, recebido {completo.calcular_total()}")
        exit()
    if completo.calcular_total(TipoAtividade.CARGA_EXTENSAO) != 60:
        print("ERRO CRÍTÉRIO 6: Total de Carga de Extensão esperado 60.")
        exit()
    if completo.calcular_total(TipoAtividade.ATIVIDADE_COMPLEMENTAR) != 10:
        print("ERRO CRÍTÉRIO 6: Total de Atividade Complementar esperado 10.")
        exit()
    if completo.calcular_total(TipoAtividade.ATIVIDADE_CURRICULAR_EXTENSAO) != 15:
        print("ERRO CRÍTÉRIO 6: Total de Atividade Curricular esperado 15.")
        exit()

    atividades_ce = completo.obter_atividades_por_tipo(TipoAtividade.CARGA_EXTENSAO)
    if len(atividades_ce) != 2:
        print("ERRO CRÍTÉRIO 6: Esperava 2 atividades de Carga de Extensão.")
        exit()

    # ------------------------------------------------------------------
    # Critério 7: Horas inválidas são rejeitadas
    # ------------------------------------------------------------------
    if sistema.registrar_atividade("Atividade Inválida", 0):
        print("ERRO CRÍTÉRIO 7: Atividade com 0 horas deveria ser rejeitada.")
        exit()
    if sistema.registrar_atividade("Atividade Negativa", -5):
        print("ERRO CRÍTÉRIO 7: Atividade com horas negativas deveria ser rejeitada.")
        exit()

    # ------------------------------------------------------------------
    # Critério 8: Meta atingida
    # ------------------------------------------------------------------
    meta_ok = HorasComplementares(meta_horas=10)
    meta_ok.registrar_atividade_complementar("Curso", 15)
    if not meta_ok.meta_atingida():
        print("ERRO CRÍTÉRIO 8: Meta deveria estar atingida com 15h >= 10h.")
        exit()
    if meta_ok.horas_faltantes() != 0:
        print("ERRO CRÍTÉRIO 8: horas_faltantes deveria ser 0 quando meta atingida.")
        exit()

    print("Sucesso! Os critérios de aceitação foram validados com êxito.")

# simula_migracao.py
COR_VERDE = "\033[92m"
COR_PADRAO = "\033[0m"

def verificar_migracao(historico_aluno, novo_curriculo, sistema_equivalencias):
    resultado_novo_curriculo = {}
    novas_concluidas_por_equivalencia = []

    # Extrai disciplinas concluídas pelo aluno {codigo_antigo: nome_antigo}
    concluidas = {d["codigo"]: d["nome"] for d in historico_aluno if d.get("status") == "concluida"}

    # Mapeia quais novos códigos o aluno tem direito por equivalência
    equiv_garantidas = {}
    for cod_antigo in concluidas:
        cod_novo = sistema_equivalencias.consultar(cod_antigo)
        if cod_novo:
            equiv_garantidas[cod_novo] = cod_antigo

    # Cruza os dados com a grade nova
    for cod_novo, dados in novo_curriculo.items():
        nome_novo = dados["nome"]

        if cod_novo in concluidas:
            resultado_novo_curriculo[nome_novo] = {"status": "Concluída", "cor": COR_VERDE}
        elif cod_novo in equiv_garantidas:
            cod_antigo = equiv_garantidas[cod_novo]
            resultado_novo_curriculo[nome_novo] = {
                "status": f"Concluída (Equivalência de: {concluidas[cod_antigo]})",
                "cor": COR_VERDE
            }
            novas_concluidas_por_equivalencia.append(nome_novo)
        else:
            resultado_novo_curriculo[nome_novo] = {"status": "Pendente", "cor": COR_PADRAO}

    return resultado_novo_curriculo, novas_concluidas_por_equivalencia

def exibir_resultado(resultado, novas_equivalencias):
    print("\n--- SITUAÇÃO NO NOVO CURRÍCULO ---")
    for disc, dados in resultado.items():
        print(f"{dados['cor']}{disc}: {dados['status']}{COR_PADRAO}")
        
    print("\n--- RESUMO DE NOVAS DISCIPLINAS CONCLUÍDAS POR EQUIVALÊNCIA ---")
    if novas_equivalencias:
        for disc in novas_equivalencias:
            print(f"{COR_VERDE}- {disc}{COR_PADRAO}")
    else:
        print("Nenhuma nova disciplina foi concluída por equivalência.")
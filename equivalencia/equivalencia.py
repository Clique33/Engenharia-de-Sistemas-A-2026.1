import os

COR_VERDE = "\033[92m"
COR_PADRAO = "\033[0m"

def verificar_migracao(historico, curriculo_atual, novo_curriculo, tabela_equivalencias):
    """Compara os currículos e o histórico para determinar o status no novo currículo.

    Parâmetros:
        historico (dict): Disciplinas cursadas e seus respectivos status.
        curriculo_atual (list): Lista de disciplinas da grade antiga.
        novo_curriculo (list): Lista de disciplinas da nova grade.
        tabela_equivalencias (dict): Mapeamento de disciplinas novas para antigas.

    Retorno:
        tuple: (resultado_novo_curriculo, novas_concluidas_por_equivalencia)
    """
    resultado_novo_curriculo = {}
    novas_concluidas_por_equivalencia = []
    
    concluidas_atual = {disc for disc, status in historico.items() if status == "Concluída"}

    for disciplina in novo_curriculo:
        if disciplina in curriculo_atual and disciplina in concluidas_atual:
            resultado_novo_curriculo[disciplina] = {"status": "Concluída", "cor": COR_VERDE}
            
        elif disciplina in tabela_equivalencias:
            equivalente = tabela_equivalencias[disciplina]
            if equivalente in concluidas_atual:
                resultado_novo_curriculo[disciplina] = {"status": "Concluída (Equivalência)", "cor": COR_VERDE}
                novas_concluidas_por_equivalencia.append(disciplina)
            else:
                resultado_novo_curriculo[disciplina] = {"status": "Pendente", "cor": COR_PADRAO}
                
        else:
            resultado_novo_curriculo[disciplina] = {"status": "Pendente", "cor": COR_PADRAO}
            
    return resultado_novo_curriculo, novas_concluidas_por_equivalencia

def exibir_resultado(resultado, novas_equivalencias):
    """Exibe o resultado formatado de forma independente de GUI no terminal."""
    print("\n--- SITUAÇÃO NO NOVO CURRÍCULO ---")
    for disc, dados in resultado.items():
        print(f"{dados['cor']}{disc}: {dados['status']}{COR_PADRAO}")
        
    print("\n--- RESUMO DE NOVAS DISCIPLINAS CONCLUÍDAS POR EQUIVALÊNCIA ---")
    if novas_equivalencias:
        for disc in novas_equivalencias:
            print(f"{COR_VERDE}- {disc}{COR_PADRAO}")
    else:
        print("Nenhuma nova disciplina foi concluída por equivalência.")


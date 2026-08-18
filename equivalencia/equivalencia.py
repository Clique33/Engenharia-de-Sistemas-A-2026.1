import os

# Códigos de cor para o terminal (ANSI)
COR_VERDE = "\033[92m"
COR_PADRAO = "\033[0m"

def verificar_migracao(historico, curriculo_atual, novo_curriculo, tabela_equivalencias):
    """
    Compara os currículos e o histórico para determinar o status no novo currículo.
    Retorna um dicionário com o status de cada disciplina e a lista de novas aproveitadas.
    """
    resultado_novo_curriculo = {}
    novas_concluidas_por_equivalencia = []
    
    # Conjunto de disciplinas concluídas no currículo atual
    concluidas_atual = {disc for disc, status in historico.items() if status == "Concluída"}

    for disciplina in novo_curriculo:
        # Critério 3: Disciplina pertence aos dois currículos e já foi concluída no atual
        if disciplina in curriculo_atual and disciplina in concluidas_atual:
            resultado_novo_curriculo[disciplina] = {"status": "Concluída", "cor": COR_VERDE}
            
        # Critério 2: Disciplina tem equivalência que foi concluída no atual
        elif disciplina in tabela_equivalencias:
            equivalente = tabela_equivalencias[disciplina]
            if equivalente in concluidas_atual:
                resultado_novo_curriculo[disciplina] = {"status": "Concluída (Equivalência)", "cor": COR_VERDE}
                novas_concluidas_por_equivalencia.append(disciplina)
            else:
                resultado_novo_curriculo[disciplina] = {"status": "Pendente", "cor": COR_PADRAO}
                
        # Critério 1: Disciplina sem equivalência e não concluída
        else:
            resultado_novo_curriculo[disciplina] = {"status": "Pendente", "cor": COR_PADRAO}
            
    return resultado_novo_curriculo, novas_concluidas_por_equivalencia

def exibir_resultado(resultado, novas_equivalencias):
    """Exibe o resultado formatado de forma independente de GUI."""
    print("\n--- SITUAÇÃO NO NOVO CURRÍCULO ---")
    for disc, dados in resultado.items():
        print(f"{dados['cor']}{disc}: {dados['status']}{COR_PADRAO}")
        
    # Critério 4: Informar disciplinas novas concluídas por equivalência no final
    print("\n--- RESUMO DE NOVAS DISCIPLINAS CONCLUÍDAS POR EQUIVALÊNCIA ---")
    if novas_equivalencias:
        for disc in novas_equivalencias:
            print(f"{COR_VERDE}- {disc}{COR_PADRAO}")
    else:
        print("Nenhuma nova disciplina foi concluída por equivalência.")

# --- CRITÉRIO 5: CENÁRIOS DE TESTE ---

# Dados base fixos para os currículos
curriculo_atual = ["Algoritmos", "Cálculo I", "Álgebra Linear", "Banco de Dados I"]
novo_curriculo = ["Introdução à Programação", "Cálculo I", "Álgebra Linear", "Banco de Dados Avançado"]
tabela_equivalencias = {
    "Introdução à Programação": "Algoritmos",
    "Banco de Dados Avançado": "Banco de Dados I"
}

print("=== EXECUTANDO CENÁRIOS DE TESTE ===")

# Cenário 1: Aluno recém-ingressado (não concluiu nada)
print("\n> Cenário 1: Aluno sem disciplinas concluídas")
historico_1 = {"Algoritmos": "Pendente", "Cálculo I": "Pendente"}
res_1, novas_1 = verificar_migracao(historico_1, curriculo_atual, novo_curriculo, tabela_equivalencias)
exibir_resultado(res_1, novas_1)

# Cenário 2: Aluno com aprovação direta em matéria comum
print("\n> Cenário 2: Aluno concluiu Cálculo I (comum aos dois)")
historico_2 = {"Cálculo I": "Concluída", "Algoritmos": "Pendente"}
res_2, novas_2 = verificar_migracao(historico_2, curriculo_atual, novo_curriculo, tabela_equivalencias)
exibir_resultado(res_2, novas_2)

# Cenário 3: Aluno com aproveitamento por equivalência
print("\n> Cenário 3: Aluno concluiu Algoritmos (gera equivalência para Introdução à Programação)")
historico_3 = {"Algoritmos": "Concluída"}
res_3, novas_3 = verificar_migracao(historico_3, curriculo_atual, novo_curriculo, tabela_equivalencias)
exibir_resultado(res_3, novas_3)

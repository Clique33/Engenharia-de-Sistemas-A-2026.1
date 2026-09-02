from equivalencia import verificar_migracao, exibir_resultado

def executar_testes():
    """Gera massa de dados simulada e executa os três cenários de teste exigidos."""
    curriculo_atual = ["Algoritmos", "Cálculo I", "Álgebra Linear", "Banco de Dados I"]
    novo_curriculo = ["Introdução à Programação", "Cálculo I", "Álgebra Linear", "Banco de Dados Avançado"]
    tabela_equivalencias = {
        "Introdução à Programação": "Algoritmos",
        "Banco de Dados Avançado": "Banco de Dados I"
    }

    print("=== EXECUTANDO CENÁRIOS DE TESTE ===")

    print("\n> Cenário 1: Aluno sem disciplinas concluídas")
    historico_1 = {"Algoritmos": "Pendente", "Cálculo I": "Pendente"}
    res_1, novas_1 = verificar_migracao(historico_1, curriculo_atual, novo_curriculo, tabela_equivalencias)
    exibir_resultado(res_1, novas_1)

    print("\n> Cenário 2: Aluno concluiu Cálculo I (comum aos dois)")
    historico_2 = {"Cálculo I": "Concluída", "Algoritmos": "Pendente"}
    res_2, novas_2 = verificar_migracao(historico_2, curriculo_atual, novo_curriculo, tabela_equivalencias)
    exibir_resultado(res_2, novas_2)

    print("\n> Cenário 3: Aluno concluiu Algoritmos (gera equivalência para Introdução à Programação)")
    historico_3 = {"Algoritmos": "Concluída"}
    res_3, novas_3 = verificar_migracao(historico_3, curriculo_atual, novo_curriculo, tabela_equivalencias)
    exibir_resultado(res_3, novas_3)

if __name__ == "__main__":
    executar_testes()

# test_simula_migracao.py
from simula_migracao import verificar_migracao, exibir_resultado
from equivalencia import EquivalenciasCurriculares

def executar_testes():
    print("=== EXECUTANDO CENÁRIOS DE TESTE COM INTEGRAÇÃO ===")

    # 1. Instanciando a classe e cadastrando a equivalência real
    sistema_equiv = EquivalenciasCurriculares()
    sistema_equiv.cadastrar("IME04-00627", "FEN06-03559") # IPD -> Algoritmos Computacionais

    # 2. Mock do Novo Currículo (Baseado no JSON da equipe)
    novo_curriculo = {
        "IME01-00508": {"nome": "Cálculo Diferencial e Integral I"},
        "FEN06-03559": {"nome": "Algoritmos Computacionais"}
    }

    print("\n> Cenário 1: Aluno sem disciplinas concluídas")
    historico_1 = [
        {"codigo": "IME01-00508", "nome": "Cálculo Diferencial e Integral I", "status": "nao_cursada"},
        {"codigo": "IME04-00627", "nome": "Introdução ao Processamento de Dados", "status": "nao_cursada"}
    ]
    res_1, novas_1 = verificar_migracao(historico_1, novo_curriculo, sistema_equiv)
    exibir_resultado(res_1, novas_1)

    print("\n> Cenário 2: Aluno concluiu IPD (Gera equivalência para Algoritmos)")
    historico_2 = [
        {"codigo": "IME04-00627", "nome": "Introdução ao Processamento de Dados", "status": "concluida"}
    ]
    res_2, novas_2 = verificar_migracao(historico_2, novo_curriculo, sistema_equiv)
    exibir_resultado(res_2, novas_2)

if __name__ == "__main__":
    executar_testes()
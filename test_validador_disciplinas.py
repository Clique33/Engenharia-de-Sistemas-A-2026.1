from validador_disciplinas import ValidadorDisciplinas

if __name__ == '__main__':
    sistema = ValidadorDisciplinas()
    
    # Setup: Simulando aluno que cursou PROG01 e MAT101
    sistema.carregar_historico(["PROG01", "MAT101"])

    print("Iniciando testes da Issue #19...")

    # Teste 1: Mostrar os pré-requisitos da disciplina (Critério 1)
    reqs = sistema.consultar_pre_requisitos("PROG02")
    if reqs != ["PROG01", "MAT101"]:
        print(f"ERRO TESTE 1: Esperava ['PROG01', 'MAT101'], retornou {reqs}")
        exit()

    # Teste 2: Aluno possui os pré-requisitos (Critério 2 - Permissão)
    pode_cursar = sistema.verificar_permissao("PROG02")
    if not pode_cursar:
        print("ERRO TESTE 2: Aluno cumpriu os requisitos, mas foi bloqueado.")
        exit()

    # Teste 3: Aluno não possui os pré-requisitos (Critério 2 - Bloqueio)
    pode_cursar_eng = sistema.verificar_permissao("ENG456")
    if pode_cursar_eng:
        print("ERRO TESTE 3: Aluno não cumpriu requisitos, mas foi liberado.")
        exit()

    print("Sucesso! Critérios de aceitação validados com precisão.")
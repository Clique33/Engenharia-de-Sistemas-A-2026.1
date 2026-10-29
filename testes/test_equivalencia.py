from equivalencia import EquivalenciasCurriculares

if __name__ == '__main__':
    sistema = EquivalenciasCurriculares()
    sistema.carregar_equivalencias_iniciais()

    # Teste 1: Consulta de uma equivalência válida
    resultado_teste_1 = sistema.consultar("ELE123")
    if resultado_teste_1 != "ENG456":
        print(f"ERRO NO TESTE 1: Esperava 'ENG456', mas o sistema retornou '{resultado_teste_1}'")
        exit()

    # Teste 2: Consulta de uma equivalência inexistente
    resultado_teste_2 = sistema.consultar("MAT999")
    if resultado_teste_2 != None:
        print(f"ERRO NO TESTE 2: Esperava vazio (None), mas o sistema retornou '{resultado_teste_2}'")
        exit()

    # Teste 3: Cadastro manual e consulta
    sistema.cadastrar("PROG01", "COMP10")
    resultado_teste_3 = sistema.consultar("PROG01")
    if resultado_teste_3 != "COMP10":
        print(f"ERRO NO TESTE 3: O cadastro manual falhou.")
        exit()

    print("Aprovado! Todos os testes rodaram com sucesso.")
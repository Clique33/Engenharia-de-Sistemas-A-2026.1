from horas_complementares import HorasComplementares

if __name__ == '__main__':
    # Inicializa o sistema com uma meta hipotética de 100 horas
    sistema = HorasComplementares(meta_horas=100)

    print("Iniciando testes...")

    # Registro de atividades
    sistema.registrar_atividade("Curso de Python", 40)
    sistema.registrar_atividade("Semana de Engenharia", 15)

    # Validação do Critério 1: Total de horas
    total = sistema.calcular_total()
    if total != 55:
        print(f"ERRO CRITÉRIO 1: Esperava 55, mas o sistema retornou {total}")
        exit()

    # Validação do Critério 2: Mostrar atividades
    atividades = sistema.atividades
    if len(atividades) != 2 or atividades[0]["atividade"] != "Curso de Python":
        print("ERRO CRITÉRIO 2: Falha ao listar as atividades registradas.")
        exit()

    print("Sucesso! Os critérios de aceitação foram validados com êxito.")
dados_engenharia_computacao = [
    # ================= 1º PERÍODO =================
    {"nome": "Algoritmos Computacionais I", "codigo": "FEN 06-xxxx", "periodo": 1, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": []},
    {"nome": "Computação, Ética e Transformação Digital", "codigo": "FEN 06-xxxx", "periodo": 1, "ch": 30, "creditos": 2, "categoria": "Computação", "pre_requisitos": []},
    {"nome": "Álgebra Linear", "codigo": "IME 02-xxxxx", "periodo": 1, "ch": 90, "creditos": 6, "categoria": "Básico", "pre_requisitos": []},
    {"nome": "Cálculo Dif. e Int. I", "codigo": "IME 01-17352", "periodo": 1, "ch": 90, "creditos": 6, "categoria": "Básico", "pre_requisitos": []},
    {"nome": "Física Teórica I", "codigo": "FIS 01-xxxx", "periodo": 1, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": []},
    {"nome": "Física Experimental I", "codigo": "FIS 01-xxxx", "periodo": 1, "ch": 30, "creditos": 2, "categoria": "Básico", "pre_requisitos": []},

    # ================= 2º PERÍODO =================
    {"nome": "Estruturas de Informação A", "codigo": "FEN 06-xxxx", "periodo": 2, "ch": 75, "creditos": 5, "categoria": "Computação", "pre_requisitos": ["Algoritmos Computacionais I"]},
    {"nome": "Lógica em Programação", "codigo": "FEN 06-xxxx", "periodo": 2, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Algoritmos Computacionais I"]},
    {"nome": "Cálculo Numérico", "codigo": "IME 06-xxxx", "periodo": 2, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Cálculo Dif. e Int. I"]},
    {"nome": "Cálculo Dif. e Int. II", "codigo": "IME 01-17356", "periodo": 2, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Cálculo Dif. e Int. I"]},
    {"nome": "Física Teórica II", "codigo": "FIS 02-xxxx", "periodo": 2, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Física Teórica I", "Cálculo Dif. e Int. I"]},
    {"nome": "Física Experimental II", "codigo": "FIS 02-xxxx", "periodo": 2, "ch": 30, "creditos": 2, "categoria": "Básico", "pre_requisitos": ["Física Experimental I"]},

    # ================= 3º PERÍODO =================
    {"nome": "Projetos de Extensão", "codigo": "FEN 06-xxxx", "periodo": 3, "ch": 30, "creditos": 2, "categoria": "Extensão", "pre_requisitos": []},
    {"nome": "Análise de Algoritmos I", "codigo": "FEN 06-xxxx", "periodo": 3, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Estruturas de Informação A"]},
    {"nome": "Circuitos Eletrônicos I", "codigo": "FEN 05-xxxx", "periodo": 3, "ch": 90, "creditos": 6, "categoria": "Eletrônica", "pre_requisitos": ["Álgebra Linear"]},
    {"nome": "Probabilidade e Estatística", "codigo": "IME 05-xxxxx", "periodo": 3, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Cálculo Dif. e Int. II"]},
    {"nome": "Cálculo Dif. e Int. III", "codigo": "IME 01-17363", "periodo": 3, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Cálculo Dif. e Int. II"]},
    {"nome": "Eletromag. Bás. Teór.", "codigo": "FIS 03-xxxxx", "periodo": 3, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Física Teórica II", "Cálculo Dif. e Int. II"]},
    {"nome": "Eletromag. Bás. Exp.", "codigo": "FIS 03-xxxxx", "periodo": 3, "ch": 30, "creditos": 2, "categoria": "Básico", "pre_requisitos": ["Física Experimental II"]},

    # ================= 4º PERÍODO =================
    {"nome": "Lab. de Programação", "codigo": "FEN 06-xxxx", "periodo": 4, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Algoritmos Computacionais I"]},
    {"nome": "Laboratório de POO", "codigo": "FEN 06-xxxx", "periodo": 4, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Estruturas de Informação A"]},
    {"nome": "Técnicas Digitais", "codigo": "FEN 05-xxxx", "periodo": 4, "ch": 90, "creditos": 6, "categoria": "Eletrônica", "pre_requisitos": ["Circuitos Eletrônicos I"]},
    {"nome": "Processamento de Sinais e Imagens", "codigo": "FEN 06-xxxx", "periodo": 4, "ch": 75, "creditos": 5, "categoria": "Computação", "pre_requisitos": ["Probabilidade e Estatística"]},
    {"nome": "Física Teórica IV", "codigo": "FIS 04-xxxx", "periodo": 4, "ch": 60, "creditos": 4, "categoria": "Básico", "pre_requisitos": ["Cálculo Dif. e Int. III", "Eletromag. Bás. Teór."]},
    {"nome": "Física Experimental IV", "codigo": "FIS 03-xxxxx", "periodo": 4, "ch": 30, "creditos": 2, "categoria": "Básico", "pre_requisitos": ["Eletromag. Bás. Exp."]},

    # ================= 5º PERÍODO =================
    {"nome": "Teoria dos Grafos e Aplicações", "codigo": "FEN 06-xxxx", "periodo": 5, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Análise de Algoritmos I"]},
    {"nome": "Inteligência Comp. I", "codigo": "FEN 06-xxxx", "periodo": 5, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Lógica em Programação", "Probabilidade e Estatística"]},
    {"nome": "Fundamentos de Comput. I", "codigo": "FEN 06-xxxx", "periodo": 5, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Laboratório de POO", "Técnicas Digitais"]},
    {"nome": "Circuitos em Corrente Contínua", "codigo": "FEN 04-xxxx", "periodo": 5, "ch": 75, "creditos": 5, "categoria": "Elétrica", "pre_requisitos": ["Cálculo Dif. e Int. III", "Eletromag. Bás. Teór."]},
    {"nome": "Materiais Elétricos e Eletrônicos", "codigo": "FEN 05-xxxx", "periodo": 5, "ch": 60, "creditos": 4, "categoria": "Eletrônica", "pre_requisitos": ["Física Teórica IV", "Física Experimental IV"]},

    # ================= 6º PERÍODO =================
    {"nome": "Inteligência Comp. II", "codigo": "FEN 06-xxxx", "periodo": 6, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Inteligência Comp. I"]},
    {"nome": "Mineração de Dados", "codigo": "FEN 06-xxxx", "periodo": 6, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Inteligência Comp. I", "Probabilidade e Estatística"]},
    {"nome": "Engenharia de Sistemas", "codigo": "FEN 06-xxxx", "periodo": 6, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Lab. de Programação"]},
    {"nome": "Arquitetura de Comp. A", "codigo": "FEN 06-xxxx", "periodo": 6, "ch": 75, "creditos": 5, "categoria": "Computação", "pre_requisitos": ["Fundamentos de Comput. I", "Técnicas Digitais"]},
    {"nome": "Circuitos em Corrente Alternada", "codigo": "FEN 04-xxxx", "periodo": 6, "ch": 75, "creditos": 5, "categoria": "Elétrica", "pre_requisitos": ["Circuitos em Corrente Contínua"]},

    # ================= 7º PERÍODO =================
    {"nome": "Teoria de Compiladores I", "codigo": "FEN 06-xxxx", "periodo": 7, "ch": 75, "creditos": 5, "categoria": "Computação", "pre_requisitos": []},
    {"nome": "Redes de Comput. e Sist. Dist.", "codigo": "FEN 06-xxxx", "periodo": 7, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Teoria dos Grafos e Aplicações", "Arquitetura de Comp. A"]},
    {"nome": "Projeto de Banco de Dados", "codigo": "FEN 06-xxxx", "periodo": 7, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Laboratório de POO", "Engenharia de Sistemas"]},
    {"nome": "Projeto de S.O.", "codigo": "FEN 06-xxxx", "periodo": 7, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Arquitetura de Comp. A"]},
    {"nome": "Instalação de Ambientes Comp.", "codigo": "FEN 06-xxxx", "periodo": 7, "ch": 45, "creditos": 3, "categoria": "Computação", "pre_requisitos": ["Circuitos em Corrente Alternada"]},
    {"nome": "Macroeconomia aplicada à Eng.", "codigo": "FEN 09-xxxx", "periodo": 7, "ch": 60, "creditos": 4, "categoria": "Industrial", "pre_requisitos": []},

    # ================= 8º PERÍODO =================
    {"nome": "Empreendedorismo na Engenharia", "codigo": "FEN 09-xxxxx", "periodo": 8, "ch": 45, "creditos": 3, "categoria": "Industrial", "pre_requisitos": []},
    {"nome": "Segurança de Redes", "codigo": "FEN 06-xxxx", "periodo": 8, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Redes de Comput. e Sist. Dist."]},
    {"nome": "Análise e Projeto de Sistemas", "codigo": "FEN 06-xxxx", "periodo": 8, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Engenharia de Sistemas", "Projeto de Banco de Dados"]},
    {"nome": "Sistemas Embutidos", "codigo": "FEN 06-xxxx", "periodo": 8, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Arquitetura de Comp. A"]},
    {"nome": "Computação Paralela e Distribuída", "codigo": "FEN 06-xxxx", "periodo": 8, "ch": 60, "creditos": 4, "categoria": "Computação", "pre_requisitos": ["Redes de Comput. e Sist. Dist.", "Projeto de S.O."]},
    {"nome": "Controle de Processos por Comp. I", "codigo": "FEN 06-xxxx", "periodo": 8, "ch": 75, "creditos": 5, "categoria": "Computação", "pre_requisitos": ["Processamento de Sinais e Imagens", "Circuitos em Corrente Alternada"]},

    # ================= 9º PERÍODO =================
    {"nome": "Metod. Cient. p/ Eng. Computação", "codigo": "FEN 06-xxxxx", "periodo": 9, "ch": 30, "creditos": 2, "categoria": "Computação", "pre_requisitos": ["150 créditos"]},
    {"nome": "Eletiva Restrita (9º Período)", "codigo": "FEN 06-xxxx", "periodo": 9, "ch": 60, "creditos": 4, "categoria": "Eletiva", "pre_requisitos": []},
    {"nome": "Estágio Sup. para Eng. de Computação", "codigo": "FEN 06-xxxx", "periodo": 9, "ch": 165, "creditos": 11, "categoria": "Extensão", "pre_requisitos": ["140 créditos"]},
    {"nome": "Administração Financeira de Projeto", "codigo": "FEN 09-xxxxx", "periodo": 9, "ch": 60, "creditos": 4, "categoria": "Industrial", "pre_requisitos": []},

    # ================= 10º PERÍODO =================
    {"nome": "Projeto de Grad. XI", "codigo": "FEN 06-xxxxx", "periodo": 10, "ch": 30, "creditos": 2, "categoria": "Computação", "pre_requisitos": ["Metod. Cient. p/ Eng. Computação"]},
    {"nome": "Eletiva Restrita (10º Período)", "codigo": "FEN 06-xxxx", "periodo": 10, "ch": 60, "creditos": 4, "categoria": "Eletiva", "pre_requisitos": []}
]

# Aqui você cola a lista gigante 'dados_engenharia_computacao' da mensagem anterior
# dados_engenharia_computacao = [ ... ]

def exibir_fluxograma_conexoes(dados_curriculo):
    print("=== MAPA DE CONEXÕES DO FLUXOGRAMA ===\n")
    
    # Agrupa as matérias por período
    periodos = {}
    for disciplina in dados_curriculo:
        p = disciplina['periodo']
        if p not in periodos:
            periodos[p] = []
        periodos[p].append(disciplina)
        
    # Imprime as conexões organizadas
    for p in sorted(periodos.keys()):
        print(f"--- {p}º PERÍODO ---")
        for materia in periodos[p]:
            nome = materia['nome']
            prereqs = materia['pre_requisitos']
            
            # Verifica se tem setas apontando para a matéria
            if not prereqs:
                print(f"🔹 [{nome}]")
                print("   └── Liberada (Sem pré-requisitos)")
            else:
                conexoes = ", ".join(prereqs)
                print(f"🔸 [{nome}]")
                print(f"   └── 🔗 Conectada com (Depende de): {conexoes}")
        print("\n")

# Executando a função
exibir_fluxograma_conexoes(dados_engenharia_computacao)
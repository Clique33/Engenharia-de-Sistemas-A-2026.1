"Função que calcula disciplinas disponiveis "


def disciplinas_disponiveis(disciplinas, concluidas):
    """
    Retorna as disciplinas que o aluno pode cursar atualmente.

    Args:
        disciplinas (dict):
            Dicionário onde a chave é o nome da disciplina e o valor
            é uma lista com os pré-requisitos.

            Exemplo:
            {
                "Matemática I": [],
                "Matemática II": ["Matemática I"],
                "Programação II": ["Programação I"]
            }

        concluidas (set):
            Conjunto contendo as disciplinas que o aluno já concluiu.

    Returns:
        list:
            Lista das disciplinas liberadas para matrícula.
    """

    disponiveis = []

    for disciplina, pre_requisitos in disciplinas.items():

        # Disciplinas já concluídas não podem aparecer
        if disciplina in concluidas:
            continue

        # Todos os pré-requisitos precisam estar concluídos
        if all(pre in concluidas for pre in pre_requisitos):
            disponiveis.append(disciplina)

    return disponiveis
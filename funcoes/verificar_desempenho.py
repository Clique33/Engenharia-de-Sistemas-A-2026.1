import json
import os

def carregar_historico_aluno(caminho_arquivo: str, matricula: str) -> list:
    """
    Lê o banco de dados JSON e retorna a lista de disciplinas de um aluno específico.
    O resultado pode ser consultado pelo restante do programa.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            banco_dados = json.load(f)

        if matricula in banco_dados:
            return banco_dados[matricula].get("disciplinas", [])
        return []
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return []

def obter_melhores_disciplinas(disciplinas: list) -> list:
    """
    Analisa as notas obtidas pelo aluno e identifica as disciplinas com melhor desempenho.
    Ignora disciplinas sem nota e ordena da maior para a menor.
    """
    # Filtrar Notas None
    disciplinas_com_nota = [
        disciplina for disciplina in disciplinas
        if disciplina.get("nota") is not None
    ]

    # Ordena as disciplinas.
    disciplinas_ordenadas = sorted(
        disciplinas_com_nota,
        key=lambda d: d["nota"],
        reverse=True
    )

    return disciplinas_ordenadas

if __name__ == '__main__':
    print("Carregando JSON e extraindo ranking...")

    caminho_json = os.path.join('Dados', 'historico_alunos.json')

    disciplinas_do_aluno = carregar_historico_aluno(caminho_json, 'matricula_201020668899')

    if disciplinas_do_aluno:
        ranking = obter_melhores_disciplinas(disciplinas_do_aluno)

        print("\n--- TOP 10 DISCIPLINAS ---")
        for i, disc in enumerate(ranking[:10], 1):
            print(f"{i}º Lugar: {disc['nome']} (Nota: {disc['nota']})")

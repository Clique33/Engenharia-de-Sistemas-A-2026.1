import os
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))

from funcoes.validador_disciplinas import ValidadorDisciplinas
from funcoes.curriculo import Curriculo

if __name__ == '__main__':
    # Inicializa o currículo lendo o JSON na pasta Dados/
    caminho_json = caminho_raiz / 'dados' / 'curriculo.json'
    curriculo_atual = Curriculo.carregar_de_arquivo(str(caminho_json))
    sistema = ValidadorDisciplinas(curriculo_atual)
    
    # Setup: Simula aprovação em Circuitos Elétricos I para liberar matérias
    sistema.carregar_historico(["FEN04-00944"])

    # Teste 1: Permissão de disciplina liberada (depende de FEN04-00944)
    if not sistema.verificar_permissao("FEN05-01840"): # Eletronica II
        print("ERRO: Aluno cumpriu requisitos de Eletronica II, mas foi bloqueado.")
        exit()

    # Teste 2: Bloqueio por falta de pré-requisito adicional
    if sistema.verificar_permissao("FEN04-05222"): # Circuitos Eletricos IV
        print("ERRO: Aluno sem todos os requisitos de Circuitos IV foi liberado.")
        exit()

    # Teste 3: Listagem de disponíveis
    disponiveis = sistema.disciplinas_disponiveis()
    if "FEN05-01840" not in disponiveis:
        print("ERRO: Eletronica II deveria estar na lista de disciplinas disponiveis.")
        exit()

    print("Testes finalizados com sucesso. Motor integrado ao JSON.")
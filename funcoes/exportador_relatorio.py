# funcoes/exportador_relatorio.py
import os
import json
from datetime import datetime

def gerar_relatorio_txt(dados_simulacao, caminho_saida="relatorio_migracao.txt"):
    """
    Gera um relatório em formato TXT com o resultado da simulação de migração curricular.
    
    Parâmetros:
    - dados_simulacao (dict): Dicionário contendo informações do aluno, disciplinas aproveitadas,
                              equivalências e disciplinas pendentes.
    - caminho_saida (str): Caminho onde o arquivo será salvo localmente.
    
    Retorna:
    - str: Caminho absoluto do arquivo gerado.
    """
    aluno = dados_simulacao.get("aluno", {})
    aproveitadas = dados_simulacao.get("disciplinas_aproveitadas", [])
    equivalencias = dados_simulacao.get("equivalencias_aplicadas", [])
    pendentes = dados_simulacao.get("disciplinas_pendentes", [])
    
    linhas = []
    linhas.append("=" * 65)
    linhas.append("           RELATÓRIO DE SIMULAÇÃO DE MIGRAÇÃO CURRICULAR")
    linhas.append("=" * 65)
    linhas.append(f"Data da Emissão: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    linhas.append(f"Aluno(a): {aluno.get('nome', 'Não informado')}")
    linhas.append(f"Matrícula: {aluno.get('matricula', 'Não informada')}")
    linhas.append(f"Curso: {aluno.get('curso', 'Não informado')}")
    linhas.append("-" * 65)
    
    linhas.append("\n1. DISCIPLINAS CONCLUÍDAS E APROVEITADAS:")
    if aproveitadas:
        for disc in aproveitadas:
            linhas.append(f"  [X] [{disc.get('codigo')}] {disc.get('nome')} | C.H.: {disc.get('carga_horaria')}h | Status: {disc.get('status', 'Aprovado')}")
    else:
        linhas.append("  Nenhuma disciplina registrada.")
        
    linhas.append("\n2. EQUIVALÊNCIAS APLICADAS NO NOVO CURRÍCULO:")
    if equivalencias:
        for eq in equivalencias:
            linhas.append(f"  -> {eq.get('disciplina_antiga')}  ==>  {eq.get('disciplina_nova')}")
    else:
        linhas.append("  Nenhuma equivalência aplicada.")
        
    linhas.append("\n3. DISCIPLINAS PENDENTES NO NOVO CURRÍCULO:")
    total_ch_pendente = 0
    if pendentes:
        for pend in pendentes:
            ch = pend.get('carga_horaria', 0)
            total_ch_pendente += ch
            linhas.append(f"  [ ] [{pend.get('codigo')}] {pend.get('nome')} | C.H.: {ch}h")
        linhas.append(f"\n  Carga Horária Total Pendente: {total_ch_pendente}h")
    else:
        linhas.append("  Parabéns! Nenhuma disciplina pendente (Currículo concluído).")
        
    linhas.append("\n" + "=" * 65)
    linhas.append("Fim do Relatório - Documento gerado automaticamente pelo sistema de migração.")
    
    conteudo = "\n".join(linhas)
    
    # Garante que o diretório de destino existe
    diretorio = os.path.dirname(caminho_saida)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio, exist_ok=True)
        
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(conteudo)
        
    return os.path.abspath(caminho_saida)
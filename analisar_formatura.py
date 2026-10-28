import json
import os
import math

def carregar_json(caminho: str) -> dict:
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho} não foi encontrado.")
        return {}

def normalizar_codigo(codigo: str) -> str:
    """Remove espaços em branco para garantir que a comparação seja exata."""
    return codigo.replace(" ", "").strip().upper()

def simular_formatura(matricula: str):
    # Carregamento dos dados
    caminho_historico = os.path.join('Dados', 'historico_alunos.json')
    caminho_grade_antiga = os.path.join('Dados', 'Disciplinas_SistemasComputacao.json')
    caminho_grade_nova = os.path.join('Dados', 'grade_nova_computacao_completo.json')

    historico = carregar_json(caminho_historico)
    grade_antiga = carregar_json(caminho_grade_antiga)
    grade_nova = carregar_json(caminho_grade_nova)

    if matricula not in historico:
        print(f"❌ Matrícula {matricula} não encontrada.")
        return

    aluno = historico[matricula]
    nome = aluno.get("nome", "Aluno")

    # Obtém as matérias concluídas NORMALIZANDO o código (removendo espaços)
    concluidas = {
        normalizar_codigo(d['codigo'])
        for d in aluno.get('disciplinas', [])
        if d.get('status') == 'concluida'
    }

    # ==========================================
    # ANÁLISE 1: GRADE ANTIGA
    # ==========================================
    total_obrigatorias_antiga = 0
    cumpridas_antiga = 0

    for cod, disc in grade_antiga.items():
        if disc.get('tipo') == 'Obrigatória':
            total_obrigatorias_antiga += 1
            if normalizar_codigo(cod) in concluidas:
                cumpridas_antiga += 1

    faltam_disc_antiga = total_obrigatorias_antiga - cumpridas_antiga
    semestres_antiga = math.ceil(faltam_disc_antiga / 5.5)

    # ==========================================
    # ANÁLISE 2: GRADE NOVA
    # ==========================================
    ch_total_nova = 0
    ch_cumprida_nova = 0
    disciplinas_faltantes_nova = 0

    for cod, disc in grade_nova.items():
        ch_disciplina = disc.get('carga_horaria', 60)
        ch_total_nova += ch_disciplina

        # Normaliza as equivalências antes de verificar
        equivalencias = [normalizar_codigo(eq) for eq in disc.get('equivalencia_grade_antiga', [])]

        # Verifica se o código da nova grade ou suas equivalências foram cumpridas
        aproveitada = normalizar_codigo(cod) in concluidas or any(eq in concluidas for eq in equivalencias)

        if aproveitada:
            ch_cumprida_nova += ch_disciplina
        else:
            disciplinas_faltantes_nova += 1

    ch_faltante_nova = ch_total_nova - ch_cumprida_nova
    semestres_nova = math.ceil(ch_faltante_nova / 360)

    # ==========================================
    # EXIBIÇÃO
    # ==========================================
    print(f"\n🎓 PROJEÇÃO DE FORMATURA: {nome} ({matricula})")
    print("-" * 60)
    print("📍 CENÁRIO 1: PERMANECER NA GRADE ANTIGA")
    print(f" > Disciplinas Obrigatórias Cumpridas: {cumpridas_antiga} de {total_obrigatorias_antiga}")
    print(f" > Disciplinas Faltantes: {faltam_disc_antiga}")
    print(f" ⏳ Tempo Estimado: {semestres_antiga} semestre(s)")
    print("-" * 60)
    print("📍 CENÁRIO 2: MIGRAR PARA A GRADE NOVA")
    print(f" > Carga Horária Aproveitada: {ch_cumprida_nova}h de {ch_total_nova}h")
    print(f" > Disciplinas Faltantes: {disciplinas_faltantes_nova}")
    print(f" ⏳ Tempo Estimado: {semestres_nova} semestre(s)")
    print("-" * 60)

if __name__ == '__main__':
    simular_formatura("matricula_201510445566") # Lisa Simpson

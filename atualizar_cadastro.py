import json
import os

# ==========================================
# LÓGICA DE DADOS (Leitura e Escrita)
# ==========================================

def carregar_cadastro(caminho_arquivo: str) -> dict:
    """Lê o JSON com os dados cadastrais dos alunos."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_cadastro(caminho_arquivo: str, dados: dict):
    """Sobrescreve o arquivo JSON com as novas informações."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def alterar_informacao_aluno(banco_dados: dict, matricula: str, campo: str, novo_valor: str) -> bool:
    """
    Modifica a informação específica do aluno no dicionário em memória.
    Retorna True se alterou com sucesso, False caso contrário.
    """
    if matricula in banco_dados and campo in banco_dados[matricula]:
        banco_dados[matricula][campo] = novo_valor
        return True
    return False

# ==========================================
# EXECUÇÃO DO PROGRAMA E VISUALIZAÇÃO
# ==========================================

if __name__ == "__main__":
    caminho_json = os.path.join('Dados', 'cadastro_alunos.json')
    db = carregar_cadastro(caminho_json)
    
    matricula_alvo = "matricula_201020668899"
    
    print("--- DADOS ANTES DA ALTERAÇÃO ---")
    print(json.dumps(db.get(matricula_alvo, {}), indent=2, ensure_ascii=False))
    
    # Critério: Poder escolher qual informação alterar
    campo_para_alterar = "telefone"
    novo_telefone = "(21) 90000-0000"
    
    sucesso = alterar_informacao_aluno(db, matricula_alvo, campo_para_alterar, novo_telefone)
    
    if sucesso:
        # Critério: Alteração ser registrada pelo sistema
        salvar_cadastro(caminho_json, db)
        print(f"\n✅ Alteração registrada com sucesso! Campo '{campo_para_alterar}' atualizado.")
        
        print("\n--- DADOS APÓS A ALTERAÇÃO ---")
        print(json.dumps(db.get(matricula_alvo, {}), indent=2, ensure_ascii=False))
    else:
        print("\n❌ Erro: Matrícula ou campo inválido.")
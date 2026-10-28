import tkinter as tk
from tkinter import ttk, messagebox
import math

# ==========================================
# 1. LÓGICA DE NEGÓCIO E CÁLCULOS (Desacoplada)
# ==========================================

def calcular_projecao(ch_total_curso: int, ch_cumprida: int, ch_media_por_semestre: int = 360) -> dict:
    """
    Calcula a projeção de formatura baseada na carga horária.
    Retorna um dicionário com os dados calculados.
    """
    ch_restante = max(0, ch_total_curso - ch_cumprida)
    semestres_restantes = math.ceil(ch_restante / ch_media_por_semestre)
    
    return {
        "ch_cumprida": ch_cumprida,
        "ch_restante": ch_restante,
        "semestres_restantes": semestres_restantes,
        "anos_restantes": round(semestres_restantes / 2, 1)
    }

def simular_migracao(historico_aluno: dict) -> dict:
    """
    Simula o cenário comparativo entre a Grade Antiga e a Grade Nova.
    Em um cenário real, essa função cruzaria os dados com os JSONs das grades.
    Aqui, usamos dados simulados baseados no histórico fornecido.
    """
    # SIMULAÇÃO: Carga horária total hipotética de cada matriz
    CH_TOTAL_ANTIGA = 3600
    CH_TOTAL_NOVA = 3451  # Conforme o novo fluxograma
    
    # SIMULAÇÃO: O que o aluno já cumpriu (aproveitamento cai na grade nova devido a equivalências não diretas)
    ch_cumprida_antiga = historico_aluno.get("ch_cumprida_atual", 1800)
    ch_cumprida_nova = historico_aluno.get("ch_cumprida_migracao", 1650) 
    
    projecao_antiga = calcular_projecao(CH_TOTAL_ANTIGA, ch_cumprida_antiga)
    projecao_nova = calcular_projecao(CH_TOTAL_NOVA, ch_cumprida_nova)
    
    return {
        "antiga": projecao_antiga,
        "nova": projecao_nova
    }

# ==========================================
# 2. INTERFACE VISUAL (Tkinter)
# ==========================================

def criar_card_comparativo(container: tk.Frame, titulo: str, dados: dict, cor_borda: str, cor_fundo: str):
    """Cria um card visual exibindo a projeção de uma grade específica."""
    card = tk.Frame(container, bg=cor_fundo, highlightbackground=cor_borda, highlightthickness=2, padx=15, pady=15)
    
    tk.Label(card, text=titulo, font=("Arial", 12, "bold"), bg=cor_fundo, fg=cor_borda).pack(anchor="w", pady=(0, 10))
    
    tk.Label(card, text=f"✅ Carga Horária Cumprida: {dados['ch_cumprida']}h", font=("Arial", 10), bg=cor_fundo).pack(anchor="w")
    tk.Label(card, text=f"📚 Carga Horária Restante: {dados['ch_restante']}h", font=("Arial", 10), bg=cor_fundo).pack(anchor="w")
    
    # Destaque para o tempo restante
    tk.Label(card, text=f"⏳ Tempo Estimado: {dados['semestres_restantes']} semestres ({dados['anos_restantes']} anos)", 
             font=("Arial", 11, "bold"), bg=cor_fundo, fg="#333333").pack(anchor="w", pady=(10, 0))
    
    return card

# ==========================================
# 3. APLICAÇÃO DE EXEMPLO
# ==========================================

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Simulador de Migração Curricular")
    janela.geometry("600x400")
    janela.configure(bg="#F8F9FA")

    # Simulando a entrada de dados do aluno (ex: Pedro)
    dados_aluno_mock = {
        "nome": "Pedro Guilherme",
        "ch_cumprida_atual": 2100,
        "ch_cumprida_migracao": 1950  # Perdeu 150h na equivalência
    }

    tk.Label(janela, text=f"Projeção de Formatura: {dados_aluno_mock['nome']}", 
             font=("Arial", 14, "bold"), bg="#F8F9FA").pack(pady=20)

    # Executa a regra de negócio
    comparativo = simular_migracao(dados_aluno_mock)

    # Container para os cards lado a lado
    frame_cards = tk.Frame(janela, bg="#F8F9FA")
    frame_cards.pack(fill="x", padx=20)
    
    frame_cards.columnconfigure(0, weight=1)
    frame_cards.columnconfigure(1, weight=1)

    # Card Grade Antiga
    card_antiga = criar_card_comparativo(frame_cards, "Matriz Atual (Antiga)", comparativo["antiga"], "#664D03", "#FFF3CD")
    card_antiga.grid(row=0, column=0, sticky="nsew", padx=10)

    # Card Grade Nova
    card_nova = criar_card_comparativo(frame_cards, "Nova Matriz", comparativo["nova"], "#0F5132", "#D1E7DD")
    card_nova.grid(row=0, column=1, sticky="nsew", padx=10)

    # Conclusão / Recomendação
    vantagem_antiga = comparativo["nova"]["semestres_restantes"] - comparativo["antiga"]["semestres_restantes"]
    if vantagem_antiga > 0:
        msg = f"💡 Conclusão: Ficar na Grade Antiga é mais rápido por {vantagem_antiga} semestre(s)."
        cor_msg = "#856404"
    elif vantagem_antiga < 0:
        msg = f"💡 Conclusão: Migrar para a Grade Nova acelerará a formatura em {abs(vantagem_antiga)} semestre(s)."
        cor_msg = "#155724"
    else:
        msg = "💡 Conclusão: O tempo estimado é o mesmo em ambas as matrizes."
        cor_msg = "#0c5460"

    tk.Label(janela, text=msg, font=("Arial", 11, "italic"), bg="#F8F9FA", fg=cor_msg).pack(pady=30)

    janela.mainloop()
import json
import os
import tkinter as tk
from tkinter import messagebox

# ==========================================
# LÓGICA DE DADOS E BUSCA
# ==========================================

def carregar_banco_disciplinas(caminho_arquivo: str) -> dict:
    """Carrega o JSON com o banco de disciplinas."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        return {}

def buscar_disciplina(banco_dados: dict, termo_busca: str) -> dict:
    """Busca uma disciplina pelo código ou nome."""
    termo = termo_busca.lower().strip()
    for codigo, info in banco_dados.items():
        if termo in codigo.lower() or termo in info["nome"].lower():
            return info
    return None

# ==========================================
# COMPONENTE VISUAL (Tkinter)
# ==========================================

def criar_card_detalhes(container_pai: tk.Frame, dados_disciplina: dict) -> tk.Frame:
    """Gera um card visual. Recebe apenas um dicionário, mantendo o baixo acoplamento."""
    grade = dados_disciplina.get("grade", "")
    bg_color = "#D1E7DD" if grade == "Grade Nova" else "#FFF3CD" if grade == "Grade Antiga" else "#E2E3E5"
    fg_color = "#0F5132" if grade == "Grade Nova" else "#664D03" if grade == "Grade Antiga" else "#41464B"

    card = tk.Frame(container_pai, bg=bg_color, highlightbackground=fg_color, highlightthickness=2, padx=15, pady=15)

    # 1. Indicação da disciplina
    tk.Label(card, text=f"{dados_disciplina.get('codigo')} - {dados_disciplina.get('nome')}", 
             font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color, wraplength=400, justify="left").pack(anchor="w")

    # 2. Grade de origem
    tk.Label(card, text=f"📍 {grade}", font=("Arial", 10, "italic"), bg=bg_color, fg="#495057").pack(anchor="w", pady=(2, 8))

    # 3. Dados acadêmicos
    tk.Label(card, text=f"📚 Créditos: {dados_disciplina.get('creditos', 0)}   |   ⏱️ Carga Horária: {dados_disciplina.get('carga_horaria', 0)}h", 
             font=("Arial", 10), bg=bg_color).pack(anchor="w")

    # 4. Regra de Equivalência
    tk.Label(card, text=f"🔄 Equivalência: {dados_disciplina.get('equivalencia', 'Sem equivalência cadastrada')}", 
             font=("Arial", 10, "bold"), bg=bg_color, fg="#084298", wraplength=400, justify="left").pack(anchor="w", pady=(8, 2))

    # 5. Pré-requisitos
    pre_reqs = dados_disciplina.get("pre_requisitos", [])
    tk.Label(card, text=f"🔒 Pré-requisitos: {', '.join(pre_reqs) if pre_reqs else 'Nenhum'}", 
             font=("Arial", 10), bg=bg_color).pack(anchor="w")

    return card

# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Consulta de Disciplinas e Equivalências")
    janela.geometry("550x350")
    
    # Aponta exatamente para a sua pasta Dados
    caminho_json = os.path.join('Dados', 'grade_nova_computacao.json')
    banco_disciplinas = carregar_banco_disciplinas(caminho_json)

    var_busca = tk.StringVar()
    frame_resultado = tk.Frame(janela)

    def executar_busca():
        termo = var_busca.get()
        if not termo:
            messagebox.showwarning("Aviso", "Digite um código ou nome de matéria.")
            return

        for widget in frame_resultado.winfo_children():
            widget.destroy()

        disciplina = buscar_disciplina(banco_disciplinas, termo)
        if disciplina:
            criar_card_detalhes(frame_resultado, disciplina).pack(fill="x", expand=True)
        else:
            tk.Label(frame_resultado, text="Disciplina não encontrada.", fg="red").pack()

    frame_busca = tk.Frame(janela)
    frame_busca.pack(pady=20, padx=20, fill="x")
    tk.Label(frame_busca, text="Buscar:").pack(side="left")
    tk.Entry(frame_busca, textvariable=var_busca, width=30).pack(side="left", padx=10)
    tk.Button(frame_busca, text="Pesquisar", command=executar_busca).pack(side="left")
    
    frame_resultado.pack(pady=10, padx=20, fill="both", expand=True)
    janela.mainloop()
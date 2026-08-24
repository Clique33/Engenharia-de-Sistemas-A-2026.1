
import tkinter as tk

# Tabela de estilos visuais por status
ESTILOS_STATUS = {
    "concluida":   {"bg": "#D1E7DD", "fg": "#0F5132", "rotulo": "Concluída"},
    "cursando":    {"bg": "#CFE2FF", "fg": "#084298", "rotulo": "Cursando"},
    "disponivel":  {"bg": "#FFF3CD", "fg": "#664D03", "rotulo": "Disponível"},
    "bloqueada":   {"bg": "#F8D7DA", "fg": "#842029", "rotulo": "Bloqueada"},
    "nao_cursada": {"bg": "#E2E3E5", "fg": "#41464B", "rotulo": "Não Cursada"},
}


def criar_card_disciplina(container_pai, dados_disciplina: dict) -> tk.Frame:
    """
    Função geradora do componente visual.
    Recebe um dicionário externo e monta o card dinamicamente.
    """
    status = dados_disciplina.get("status", "nao_cursada")
    estilo = ESTILOS_STATUS.get(status, ESTILOS_STATUS["nao_cursada"])

    # Bloco / Moldura do card
    card = tk.Frame(
        container_pai,
        bg=estilo["bg"],
        highlightbackground=estilo["fg"],
        highlightthickness=2,
        padx=12,
        pady=10
    )

    # Rótulo com Código
    lbl_codigo = tk.Label(
        card,
        text=dados_disciplina.get("codigo", "SEM CÓDIGO"),
        font=("Arial", 10, "bold"),
        bg=estilo["bg"],
        fg=estilo["fg"]
    )
    lbl_codigo.pack(anchor="w")

    # Rótulo com Nome da Disciplina
    lbl_nome = tk.Label(
        card,
        text=dados_disciplina.get("nome", "Disciplina Sem Nome"),
        font=("Arial", 11),
        bg=estilo["bg"],
        fg="#212529",
        wraplength=180,
        justify="left"
    )
    lbl_nome.pack(anchor="w", pady=(2, 6))

    # Indicador textual do Estado
    lbl_status = tk.Label(
        card,
        text=estilo["rotulo"],
        font=("Arial", 9, "italic"),
        bg=estilo["bg"],
        fg=estilo["fg"]
    )
    lbl_status.pack(anchor="e")

    return card



# Exemplo de utilização 
if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Componente de Disciplina")
    janela.geometry("750x220")
    janela.configure(bg="#F8F9FA")

    # Lista de dicionários representando dados externos
    disciplinas_exemplo = [
        {"codigo": "ENG0101", "nome": "Cálculo I", "status": "concluida"},
        {"codigo": "ENG0102", "nome": "Engenharia de Sistemas A", "status": "cursando"},
        {"codigo": "ENG0201", "nome": "CEME", "status": "disponivel"},
        {"codigo": "ENG0301", "nome": "Engenharia de Sistemas B", "status": "bloqueada"},
        {"codigo": "ENG0405", "nome": "Física IV", "status": "nao_cursada"},
    ]

    painel_cards = tk.Frame(janela, bg="#F8F9FA")
    painel_cards.pack(pady=20, padx=20, fill="both", expand=True)

    for coluna, disc in enumerate(disciplinas_exemplo):
        card = criar_card_disciplina(painel_cards, disc)
        card.grid(row=0, column=coluna, padx=8, pady=8, sticky="nsew")

    janela.mainloop()
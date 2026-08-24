import json
import os
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
    Recebe um dicionário com os dados da disciplina e monta o card.
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

    # Rótulo com Código da Matéria
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
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_json = os.path.join(pasta_atual, "Dados", "historico_alunos.json")

    with open(caminho_json, "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    # Extrai a lista de disciplinas
    disciplinas_exemplo = []
    if isinstance(conteudo, dict):
        primeiro_aluno = next(iter(conteudo.values()))
        disciplinas_exemplo = primeiro_aluno.get("disciplinas", [])
    elif isinstance(conteudo, list) and len(conteudo) > 0:
        disciplinas_exemplo = conteudo[0].get("disciplinas", [])

    janela = tk.Tk()
    janela.title("Histórico de Disciplinas - Aluno")
    janela.geometry("900x260")
    janela.configure(bg="#F8F9FA")

    # Canvas para permitir rolagem horizontal
    canvas = tk.Canvas(janela, bg="#F8F9FA", highlightthickness=0)
    canvas.pack(side="top", fill="both", expand=True, padx=15, pady=(15, 0))

    # Barra de rolagem horizontal
    scrollbar_h = tk.Scrollbar(janela, orient="horizontal", command=canvas.xview)
    scrollbar_h.pack(side="bottom", fill="x", padx=15, pady=(0, 10))

    canvas.configure(xscrollcommand=scrollbar_h.set)

    # Container interno onde ficam os cards
    painel_cards = tk.Frame(canvas, bg="#F8F9FA")
    painel_window = canvas.create_window((0, 0), window=painel_cards, anchor="nw")

    # Ajusta o scroll conforme o tamanho do painel interno
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    painel_cards.bind("<Configure>", ajustar_scroll)

    # Renderiza os cards um ao lado do outro
    for coluna, disc in enumerate(disciplinas_exemplo):
        card = criar_card_disciplina(painel_cards, disc)
        card.grid(row=0, column=coluna, padx=8, pady=8, sticky="nsew")

    # Suporte a rolagem horizontal via roda do mouse (Linux/Windows)
    canvas.bind_all("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(int(-1 * (e.delta / 120)), "units"))
    canvas.bind_all("<Shift-Button-4>", lambda e: canvas.xview_scroll(-1, "units"))
    canvas.bind_all("<Shift-Button-5>", lambda e: canvas.xview_scroll(1, "units"))

    janela.mainloop()
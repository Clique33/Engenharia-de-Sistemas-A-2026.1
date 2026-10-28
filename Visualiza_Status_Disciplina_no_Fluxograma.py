from Visualiza_Fluxograma import FluxogramaApp
import componente_disciplina
from verificar_desempenho import carregar_historico_aluno


# Tabela de estilos visuais por status
ESTILOS_STATUS = {
    "concluida":   {"bg": "#D1E7DD", "fg": "#0F5132", "rotulo": "Concluída"},
    "cursando":    {"bg": "#CFE2FF", "fg": "#084298", "rotulo": "Cursando"},
    "disponivel":  {"bg": "#FFF3CD", "fg": "#664D03", "rotulo": "Disponível"},
    "bloqueada":   {"bg": "#F8D7DA", "fg": "#842029", "rotulo": "Bloqueada"},
    "nao_cursada": {"bg": "#E2E3E5", "fg": "#41464B", "rotulo": "Não Cursada"},
}

def carregar_e_exibir_fluxograma(matricula_aluno):
    # PASSO 1: Puxa o histórico escolar do aluno
    historico = carregar_historico_aluno(matricula_aluno)
    
    # PASSO 2: Inicia a interface gráfica do fluxograma
    app = FluxogramaApp()

    for disciplinas in historico:
        codigo = disciplinas.get("codigo")
        
        # Classifica a disciplina (Do arquivo 'componente_disciplina.py')
        status = componente_disciplina.classificar_disciplina(disciplinas)
        
        # Pega a cor correspondente ao status (se não achar, usa Cinza)
        estilo = ESTILOS_STATUS.get(status, ESTILOS_STATUS["nao_cursada"])
        cor_borda = estilo["fg"]  # Usa a cor definida no 'fg' como a cor da borda

        # PASSO 3: MUDANÇA DA BORDA NO TKINTER
        
        # OPÇÃO A: Se o fluxograma foi desenhado dentro de um Canvas do Tkinter
        if hasattr(app, "canvas"):
            # Encontra os elementos desenhados com a tag/código da matéria
            itens = app.canvas.find_withtag(codigo)
            for item in itens:
                # 'outline' altera a cor da linha de contorno/borda no Canvas
                app.canvas.itemconfig(item, outline=cor_borda, width=3)
    # PASSO 4: Mantém a janela do Tkinter aberta
    if hasattr(app, "mainloop"):
        app.mainloop()
    elif hasattr(app, "run"):
        app.run()


import tkinter as tk
from tkinter import messagebox
import platform



LEGENDAS_ESTILO = {
    "Computação": {"bg": "#EE8939", "line": "#D47324"},
    "Eletrônica": {"bg": "#7AD968", "line": "#48A336"},
    "Básico": {"bg": "#FCE679", "line": "#C2AE29"},
    "Industrial": {"bg": "#C994C7", "line": "#915B8E"},
    "Elétrica": {"bg": "#A7AED4", "line": "#6E77A8"},
    "Extensão": {"bg": "#FFFFFF", "line": "#444444"},
    "Eletivas": {"bg": "#F2C99D", "line": "#A88358"}
}


DADOS_DISCIPLINAS = [
    # --- 1º Período ---
    {"id": "alg1", "col": 0, "row": 0, "nome": "Algoritmos\nComputacionais I", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": []},
    {"id": "cetd", "col": 0, "row": 1, "nome": "Computação, Ética e\nTransformação Digital", "codigo": "FEN 00-xxxx", "horas": 30, "creditos": 2, "categoria": "Computação", "pre": []},
    {"id": "algebra", "col": 0, "row": 2, "nome": "Álgebra\nLinear", "codigo": "IME 02-xxxxx", "horas": 90, "creditos": 6, "categoria": "Básico", "pre": []},
    {"id": "cal1", "col": 0, "row": 4, "nome": "Cálculo\nDif. e Int. I", "codigo": "IME 01-17352", "horas": 90, "creditos": 6, "categoria": "Básico", "pre": []},
    
    # --- 2º Período ---
    {"id": "estrut", "col": 1, "row": 0, "nome": "Estruturas de\nInformação A", "codigo": "FEN 06-xxxx", "horas": 75, "creditos": 5, "categoria": "Computação", "pre": ["alg1"]},
    {"id": "logica", "col": 1, "row": 1, "nome": "Lógica em\nProgramação", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["alg1"]},
    {"id": "calcnum", "col": 1, "row": 3, "nome": "Cálculo\nNumérico", "codigo": "IME 05-xxxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["cal1"]},
    {"id": "calc2", "col": 1, "row": 4, "nome": "Cálculo\nDif. e Int. II", "codigo": "IME 01-17356", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["cal1"]},
    {"id": "fis1", "col": 1, "row": 5, "nome": "Física\nTeórica I", "codigo": "FIS 01-xxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": []},
    {"id": "fexp1", "col": 1, "row": 6, "nome": "Física\nExperimental I", "codigo": "FIS 01-xxxx", "horas": 30, "creditos": 2, "categoria": "Básico", "pre": []},
    
    # --- 3º Período ---
    {"id": "ext", "col": 2, "row": 0, "nome": "Projetos de\nExtensão", "codigo": "FEN 06-xxxx", "horas": 30, "creditos": 2, "categoria": "Extensão", "pre": [], "tracejado": True},
    {"id": "alg2", "col": 2, "row": 1, "nome": "Análise de\nAlgoritmos I", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["alg1", "logica"]},
    {"id": "circ1", "col": 2, "row": 2, "nome": "Circuitos\nEletrônicos I", "codigo": "FEN 05-xxxx", "horas": 90, "creditos": 6, "categoria": "Eletrônica", "pre": ["algebra"]},
    {"id": "prob", "col": 2, "row": 3, "nome": "Probabilidade\ne Estatística", "codigo": "IME 05-xxxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["cal1"]},
    {"id": "calc3", "col": 2, "row": 4, "nome": "Cálculo Dif.\ne Int. III", "codigo": "IME 01-17363", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["calc2"]},
    {"id": "fis2", "col": 2, "row": 5, "nome": "Física\nTeórica II", "codigo": "FIS 02-xxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["cal1", "fis1"]},
    {"id": "fexp2", "col": 2, "row": 6, "nome": "Física\nExperimental II", "codigo": "FIS 02-xxxx", "horas": 30, "creditos": 2, "categoria": "Básico", "pre": ["fexp1"]},
    
    # --- 4º Período ---
    {"id": "labprog", "col": 3, "row": 0, "nome": "Lab. de\nProgramação", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["estrut"]},
    {"id": "labpoo", "col": 3, "row": 1, "nome": "Laboratório\nde POO", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["estrut", "logica"]},
    {"id": "tecdig", "col": 3, "row": 2, "nome": "Técnicas\nDigitais", "codigo": "FEN 05-xxxx", "horas": 90, "creditos": 6, "categoria": "Eletrônica", "pre": ["circ1"]},
    {"id": "sinais", "col": 3, "row": 3, "nome": "Processamento de\nSinais e Imagens", "codigo": "FEN 06-xxxx", "horas": 75, "creditos": 5, "categoria": "Computação", "pre": ["prob", "algebra"]},
    {"id": "eletromag", "col": 3, "row": 5, "nome": "Eletromag.\nBás. Teór.", "codigo": "FIS 03-xxxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["fis2"]},
    {"id": "fexp3", "col": 3, "row": 6, "nome": "Eletromag.\nBás. Exp.", "codigo": "FIS 03-xxxxx", "horas": 30, "creditos": 2, "categoria": "Básico", "pre": ["fexp2"]},
    
    # --- 5º Período ---
    {"id": "grafos", "col": 4, "row": 0, "nome": "Teoria dos Grafos\ne Aplicações", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["estrut", "alg2"]},
    {"id": "int1", "col": 4, "row": 1, "nome": "Inteligência\nComp. I", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["labprog"]},
    {"id": "fundcomp", "col": 4, "row": 2, "nome": "Fundamentos\nde Comput. I", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["tecdig"]},
    {"id": "ccd", "col": 4, "row": 4, "nome": "Circuitos em\nCorrente Contínua", "codigo": "FEN 04-xxxx", "horas": 75, "creditos": 5, "categoria": "Elétrica", "pre": ["eletromag"]},
    {"id": "fis4", "col": 4, "row": 5, "nome": "Física\nTeórica IV", "codigo": "FIS 04-xxxx", "horas": 60, "creditos": 4, "categoria": "Básico", "pre": ["eletromag"]},
    {"id": "fexp4", "col": 4, "row": 6, "nome": "Física\nExperimental IV", "codigo": "FIS 03-xxxxx", "horas": 30, "creditos": 2, "categoria": "Básico", "pre": ["fexp3"]},
    
    # --- 6º Período ---
    {"id": "int2", "col": 5, "row": 0, "nome": "Inteligência\nComp. II", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["labprog"]},
    {"id": "mineracao", "col": 5, "row": 1, "nome": "Mineração\nde Dados", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["int1"]},
    {"id": "engsist", "col": 5, "row": 2, "nome": "Engenharia\nde Sistemas", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["labpoo"]},
    {"id": "arq", "col": 5, "row": 3, "nome": "Arquitetura\nde Comp. A", "codigo": "FEN 06-xxxx", "horas": 75, "creditos": 5, "categoria": "Computação", "pre": ["fundcomp"]},
    {"id": "cca", "col": 5, "row": 4, "nome": "Circuitos em\nCorrente Alternada", "codigo": "FEN 04-xxxx", "horas": 75, "creditos": 5, "categoria": "Elétrica", "pre": ["ccd"]},
    {"id": "materiais", "col": 5, "row": 5, "nome": "Materiais Elétricos\ne Eletrônicos", "codigo": "FEN 05-xxxx", "horas": 60, "creditos": 4, "categoria": "Eletrônica", "pre": ["fis4"]},
    
    # --- 7º Período ---
    {"id": "comp1", "col": 6, "row": 0, "nome": "Teoria de\nCompiladores I", "codigo": "FEN 06-xxxx", "horas": 75, "creditos": 5, "categoria": "Computação", "pre": ["alg2"]},
    {"id": "redes", "col": 6, "row": 1, "nome": "Redes de Comput.\ne Sist. Dist.", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": []},
    {"id": "bancodados", "col": 6, "row": 2, "nome": "Projeto de\nBanco de Dados", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["engsist"]},
    {"id": "projso", "col": 6, "row": 3, "nome": "Projeto\nde S.O.", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["arq"]},
    {"id": "instalacoes", "col": 6, "row": 4, "nome": "Instalação de\nAmbientes Comp.", "codigo": "FEN 06-xxxx", "horas": 45, "creditos": 3, "categoria": "Computação", "pre": ["cca"]},
    {"id": "macro", "col": 6, "row": 5, "nome": "Macroeconomia\naplicada à Eng.", "codigo": "FEN 09-xxxx", "horas": 60, "creditos": 4, "categoria": "Industrial", "pre": []},
    
    # --- 8º Período ---
    {"id": "empreend", "col": 7, "row": 0, "nome": "Empreendedorismo\nna Engenharia", "codigo": "FEN 09-xxxxx", "horas": 45, "creditos": 3, "categoria": "Industrial", "pre": []},
    {"id": "segredes", "col": 7, "row": 1, "nome": "Segurança\nde Redes", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["redes"]},
    {"id": "analiseproj", "col": 7, "row": 2, "nome": "Análise e Projeto\nde Sistemas", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["bancodados"]},
    {"id": "sistemasemb", "col": 7, "row": 3, "nome": "Sistemas\nEmbutidos", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["arq"]},
    {"id": "paralela", "col": 7, "row": 4, "nome": "Computação Paralela\ne Distribuída", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Computação", "pre": ["projso"]},
    {"id": "controle", "col": 7, "row": 5, "nome": "Controle de Processos\npor Comp. I", "codigo": "FEN 06-xxxx", "horas": 75, "creditos": 5, "categoria": "Computação", "pre": ["projso"]},
    
    # --- 9º Período ---
    {"id": "metod", "col": 8, "row": 0, "nome": "Metod. Cient. p/\nEng. Computação", "codigo": "FEN 06-xxxxx", "horas": 30, "creditos": 2, "categoria": "Computação", "pre": [], "requisito": "150 cred"},
    {"id": "eletiva9", "col": 8, "row": 1, "nome": "Eletiva\nRestrita", "codigo": "FEN 06-xxxx", "horas": 60, "creditos": 4, "categoria": "Eletivas", "pre": [], "tracejado": True},
    {"id": "estagio", "col": 8, "row": 2, "nome": "Estágio Sup. para\nEng. de Computação", "codigo": "FEN 06-xxxx", "horas": 165, "creditos": 11, "categoria": "Extensão", "pre": [], "requisito": "140 cred", "tracejado": True},
    
    # --- 10º Período ---
    {"id": "projgrad", "col": 9, "row": 0, "nome": "Projeto de\nGrad. XI", "codigo": "FEN 06-xxxxx", "horas": 30, "creditos": 2, "categoria": "Computação", "pre": ["metod"]},
    {"id": "eletiva10", "col": 9, "row": 1, "nome": "Eletiva\nRestrita", "codigo": "FEN 06-xxxxx", "horas": 60, "creditos": 4, "categoria": "Eletivas", "pre": [], "tracejado": True},
    {"id": "admproj", "col": 9, "row": 2, "nome": "Administração\nFinanceira de Projeto", "codigo": "FEN 09-xxxxx", "horas": 60, "creditos": 4, "categoria": "Industrial", "pre": []}
]


DADOS_CO_REQUISITOS = [
    ("fis1", "fexp1"),
    ("fis2", "fexp2"),
    ("eletromag", "fexp3"),
    ("fis4", "fexp4")
]


CUSTOM_ROUTES = {
    ("alg1", "alg2"): 0.85,    
    ("cal1", "prob"): 3.85,    
    ("cal1", "fis2"): 4.85,    
    ("estrut", "labprog"): -0.2,   
    ("estrut", "labpoo"): 0.85,    
    ("logica", "labpoo"): 1.80,
    ("algebra", "sinais"): 2.80,   
    ("estrut", "grafos"): -0.3,    
    ("alg2", "grafos"): 0.70,     
    ("labprog", "int2"): -0.1,     
    ("labpoo", "engsist"): 1.85,   
    ("alg2", "comp1"): -0.4, 
    ("arq", "sistemasemb"): 3.85
}

TEXTO_RODAPE = (
    "O currículo do curso de Engenharia de Computação compreende um total de 3451 horas, 216\ncréditos, sendo:\n"
    "    a) 3120 horas, equivalentes a 208 créditos em disciplinas obrigatórias, sendo 195 horas, 13\n        créditos, de disciplinas obrigatórias com carga horária de Extensão;\n"
    "    b) um mínimo de 120 horas, 8 créditos em disciplinas eletivas restritas;\n"
    "    c) um mínimo de 151 horas em Atividades Curriculares de Extensão (ACE);\n"
    "    d) um mínimo de 60 horas em Atividades Curriculares Complementares (ACC).\n"
    "O curso estabelece o tempo mínimo de integralização em 10 períodos (5 anos) e máximo em 18\nperíodos (9 anos)."
)


class FluxogramaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluxograma Curricular - Engenharia de Computação")
        self.root.geometry("1600x900")
        self.root.configure(bg="#FFFFFF")
        
        self.zoom = 1.0
        self.mapa_disc = {d["id"]: d for d in DADOS_DISCIPLINAS}

        self.construir_ui()
        self.bind_eventos()
        self.renderizar()

    def construir_ui(self):
        header = tk.Frame(self.root, bg="#FFFFFF")
        header.pack(fill=tk.X, pady=15)
        
        tk.Label(header, text="Curso: Engenharia de Computação", font=("Arial", 22, "bold"), bg="#FFFFFF", fg="#111").pack(anchor="center")
        
        container = tk.Frame(self.root, bg="#FFFFFF")
        container.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(container, bg="#FFFFFF", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def bind_eventos(self):
        # Arrastar para mover (Pan)
        self.canvas.bind("<ButtonPress-1>", lambda e: self.canvas.scan_mark(e.x, e.y))
        self.canvas.bind("<B1-Motion>", lambda e: self.canvas.scan_dragto(e.x, e.y, gain=1))
        
        # ZOOM direto no scroll do mouse
        if platform.system() in ('Windows', 'Darwin'):
            self.root.bind("<MouseWheel>", self.gerenciar_scroll)
        else:
            for ev in ["<Button-4>", "<Button-5>"]:
                self.root.bind(ev, self.gerenciar_scroll)

    def gerenciar_scroll(self, event):
        delta = 1 if (event.num == 4 or getattr(event, 'delta', 0) > 0) else -1

        # Zoom IN / Zoom OUT
        if delta > 0:
            self.zoom = min(self.zoom * 1.1, 2.0)
        else:
            self.zoom = max(self.zoom * 0.9, 0.2)  # Permite diminuir bem mais para ver tudo de longe
            
        self.renderizar()

    def renderizar(self):
        self.canvas.delete("all")

        inicio_x, largura_coluna = 50 * self.zoom, 190 * self.zoom
        inicio_y, altura_linha = 100 * self.zoom, 115 * self.zoom 
        w, h = 145 * self.zoom, 75 * self.zoom

        # Fonte que escala livremente para não transbordar no zoom negativo
        fonte_titulos = ("Arial", max(1, int(11 * self.zoom)), "bold")

        # Títulos
        for p in range(1, 11):
            x_txt = inicio_x + (p - 1) * largura_coluna + (w / 2)
            self.canvas.create_text(x_txt, 30 * self.zoom, text=f"{p}º Período", font=fonte_titulos, fill="#222")

        # Posições
        pos = {d["id"]: (inicio_x + d["col"] * largura_coluna, inicio_y + d["row"] * altura_linha) for d in DADOS_DISCIPLINAS}

        # Linhas Sólidas
        for d in DADOS_DISCIPLINAS:
            for id_orig in d.get("pre", []):
                self.desenhar_linha_ortogonal(id_orig, d["id"], pos, w, h, inicio_y, altura_linha)

        # Linhas Tracejadas
        for id_orig, id_dest in DADOS_CO_REQUISITOS:
            out_x, out_y = pos[id_orig][0] + (w / 2), pos[id_orig][1] + h
            in_x, in_y = pos[id_dest][0] + (w / 2), pos[id_dest][1]
            thick = max(1, int(1.5 * self.zoom))
            arrow_s = int(5 * self.zoom)
            self.canvas.create_line(out_x, out_y, in_x, in_y, fill="#555", width=thick, dash=(4,4), arrow=tk.BOTH, arrowshape=(arrow_s, arrow_s+2, arrow_s))

        # Cartões
        for d in DADOS_DISCIPLINAS:
            self.desenhar_cartao(d, pos[d["id"]][0], pos[d["id"]][1], w, h)

        self.desenhar_rodape(inicio_x, inicio_y, altura_linha)
        
        bbox = self.canvas.bbox("all")
        if bbox: self.canvas.configure(scrollregion=(0, 0, bbox[2] + 150, bbox[3] + 150))

    def desenhar_linha_ortogonal(self, id_orig, id_dest, pos, w, h, inicio_y, h_linha):
        out_x, out_y = pos[id_orig][0] + w, pos[id_orig][1] + (h / 2)
        in_x, in_y = pos[id_dest][0], pos[id_dest][1] + (h / 2)
        
        cor = LEGENDAS_ESTILO[self.mapa_disc[id_orig]["categoria"]]["line"]
        thick = max(1, int(1.5 * self.zoom))
        arrow_s = int(6 * self.zoom)

        if (id_orig, id_dest) in CUSTOM_ROUTES:
            track_y = inicio_y + CUSTOM_ROUTES[(id_orig, id_dest)] * h_linha
            step_x = 20 * self.zoom
            
            self.canvas.create_line(
                out_x, out_y, 
                out_x + step_x, out_y,
                out_x + step_x, track_y,
                in_x - step_x, track_y,
                in_x - step_x, in_y,
                in_x, in_y,
                fill=cor, width=thick, arrow=tk.LAST, arrowshape=(arrow_s, arrow_s+3, arrow_s), joinstyle=tk.ROUND
            )
        else:
            mid_x = out_x + (in_x - out_x) / 2
            self.canvas.create_line(out_x, out_y, mid_x, out_y, mid_x, in_y, in_x, in_y, fill=cor, width=thick, arrow=tk.LAST, arrowshape=(arrow_s, arrow_s+3, arrow_s), joinstyle=tk.ROUND)

    def desenhar_cartao(self, d, x, y, w, h):
        cat = LEGENDAS_ESTILO[d["categoria"]]
        dash_estilo = (5, 5) if d.get("tracejado") else ()
        
        card_id = self.canvas.create_rectangle(x, y, x + w, y + h, fill=cat["bg"], outline="#222", dash=dash_estilo, width=max(1, int(1.0*self.zoom)))
        
        # Fontes sem trava de tamanho para escalar perfeitamente no zoom
        f_min = ("Arial", max(1, int(8 * self.zoom)))
        f_med = ("Arial", max(1, int(9 * self.zoom)))
        f_bold = ("Arial", max(1, int(9.5 * self.zoom)), "bold")

        pad_x = max(1, int(10 * self.zoom))
        pad_y = max(1, int(12 * self.zoom))

        self.canvas.create_text(x + pad_x, y + pad_y, text=d["codigo"], font=f_min, fill="#111", anchor="w")
        self.canvas.create_text(x + w/2, y + h/2, text=d["nome"], font=f_bold, fill="#111", width=w - (2 * pad_x), justify="center")
        self.canvas.create_text(x + pad_x, y + h - pad_y, text=str(d["horas"]), font=f_med, fill="#111", anchor="w")
        self.canvas.create_text(x + w - pad_x, y + h - pad_y, text=str(d["creditos"]), font=f_med, fill="#111", anchor="e")

        # Setinhas de pré-requisito estático
        if "requisito" in d:
            rx = x + 35 * self.zoom
            ry = y + h + 18 * self.zoom
            self.canvas.create_text(rx, ry, text=d["requisito"], font=f_min, fill="#222", anchor="w")
            self.canvas.create_line(rx - 8*self.zoom, ry, rx - 8*self.zoom, y + h, arrow=tk.LAST, arrowshape=(max(1, int(3*self.zoom)), max(1, int(4*self.zoom)), max(1, int(2*self.zoom))), fill="#222", width=max(1, int(1.0*self.zoom)))
            self.canvas.create_line(rx - 8*self.zoom, ry, rx, ry, fill="#222", width=max(1, int(1.0*self.zoom)))

        self.canvas.tag_bind(card_id, "<ButtonRelease-1>", lambda e, dados=d: self.mostrar_infos(dados))

    def desenhar_rodape(self, in_x, in_y, h_linha):
        base_y = in_y + (6.5 * h_linha) + 50 * self.zoom
        
        # Fontes escaláveis sem limite
        f_txt = ("Arial", max(1, int(9 * self.zoom)))
        f_bold = ("Arial", max(1, int(10 * self.zoom)), "bold")

        self.canvas.create_text(in_x, base_y, text="Os números situados na parte inferior esquerda e direita representam\ncarga horária e créditos, respectivamente, conferidos à disciplina.", font=f_txt, fill="#444", anchor="w")
        self.canvas.create_text(in_x, base_y + 35*self.zoom, text=TEXTO_RODAPE, font=f_txt, fill="#111", anchor="nw", justify="left")

        leg_x = in_x + (7 * 180 * self.zoom)
        self.canvas.create_text(leg_x, base_y + 10*self.zoom, text="Código para as Disciplinas", font=f_bold, anchor="w", fill="#111")
        
        cats = [("Básico", "Básico"), ("Extensão", "Extensão"), ("Elétrica", "Elétrica"), ("Industrial", "Industrial"), 
                ("Computação", "Computação"), ("Eletrônica", "Eletrônica"), ("Eletivas", "Eletivas")]
        
        box_s = 14 * self.zoom
        for i, (nome, ch) in enumerate(cats):
            col = i % 2
            row = i // 2
            lx = leg_x + (col * 110 * self.zoom)
            ly = base_y + 35*self.zoom + (row * 22 * self.zoom)
            
            dash_box = (2,2) if "tracejado" in nome.lower() or nome == "Extensão" else ()
            self.canvas.create_rectangle(lx, ly, lx + box_s, ly + box_s, fill=LEGENDAS_ESTILO[ch]["bg"], outline="#222", dash=dash_box, width=max(1, int(1.0*self.zoom)))
            self.canvas.create_text(lx + box_s + 10*self.zoom, ly + box_s/2, text=nome, font=f_txt, anchor="w", fill="#111")

    def mostrar_infos(self, d):
        nome_str = d['nome'].replace('\n', ' ')
        pre_str = ", ".join([self.mapa_disc[p]["nome"].replace('\n', ' ') for p in d.get("pre", [])]) if d.get("pre") else "Nenhum"
        
        infos = f"Disciplina: {nome_str}\nCódigo: {d['codigo']}\nPeríodo Original: {d.get('col', 0) + 1}º\nCategoria: {d['categoria']}\n\nPré-requisitos: {pre_str}"
        messagebox.showinfo("Dados da Matéria", infos)


if __name__ == "__main__":
    root = tk.Tk()
    app = FluxogramaApp(root)
    root.mainloop()
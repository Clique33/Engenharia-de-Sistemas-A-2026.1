
class Disciplina:
    def __init__(self, nome, periodo):
        self.nome = nome 
        self.periodo = periodo


class Curriculo:
    
    def __init__(self, curso, disciplinas=[None], periodos=8):

        self.curso = curso
        self.disciplinas = disciplinas
        self.periodos = periodos

    def adicionar_disciplina(self, disciplina):

        self.disciplinas.append(disciplina)

    def mostrar_disciplinas(self):

        vazio = 0
        print(type(self.disciplinas))        

        # for d in self.disciplinas:
        #     print(d.nome)


c = Curriculo()
c.adicionar_disciplina()
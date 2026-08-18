
class Disciplina:
    def __init__(self, nome, periodo):
        self.nome = nome 
        self.periodo = periodo


class Curriculo:
    
    def __init__(self, curso, disciplinas=[], periodos=8):

        self.curso = curso
        self.disciplinas = disciplinas
        self.periodos = periodos

    def adicionar_disciplina(self, disciplina: Disciplina):

        buffer = disciplina

        self.disciplinas.append(buffer)



        
    def mostrar_disciplinas(self):


        tamanho = len(self.disciplinas)

        if tamanho == 0: 
            print('Curso sem disciplinas')
            return -1

        for disciplina in self.disciplinas:
            print(disciplina.nome)


calculo = Disciplina("calculo", 1)


c = Curriculo("Engenharia da computacao")
print(c.curso)
c.adicionar_disciplina(calculo)

c.mostrar_disciplinas()
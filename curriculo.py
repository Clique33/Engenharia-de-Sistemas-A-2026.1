import disciplina



class Curriculo:
    
    def __init__(self, curso, disciplinas=[], periodos=8):

        self.curso = curso
        self.disciplinas = disciplinas
        self.periodos = periodos
    

    def adicionar_disciplina(self, disciplina: disciplina.Disciplina):
        buffer = disciplina

        for d in self.disciplinas:
            if disciplina.codigo == d.codigo:
                print("a disciplina ja existe")
                return -1
            
        self.disciplinas.append(buffer)

    def buscar_disciplina(self, codigo):

        for disciplina in self.disciplinas:
            if (codigo == disciplina.codigo):
                return disciplina

        return -1

    def disciplinas_por_periodo(self, periodo):

        print(f"Disciplinas do {periodo}º: ")
        for disciplina in self.disciplinas:
            if periodo == disciplina.periodo_recomendado:

                print(f"Codigo da disciplina: {disciplina.codigo}")
                print(f"Nome da disciplina: {disciplina.nome}")
                print(f"Periodo da disciplina: {disciplina.periodo} \n")
                
        


    def mostrar_disciplinas(self):


        tamanho = len(self.disciplinas)

        if tamanho == 0: 
            print("Curso sem disciplinas \n")

            return -1
        
        print(f"\nImprimindo disciplinas do curso de {self.curso}:")

        for disciplina in self.disciplinas:
            print(f"\nCodigo da disciplina: {disciplina.codigo}")
            print(f"Nome da disciplina: {disciplina.nome}")
            print(f"Periodo da disciplina: {disciplina.periodo_recomendado} \n")
            


class Disciplina:
    def __init__(self, nome, codigo, periodo):
        self.nome = nome 
        self.periodo = periodo
        self.codigo = codigo


class Curriculo:
    
    def __init__(self, curso, disciplinas=[], periodos=8):

        self.curso = curso
        self.disciplinas = disciplinas
        self.periodos = periodos

    def adicionar_disciplina(self, disciplina: Disciplina):

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
            if periodo == disciplina.periodo:

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
            print(f"Periodo da disciplina: {disciplina.periodo} \n")
            

#TESTE

def criaCurriculo(nome="curso", disciplinas=[]):
    
    
    c = Curriculo(nome)
    
    for disciplina in disciplinas:
        d = Disciplina(disciplina.nome, disciplina.codigo, disciplina.periodo)
        c.adicionar_disciplina(d)

    c.mostrar_disciplinas()


def cria_disciplinas(numero):

    disciplinas = []
    i=0
    while i < numero:
        
        nome = input("\nDigite o nome da disciplina:")
        codigo = int(input("Digite o codigo da disciplina:"))
        periodo = int(input("Digite o periodo da disciplina:"))
        
        disciplina = Disciplina(nome, codigo, periodo)
        disciplinas.append(disciplina)
        i+=1

    return disciplinas

disciplinas = cria_disciplinas(2)

criaCurriculo("Engenharia da computacao", disciplinas)
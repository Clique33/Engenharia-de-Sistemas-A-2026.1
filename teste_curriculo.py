
#TESTE

def criaCurriculo(nome="curso", disciplinas=[]):
    
    
    c = Curriculo(nome)
    
    for dp in disciplinas:
        d = disciplina.Disciplina(dp.codigo, dp.nome, 60, dp.periodo_recomendado, [])
        c.adicionar_disciplina(d)


    c.mostrar_disciplinas()


def cria_disciplinas(numero):

    disciplinas = []
    i=0
    while i < numero:
        
        nome = input("\nDigite o nome da disciplina:")
        codigo = int(input("Digite o codigo da disciplina:"))
        periodo = int(input("Digite o periodo da disciplina:"))
        
        dp = disciplina.Disciplina(codigo, nome, 60, periodo, [])
        disciplinas.append(dp)
        i+=1

    return disciplinas

disciplinas = cria_disciplinas(2)

criaCurriculo("Engenharia da computacao", disciplinas)
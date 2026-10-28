from leitor_historico import LeitorHistorico, DisciplinaHistorico

class ClassificadorHistorico:
    """Responsável por classificar as disciplinas do histórico escolar do aluno."""
    
    # Padrões comuns de reconhecimento de status no histórico
    STATUS_APROVADO = ["APROVADO", "AP", "APR", "DISPENSADO", "APROVADO POR NOTA"]
    STATUS_REPROVADO = ["REPROVADO", "RP", "REP", "REPROVADO POR FREQUENCIA"]
    STATUS_CURSANDO = ["CURSANDO", "MATRICULADO", "EM ANDAMENTO"]

    def __init__(self, leitor_historico: LeitorHistorico):
        self.leitor = leitor_historico

    def classificar_disciplinas(self) -> dict:
        """
        Analisa o histórico e categoriza as disciplinas em:
        - aprovadas
        - reprovadas
        - cursando
        - nao_concluidas
        """
        disciplinas = self.leitor.obter_disciplinas()
        
        resultado = {
            "aprovadas": [],
            "reprovadas": [],
            "cursando": [],
            "nao_concluidas": []
        }

        for disc in disciplinas:
            situacao = disc.situacao.strip().upper()

            if situacao in self.STATUS_APROVADO:
                resultado["aprovadas"].append(disc)
            elif situacao in self.STATUS_REPROVADO:
                resultado["reprovadas"].append(disc)
            elif situacao in self.STATUS_CURSANDO:
                resultado["cursando"].append(disc)
            else:
                resultado["nao_concluidas"].append(disc)

        return resultado
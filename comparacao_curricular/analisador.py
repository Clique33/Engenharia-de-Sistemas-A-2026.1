class AnalisadorCurriculo:
    def __init__(self, historico_aluno, curriculo_atual, curriculo_novo):
        self.historico_aluno = historico_aluno
        self.curriculo_atual = curriculo_atual
        self.curriculo_novo = curriculo_novo

    def processar_status(self, curriculo):
        resultado = []
        for disc in curriculo:
            nome = disc["nome"]
            
            # 1. Verifica se já foi concluída exatamente com o mesmo nome
            if nome in self.historico_aluno:
                resultado.append({"nome": nome, "status": "concluida"})
                continue
                
            # 2. Verifica se foi aproveitada por equivalência
            equivalencia = disc.get("equivalente_a")
            if equivalencia and equivalencia in self.historico_aluno:
                resultado.append({
                    "nome": nome, 
                    "status": "equivalencia", 
                    "detalhe": f"Equivalente a: {equivalencia}"
                })
                continue
            
            # 3. Verifica se é uma disciplina totalmente nova do currículo recente
            if disc.get("nova_disciplina"):
                resultado.append({"nome": nome, "status": "nova"})
                continue
                
            # 4. Caso contrário, está pendente
            resultado.append({"nome": nome, "status": "pendente"})
            
        return resultado

    def gerar_relatorio(self):
        return {
            "curriculo_atual": self.processar_status(self.curriculo_atual),
            "curriculo_novo": self.processar_status(self.curriculo_novo)
        }
    
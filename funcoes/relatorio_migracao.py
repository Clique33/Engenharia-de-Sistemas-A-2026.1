import os
from typing import Dict, List, Any

class RelatorioMigracao:
    """Responsável por gerar e exportar o relatório de simulação de migração curricular."""
    
    def __init__(self, matricula: str, nome_aluno: str, curriculo_origem: str, curriculo_destino: str):
        self.matricula = matricula
        self.nome_aluno = nome_aluno
        self.curriculo_origem = curriculo_origem
        self.curriculo_destino = curriculo_destino

    def formatar_relatorio_txt(
        self, 
        disciplinas_aproveitadas: List[Dict[str, Any]], 
        disciplinas_pendentes: List[Dict[str, Any]], 
        ch_aproveitada: int, 
        ch_pendente: int
    ) -> str:
        """Gera o texto formatado com todas as informações da simulação de migração."""
        linhas = []
        linhas.append("============================================================")
        linhas.append("         SISA - RELATÓRIO DE SIMULAÇÃO DE MIGRAÇÃO          ")
        linhas.append("============================================================")
        linhas.append(f"Aluno: {self.nome_aluno} (Matrícula: {self.matricula})")
        linhas.append(f"Currículo Origem : {self.curriculo_origem}")
        linhas.append(f"Currículo Destino: {self.curriculo_destino}")
        linhas.append("------------------------------------------------------------\n")

        linhas.append("1. DISCIPLINAS APROVEITADAS / EQUIVALÊNCIAS APLICADAS:")
        if not disciplinas_aproveitadas:
            linhas.append("   (Nenhuma disciplina aproveitada)")
        else:
            for item in disciplinas_aproveitadas:
                origem = item.get("cod_origem", "N/A")
                destino = item.get("cod_destino", "N/A")
                nome = item.get("nome_destino", "Disciplina sem nome")
                ch = item.get("ch", 0)
                linhas.append(f"   - [{origem} -> {destino}] {nome} ({ch}h)")
        
        linhas.append(f"\n   Total de Carga Horária Aproveitada: {ch_aproveitada}h")
        linhas.append("------------------------------------------------------------\n")

        linhas.append("2. DISCIPLINAS PENDENTES NO NOVO CURRÍCULO:")
        if not disciplinas_pendentes:
            linhas.append("   (Parabéns! Nenhuma disciplina pendente)")
        else:
            for item in disciplinas_pendentes:
                codigo = item.get("codigo", "N/A")
                nome = item.get("nome", "Disciplina sem nome")
                ch = item.get("ch", 0)
                linhas.append(f"   - [{codigo}] {nome} ({ch}h)")

        linhas.append(f"\n   Total de Carga Horária Pendente: {ch_pendente}h")
        linhas.append("============================================================")
        
        return "\n".join(linhas)

    def exportar_txt(
        self, 
        caminho_saida: str, 
        disciplinas_aproveitadas: List[Dict[str, Any]], 
        disciplinas_pendentes: List[Dict[str, Any]], 
        ch_aproveitada: int, 
        ch_pendente: int
    ) -> str:
        """Exporta e salva localmente o relatório no formato TXT."""
        conteudo = self.formatar_relatorio_txt(
            disciplinas_aproveitadas, 
            disciplinas_pendentes, 
            ch_aproveitada, 
            ch_pendente
        )
        
        try:
            diretorio = os.path.dirname(caminho_saida)
            if diretorio and not os.path.exists(diretorio):
                os.makedirs(diretorio, exist_ok=True)
                
            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            return caminho_saida
        except Exception as e:
            raise RuntimeError(f"Erro ao exportar o relatório TXT: {e}")
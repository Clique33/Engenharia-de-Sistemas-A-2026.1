# funcoes/test_exportador_relatorio.py
import os
import unittest
from exportador_relatorio import gerar_relatorio_txt
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../funcoes"))
)


class TestExportadorRelatorio(unittest.TestCase):
    def setUp(self):
        self.dados_teste = {
            "aluno": {
                "nome": "Maria Souza",
                "matricula": "202456789",
                "curso": "Engenharia de Software"
            },
            "disciplinas_aproveitadas": [
                {"codigo": "MAT101", "nome": "Cálculo I", "carga_horaria": 60, "status": "Aprovado"}
            ],
            "equivalencias_aplicadas": [
                {"disciplina_antiga": "PROG101 (Fundamentos)", "disciplina_nova": "ES103 (Programação Orientada a Objetos)"}
            ],
            "disciplinas_pendentes": [
                {"codigo": "ES202", "nome": "Requisitos de Software", "carga_horaria": 60},
                {"codigo": "ES203", "nome": "Arquitetura de Software", "carga_horaria": 60}
            ]
        }
        self.arquivo_teste = "relatorio_teste.txt"

    def tearDown(self):
        if os.path.exists(self.arquivo_teste):
            os.remove(self.arquivo_teste)

    def test_geracao_arquivo_e_conteudo(self):
        caminho = gerar_relatorio_txt(self.dados_teste, self.arquivo_teste)
        
        # Verifica se o arquivo foi salvo localmente
        self.assertTrue(os.path.exists(caminho))
        
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
            
        # Valida se as informações do aluno e disciplinas estão presentes
        self.assertIn("Maria Souza", conteudo)
        self.assertIn("Cálculo I", conteudo)
        self.assertIn("ES103 (Programação Orientada a Objetos)", conteudo)
        self.assertIn("Requisitos de Software", conteudo)
        self.assertIn("Carga Horária Total Pendente: 120h", conteudo)

if __name__ == "__main__":
    unittest.main()
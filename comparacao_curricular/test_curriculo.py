import unittest
from analisador import AnalisadorCurriculo

class TestAnalisadorCurriculo(unittest.TestCase):
    def setUp(self):
        # Dado que o aluno possui "Física I" e "Cálculo I" concluídas no currículo antigo
        self.historico = ["Cálculo I", "Física I"]
        
        self.curriculo_antigo = [
            {"nome": "Cálculo I"},
            {"nome": "Física I"},
            {"nome": "Sistemas de Controle"}
        ]
        
        self.curriculo_novo = [
            {"nome": "Cálculo I"},
            {"nome": "Física Aplicada à Computação", "equivalente_a": "Física I"},
            {"nome": "Sistemas de Controle"},
            {"nome": "Inteligência Artificial", "nova_disciplina": True}
        ]
        
        self.analisador = AnalisadorCurriculo(
            self.historico, self.curriculo_antigo, self.curriculo_novo
        )

    def test_impacto_migracao_curriculo_novo(self):
        # Quando a análise é executada
        relatorio = self.analisador.gerar_relatorio()
        disciplinas_novo = relatorio["curriculo_novo"]
        
        # Então as classificações visuais (status) devem estar corretas
        status_calculo = next(d for d in disciplinas_novo if d["nome"] == "Cálculo I")
        self.assertEqual(status_calculo["status"], "concluida")
        
        status_fisica = next(d for d in disciplinas_novo if d["nome"] == "Física Aplicada à Computação")
        self.assertEqual(status_fisica["status"], "equivalencia")
        self.assertEqual(status_fisica["detalhe"], "Equivalente a: Física I")
        
        status_ia = next(d for d in disciplinas_novo if d["nome"] == "Inteligência Artificial")
        self.assertEqual(status_ia["status"], "nova")

if __name__ == '__main__':
    unittest.main()
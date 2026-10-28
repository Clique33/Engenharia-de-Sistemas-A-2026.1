import unittest
import tempfile
import os
import json
from leitor_historico import LeitorHistorico
from classificador_historico import ClassificadorHistorico

class TestClassificadorHistorico(unittest.TestCase):
    def setUp(self):
        # Cria um histórico simulado com diferentes situações
        self.dados_teste = {
            "historico": [
                {"codigo": "MAT101", "nome": "Cálculo I", "situacao": "APROVADO"},
                {"codigo": "FIS101", "nome": "Física I", "situacao": "REPROVADO"},
                {"codigo": "COMP101", "nome": "Algoritmos", "situacao": "CURSANDO"},
                {"codigo": "EST101", "nome": "Estatística", "situacao": "TRANCADO"}
            ]
        }
        self.arquivo_temp = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix='.json')
        json.dump(self.dados_teste, self.arquivo_temp)
        self.arquivo_temp.close()

        leitor = LeitorHistorico(self.arquivo_temp.name)
        self.classificador = ClassificadorHistorico(leitor)

    def tearDown(self):
        if os.path.exists(self.arquivo_temp.name):
            os.unlink(self.arquivo_temp.name)

    def test_identifica_aprovadas(self):
        resultado = self.classificador.classificar_disciplinas()
        self.assertEqual(len(resultado["aprovadas"]), 1)
        self.assertEqual(resultado["aprovadas"][0].codigo, "MAT101")

    def test_identifica_reprovadas(self):
        resultado = self.classificador.classificar_disciplinas()
        self.assertEqual(len(resultado["reprovadas"]), 1)
        self.assertEqual(resultado["reprovadas"][0].codigo, "FIS101")

    def test_identifica_cursando(self):
        resultado = self.classificador.classificar_disciplinas()
        self.assertEqual(len(resultado["cursando"]), 1)
        self.assertEqual(resultado["cursando"][0].codigo, "COMP101")

    def test_identifica_nao_concluidas(self):
        resultado = self.classificador.classificar_disciplinas()
        self.assertEqual(len(resultado["nao_concluidas"]), 1)
        self.assertEqual(resultado["nao_concluidas"][0].codigo, "EST101")

if __name__ == '__main__':
    unittest.main()
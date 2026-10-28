import unittest
import os
import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no path para importar 'funcoes'
caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))

from funcoes.curriculo import Curriculo, Disciplina


class TestCurriculo(unittest.TestCase):

    def test_carregamento_curriculo(self):
        caminho_json = caminho_raiz / "Dados" / "curriculo.json"
        curriculo = Curriculo.carregar_de_arquivo(caminho_json)

        self.assertGreater(len(curriculo.disciplinas), 0)

        compiladores = curriculo.obter_disciplina("FEN06-05038")
        self.assertIsNotNone(compiladores)
        self.assertEqual(compiladores.nome, "Compiladores")
        self.assertEqual(getattr(compiladores, 'periodo_recomendado', None), 10)
        self.assertEqual(compiladores.carga_horaria, 75)
        self.assertIn("FEN06-04664", compiladores.pre_requisitos)

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            Curriculo.carregar_de_arquivo("arquivo_invalido.json")


if __name__ == "__main__":
    unittest.main()
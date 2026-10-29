import unittest
import sys
from pathlib import Path

caminho_raiz = Path(__file__).resolve().parent.parent
if str(caminho_raiz) not in sys.path:
    sys.path.append(str(caminho_raiz))

from funcoes.curriculo import Curriculo


class TestCurriculo(unittest.TestCase):
    def test_carregamento_curriculo(self):
        curriculo = Curriculo.carregar_de_arquivo("dados/curriculo.json")
        self.assertIsNotNone(curriculo)
        # Garante que carregou pelo menos uma disciplina da grade
        self.assertTrue(len(curriculo.disciplinas) > 0)


if __name__ == "__main__":
    unittest.main()
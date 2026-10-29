import unittest
from curriculo import Curriculo, Disciplina


class TestCurriculo(unittest.TestCase):

    def test_carregamento_curriculo(self):
        curriculo = Curriculo.carregar_de_arquivo("curriculo.json")

        self.assertGreater(len(curriculo.disciplinas), 0)

        compiladores = curriculo.obter_disciplina("FEN06-05038")
        self.assertIsNotNone(compiladores)
        self.assertEqual(compiladores.nome, "Compiladores")
        self.assertEqual(compiladores.periodo, 10)
        self.assertEqual(compiladores.creditos, 4)
        self.assertEqual(compiladores.carga_horaria, 75)
        self.assertIn("FEN06-04664", compiladores.pre_requisitos)

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            Curriculo.carregar_de_arquivo("arquivo_invalido.json")


if __name__ == "__main__":
    unittest.main()
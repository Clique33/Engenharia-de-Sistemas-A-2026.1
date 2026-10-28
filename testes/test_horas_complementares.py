import unittest
import tempfile
import os
import sys 
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../funcoes"))
)
from horas_complementares import HorasComplementares

class TestHorasComplementares(unittest.TestCase):
    def setUp(self):
        self.hc = HorasComplementares()
        self.hc.adicionar_carga_extensao("Projeto Social Comunitário", 30)
        self.hc.adicionar_atividade_complementar("Participação em Congresso Acadêmico", 20, "Ensino")
        self.hc.adicionar_atividade_curricular_extensao("EXT101", "Extensão Tecnológica Aplicada", 40)

    def test_salvar_e_carregar_json(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', encoding='utf-8') as temp:
            caminho_temp = temp.name

        try:
            # Salva os dados
            self.hc.salvar_json(caminho_temp)
            self.assertTrue(os.path.exists(caminho_temp))

            # Carrega os dados de volta
            hc_carregado = HorasComplementares.carregar_json(caminho_temp)

            # Valida preservação de Carga de Extensão
            self.assertEqual(len(hc_carregado.carga_extensao), 1)
            self.assertEqual(hc_carregado.carga_extensao[0]["descricao"], "Projeto Social Comunitário")
            self.assertEqual(hc_carregado.carga_extensao[0]["horas"], 30)

            # Valida preservação de Atividade Complementar
            self.assertEqual(len(hc_carregado.atividade_complementar), 1)
            self.assertEqual(hc_carregado.atividade_complementar[0]["descricao"], "Participação em Congresso Acadêmico")
            self.assertEqual(hc_carregado.atividade_complementar[0]["horas"], 20)
            self.assertEqual(hc_carregado.atividade_complementar[0]["categoria"], "Ensino")

            # Valida preservação de Atividade Curricular de Extensão
            self.assertEqual(len(hc_carregado.atividade_curricular_extensao), 1)
            self.assertEqual(hc_carregado.atividade_curricular_extensao[0]["codigo"], "EXT101")
            self.assertEqual(hc_carregado.atividade_curricular_extensao[0]["nome"], "Extensão Tecnológica Aplicada")
            self.assertEqual(hc_carregado.atividade_curricular_extensao[0]["horas"], 40)

            # Valida o cálculo total de horas (30 + 20 + 40 = 90)
            self.assertEqual(hc_carregado.total_horas(), 90)

        finally:
            if os.path.exists(caminho_temp):
                os.unlink(caminho_temp)

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            HorasComplementares.carregar_json("caminho_inexistente_abc.json")

    def test_json_invalido(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', encoding='utf-8') as temp:
            temp.write("{ 'formato_invalido': sem_fechar ... ")
            caminho_temp = temp.name

        try:
            with self.assertRaises(ValueError):
                HorasComplementares.carregar_json(caminho_temp)
        finally:
            if os.path.exists(caminho_temp):
                os.unlink(caminho_temp)

if __name__ == '__main__':
    unittest.main()
import unittest
import os
import json
import tempfile
from leitor_historico import LeitorHistorico, DisciplinaHistorico

class TestLeitorHistorico(unittest.TestCase):
    def setUp(self):
        # Criação de um arquivo temporário simulando o histórico escolar
        self.dados_teste = {
            "matricula": "2026001",
            "nome": "Aluno Teste",
            "historico": [
                {
                    "codigo": "COMP101",
                    "nome": "Introdução à Computação",
                    "situacao": "APROVADO",
                    "periodo": "2025.1",
                    "media": 8.5
                },
                {
                    "codigo": "COMP102",
                    "nome": "Algoritmos e Estruturas de Dados",
                    "situacao": "CURSANDO",
                    "periodo": "2026.1"
                }
            ]
        }
        self.arquivo_temp = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix='.json')
        json.dump(self.dados_teste, self.arquivo_temp)
        self.arquivo_temp.close()
        self.leitor = LeitorHistorico(self.arquivo_temp.name)

    def tearDown(self):
        if os.path.exists(self.arquivo_temp.name):
            os.unlink(self.arquivo_temp.name)

    def test_abrir_arquivo_e_identificar_disciplinas(self):
        disciplinas = self.leitor.obter_disciplinas()
        self.assertEqual(len(disciplinas), 2)
        
        # Verifica armazenamento de código, nome e situação da primeira disciplina
        self.assertEqual(disciplinas[0].codigo, "COMP101")
        self.assertEqual(disciplinas[0].nome, "Introdução à Computação")
        self.assertEqual(disciplinas[0].situacao, "APROVADO")

        # Verifica segunda disciplina
        self.assertEqual(disciplinas[1].codigo, "COMP102")
        self.assertEqual(disciplinas[1].nome, "Algoritmos e Estruturas de Dados")
        self.assertEqual(disciplinas[1].situacao, "CURSANDO")

    def test_arquivo_inexistente(self):
        leitor_invalido = LeitorHistorico("caminho_inexistente_abc.json")
        with self.assertRaises(FileNotFoundError):
            leitor_invalido.obter_disciplinas()

    def test_json_invalido(self):
        arquivo_invalido = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix='.json')
        arquivo_invalido.write("{ 'json': 'invalido' sem fechar ... ")
        arquivo_invalido.close()

        leitor_invalido = LeitorHistorico(arquivo_invalido.name)
        with self.assertRaises(ValueError):
            leitor_invalido.obter_disciplinas()
        
        os.unlink(arquivo_invalido.name)

if __name__ == '__main__':
    unittest.main()
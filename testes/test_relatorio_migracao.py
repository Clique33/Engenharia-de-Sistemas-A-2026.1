import unittest
import tempfile
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../funcoes"))
)


from relatorio_migracao import RelatorioMigracao



class TestRelatorioMigracao(unittest.TestCase):
    def setUp(self):
        self.relatorio = RelatorioMigracao(
            matricula="20261001",
            nome_aluno="Aluno Teste SISA",
            curriculo_origem="2018.1 - Ciência da Computação",
            curriculo_destino="2026.1 - Engenharia de Computação"
        )
        self.disciplinas_aproveitadas = [
            {"cod_origem": "COMP101", "cod_destino": "ENG101", "nome_destino": "Introdução à Programação", "ch": 60},
            {"cod_origem": "MAT101", "cod_destino": "ENG102", "nome_destino": "Cálculo I", "ch": 90}
        ]
        self.disciplinas_pendentes = [
            {"codigo": "ENG201", "nome": "Circuitos Digitais", "ch": 60},
            {"codigo": "ENG301", "nome": "Sistemas Operacionais II", "ch": 60}
        ]
        self.ch_aproveitada = 150
        self.ch_pendente = 120

    def test_formatacao_texto_relatorio(self):
        texto = self.relatorio.formatar_relatorio_txt(
            self.disciplinas_aproveitadas,
            self.disciplinas_pendentes,
            self.ch_aproveitada,
            self.ch_pendente
        )
        
        # Valida cabeçalho e informações do aluno
        self.assertIn("20261001", texto)
        self.assertIn("Aluno Teste SISA", texto)
        self.assertIn("2018.1 - Ciência da Computação", texto)
        self.assertIn("2026.1 - Engenharia de Computação", texto)

        # Valida seção de equivalências e aproveitamentos
        self.assertIn("COMP101 -> ENG101", texto)
        self.assertIn("Introdução à Programação", texto)
        self.assertIn("Total de Carga Horária Aproveitada: 150h", texto)

        # Valida disciplinas pendentes
        self.assertIn("ENG201", texto)
        self.assertIn("Circuitos Digitais", texto)
        self.assertIn("Total de Carga Horária Pendente: 120h", texto)

    def test_exportacao_arquivo_local_txt(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp:
            caminho_saida = temp.name

        try:
            caminho_gerado = self.relatorio.exportar_txt(
                caminho_saida,
                self.disciplinas_aproveitadas,
                self.disciplinas_pendentes,
                self.ch_aproveitada,
                self.ch_pendente
            )

            # Verifica se o arquivo foi criado no sistema de arquivos
            self.assertTrue(os.path.exists(caminho_gerado))

            # Lê o arquivo e confirma o conteúdo
            with open(caminho_gerado, 'r', encoding='utf-8') as f:
                conteudo = f.read()

            self.assertIn("SISA - RELATÓRIO DE SIMULAÇÃO DE MIGRAÇÃO", conteudo)
            self.assertIn("Total de Carga Horária Pendente: 120h", conteudo)

        finally:
            if os.path.exists(caminho_saida):
                os.unlink(caminho_saida)

if __name__ == '__main__':
    unittest.main()
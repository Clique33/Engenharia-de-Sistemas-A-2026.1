import unittest


class Disciplina:

    def __init__(
        self,
        codigo: str,
        nome: str,
        carga_horaria: int,
        periodo_recomendado: int,
        pre_requisitos: list = None,
    ):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.periodo_recomendado = periodo_recomendado
        self.pre_requisitos = pre_requisitos
        if pre_requisitos is None:
            self.pre_requisitos = []

    def obter_informações(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "carga_horaria": self.carga_horaria,
            "periodo": self.periodo_recomendado,
            "pre_requisitos": self.pre_requisitos,
        }

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.carga_horaria}h)"

    def adicionar_pre_requisito(self, disciplina_codigo: str):
        """Adiciona o código de uma disciplina pré-requisito."""
        if disciplina_codigo not in self.pre_requisitos:
            self.pre_requisitos.append(disciplina_codigo)

    def tem_pre_requisitos(self) -> bool:
        """Verifica se a disciplina possui pré-requisitos."""
        return len(self.pre_requisitos) > 0

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.carga_horaria}h)"


class Curriculo:

    def __init__(self, nome: str, versao: str):
        self.nome = nome
        self.versao = versao
        self.disciplinas = {}

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.disciplinas[disciplina.codigo] = disciplina

    def obter_disciplina(self, codigo: str) -> Disciplina:
        return self.disciplinas.get(codigo)

    def total_disciplinas(self) -> int:
        return len(self.disciplinas)


class GerenciadorCurriculos:

    def __init__(self):
        self.curriculos = {}

    def cadastrar_curriculo(self, curriculo: Curriculo):
        chave = f"{curriculo.nome}_{curriculo.versao}"
        self.curriculos[chave] = curriculo

    def carregar_curriculo(self, nome: str, versao: str) -> Curriculo:
        chave = f"{nome}_{versao}"
        return self.curriculos.get(chave)


def carregar_novo_curriculo_engenharia_computacao() -> Curriculo:
    curriculo = Curriculo(
        nome="Engenharia de Computação", versao="V1_2025"
    )

    # Ordem dos parâmetros: (codigo, nome, carga_horaria, periodo_recomendado, pre_requisitos)
    disciplinas_dados = [
        # 1º Período
        ("IME 01-17352", "Cálculo Dif. e Int. I", 90, 1, []),
        ("IME 02-xxxxx", "Álgebra Linear", 90, 1, []),
        ("FIS 01-xxxx1", "Física Teórica I", 60, 1, []),
        ("FIS 01-xxxx2", "Física Experimental I", 30, 1, []),
        ("FEN 06-xxxx1", "Algoritmos Computacionais I", 60, 1, []),
        ("FEN 06-xxxx2", "Fundamentos de Comput. I", 60, 1, []),
        # 2º Período
        (
            "IME 01-17356",
            "Cálculo Dif. e Int. II",
            60,
            2,
            ["IME 01-17352"],
        ),
        ("FIS 02-xxxx1", "Física Teórica II", 60, 2, ["FIS 01-xxxx1"]),
        ("FIS 02-xxxx2", "Física Experimental II", 30, 2, ["FIS 01-xxxx2"]),
        (
            "FEN 06-xxxx3",
            "Estruturas de Informação A",
            75,
            2,
            ["FEN 06-xxxx1"],
        ),
        (
            "FEN 06-xxxx4",
            "Análise de Algoritmos I",
            60,
            2,
            ["FEN 06-xxxx1"],
        ),
        # 3º Período
        (
            "IME 01-17363",
            "Cálculo Dif. e Int. III",
            60,
            3,
            ["IME 01-17356"],
        ),
        ("FIS 03-xxxxx1", "Eletromag. Bás. Teór.", 60, 3, ["FIS 02-xxxx1"]),
        ("FIS 03-xxxxx2", "Eletromag. Bás. Exp.", 30, 3, ["FIS 02-xxxx2"]),
        ("FEN 04-xxxx1", "Circuitos em Corrente Contínua", 75, 3, []),
        (
            "FEN 06-xxxx5",
            "Teoria dos Grafos e Aplicações",
            60,
            3,
            ["FEN 06-xxxx3"],
        ),
        ("FEN 06-xxxx6", "Lab. de Programação", 60, 3, ["FEN 06-xxxx1"]),
        # 4º Período
        ("IME 06-xxxx", "Cálculo Numérico", 60, 4, ["IME 01-17356"]),
        ("FIS 04-xxxx", "Física Teórica IV", 60, 4, ["FIS 03-xxxxx1"]),
        ("FIS 03-xxxxx3", "Física Experimental IV", 30, 4, ["FIS 03-xxxxx2"]),
        (
            "FEN 04-xxxx2",
            "Circuitos em Corrente Alternada",
            75,
            4,
            ["FEN 04-xxxx1"],
        ),
        (
            "FEN 05-xxxx1",
            "Materiais Elétricos e Eletrônicos",
            60,
            4,
            [],
        ),
        ("FEN 06-xxxx7", "Laboratório de POO", 60, 4, ["FEN 06-xxxx6"]),
        # 5º Período
        ("IME 05-xxxxx", "Probabilidade e Estatística", 60, 5, []),
        ("FEN 05-xxxx2", "Técnicas Digitais", 90, 5, []),
        ("FEN 06-xxxx8", "Arquitetura de Comp. A", 75, 5, ["FEN 05-xxxx2"]),
        ("FEN 06-xxxx9", "Inteligência Comp. I", 60, 5, []),
        ("FEN 06-xxxx10", "Lógica em Programação", 60, 5, []),
        # 6º Período
        (
            "FEN 05-xxxx3",
            "Circuitos Eletrônicos I",
            90,
            6,
            ["FEN 04-xxxx2"],
        ),
        (
            "FEN 06-xxxx11",
            "Controle de Processos por Comp. I",
            75,
            6,
            [],
        ),
        (
            "FEN 06-xxxx12",
            "Computação, Ética e Transformação Digital",
            30,
            6,
            [],
        ),
        (
            "FEN 06-xxxx13",
            "Inteligência Comp. II",
            60,
            6,
            ["FEN 06-xxxx9"],
        ),
        ("FEN 06-xxxx14", "Mineração de Dados", 60, 6, []),
        # 7º Período
        ("FEN 09-xxxxx1", "Administração Financeira de Projeto", 60, 7, []),
        ("FEN 06-xxxx15", "Engenharia de Sistemas", 60, 7, []),
        (
            "FEN 06-xxxx16",
            "Instalação de Ambientes Comp.",
            45,
            7,
            [],
        ),
        (
            "FEN 06-xxxx17",
            "Processamento de Sinais e Imagens",
            75,
            7,
            [],
        ),
        (
            "FEN 06-xxxxx2",
            "Metod. Cient. p/ Eng. Computação",
            30,
            7,
            [],
        ),
        ("FEN 06-xxxx18", "Segurança de Redes", 60, 7, []),
        # 8º Período
        ("FEN 09-xxxxx2", "Empreendedorismo na Engenharia", 45, 8, []),
        ("FEN 06-xxxx19", "Análise e Projeto de Sistemas", 60, 8, []),
        (
            "FEN 06-xxxx20",
            "Computação Paralela e Distribuída",
            60,
            8,
            [],
        ),
        ("FEN 06-xxxx21", "Projeto de S.O.", 60, 8, []),
        ("FEN 06-xxxx22", "Sistemas Embutidos", 60, 8, []),
        # 9º Período
        ("FEN 09-xxxx3", "Macroeconomia aplicada à Eng.", 60, 9, []),
        ("FEN 06-xxxx23", "Projeto de Banco de Dados", 60, 9, []),
        ("FEN 06-xxxxx3", "Projeto de Grad. XI", 30, 9, []),
        (
            "FEN 06-xxxx24",
            "Redes de Comput. e Sist. Dist.",
            60,
            9,
            [],
        ),
        ("FEN 06-xxxx25", "Eletiva Restrita 1", 60, 9, []),
        # 10º Período
        (
            "FEN 06-xxxx26",
            "Estágio Sup. para Eng. de Computação",
            165,
            10,
            [],
        ),
        ("FEN 06-xxxx27", "Teoria de Compiladores I", 75, 10, []),
        ("FEN 06-xxxx28", "Projetos de Extensão", 30, 10, []),
        ("FEN 06-xxxx29", "Eletiva Restrita 2", 60, 10, []),
    ]

    for codigo, nome, ch, periodo, req in disciplinas_dados:
        disciplina = Disciplina(codigo, nome, ch, periodo, req)
        curriculo.adicionar_disciplina(disciplina)

    return curriculo


def carregar_curriculo_atual_exemplo() -> Curriculo:
    curriculo = Curriculo(
        nome="Engenharia de Computação", versao="V0_Antiga"
    )
    curriculo.adicionar_disciplina(
        Disciplina("IME 01-10000", "Cálculo I Antigo", 90, 1)
    )
    return curriculo


class TestCarregamentoCurriculos(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciadorCurriculos()
        self.curriculo_atual = carregar_curriculo_atual_exemplo()
        self.novo_curriculo = carregar_novo_curriculo_engenharia_computacao()

        self.gerenciador.cadastrar_curriculo(self.curriculo_atual)
        self.gerenciador.cadastrar_curriculo(self.novo_curriculo)

    def test_carregamento_independente_simultaneo(self):
        v_atual = self.gerenciador.carregar_curriculo(
            "Engenharia de Computação", "V0_Antiga"
        )
        v_nova = self.gerenciador.carregar_curriculo(
            "Engenharia de Computação", "V1_2025"
        )

        self.assertIsNotNone(v_atual)
        self.assertIsNotNone(v_nova)
        self.assertNotEqual(v_atual.versao, v_nova.versao)

    def test_integridade_disciplinas_novo_curriculo(self):
        v_nova = self.gerenciador.carregar_curriculo(
            "Engenharia de Computação", "V1_2025"
        )
        self.assertGreaterEqual(len(v_nova.disciplinas), 50)

        calc1 = v_nova.obter_disciplina("IME 01-17352")
        self.assertIsNotNone(calc1)
        self.assertEqual(calc1.nome, "Cálculo Dif. e Int. I")
        self.assertEqual(calc1.periodo_recomendado, 1)
        self.assertEqual(calc1.carga_horaria, 90)

    def test_pre_requisitos(self):
        v_nova = self.gerenciador.carregar_curriculo(
            "Engenharia de Computação", "V1_2025"
        )
        calc2 = v_nova.obter_disciplina("IME 01-17356")
        self.assertIn("IME 01-17352", calc2.pre_requisitos)


if __name__ == "__main__":
    unittest.main()
import json
import os

class DisciplinaHistorico:
    """Estrutura que armazena as informações de uma disciplina cursada ou em curso pelo aluno."""
    def __init__(self, codigo: str, nome: str = "", situacao: str = "", periodo: str = "", media: float = None):
        self.codigo = codigo
        self.nome = nome
        self.situacao = situacao
        self.periodo = periodo
        self.media = media

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "situacao": self.situacao,
            "periodo": self.periodo,
            "media": self.media
        }

class LeitorHistorico:
    """Responsável por ler e processar o arquivo de histórico escolar do aluno."""
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def carregar_historico(self) -> dict:
        """Abre e lê o arquivo JSON, tratando exceções de arquivo inexistente ou JSON inválido."""
        if not os.path.exists(self.caminho_arquivo):
            raise FileNotFoundError(f"O arquivo de histórico '{self.caminho_arquivo}' não foi encontrado.")
        
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"O arquivo '{self.caminho_arquivo}' possui um formato JSON inválido: {e}")
        except Exception as e:
            raise RuntimeError(f"Erro inesperado ao ler o arquivo de histórico: {e}")

        return dados

    def obter_disciplinas(self) -> list:
        """Identifica e retorna uma lista de objetos DisciplinaHistorico extraídos do histórico."""
        dados = self.carregar_historico()
        
        # Suporta tanto dicionários com chave de histórico quanto listas diretas
        lista_bruta = []
        if isinstance(dados, dict):
            lista_bruta = dados.get("historico", dados.get("disciplinas", []))
        elif isinstance(dados, list):
            lista_bruta = dados

        disciplinas = []
        for item in lista_bruta:
            codigo = item.get("codigo") or item.get("code")
            if not codigo:
                continue  # Ignora registros sem código válido
            
            nome = item.get("nome", item.get("name", ""))
            situacao = item.get("situacao", item.get("status", ""))
            periodo = item.get("periodo", item.get("term", ""))
            media = item.get("media", item.get("grade", None))

            disciplinas.append(DisciplinaHistorico(
                codigo=codigo,
                nome=nome,
                situacao=situacao,
                periodo=periodo,
                media=media
            ))

        return disciplinas
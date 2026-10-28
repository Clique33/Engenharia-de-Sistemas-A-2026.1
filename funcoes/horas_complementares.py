from enum import Enum
import json
import os

class TipoAtividade(Enum):
    """Tipos de atividades que integram a carga de horas complementares."""
    CARGA_EXTENSAO = "Carga de Extensão"
    ATIVIDADE_COMPLEMENTAR = "Atividade Complementar"
    ATIVIDADE_CURRICULAR_EXTENSAO = "Atividade Curricular de Extensão"


class AtividadeComplementar:
    """Representa uma atividade complementar registrada."""

    def __init__(self, nome: str, horas: int, tipo: TipoAtividade):
        self.nome = nome
        self.horas = horas
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo.value}: {self.nome} ({self.horas}h)"



class HorasComplementares:
    """Gerencia e persiste as horas complementares divididas em:
    - Carga de Extensão
    - Atividade Complementar
    - Atividade Curricular de Extensão
    """
    def __init__(self):
        self.carga_extensao = []
        self.atividade_complementar = []
        self.atividade_curricular_extensao = []

    def adicionar_carga_extensao(self, descricao: str, horas: int):
        self.carga_extensao.append({"descricao": descricao, "horas": horas})

    def adicionar_atividade_complementar(self, descricao: str, horas: int, categoria: str = ""):
        self.atividade_complementar.append({"descricao": descricao, "horas": horas, "categoria": categoria})

    def adicionar_atividade_curricular_extensao(self, codigo: str, nome: str, horas: int):
        self.atividade_curricular_extensao.append({"codigo": codigo, "nome": nome, "horas": horas})

    def total_horas(self) -> int:
        """Calcula o total de horas acumuladas em todas as categorias."""
        return (
            sum(item.get("horas", 0) for item in self.carga_extensao) +
            sum(item.get("horas", 0) for item in self.atividade_complementar) +
            sum(item.get("horas", 0) for item in self.atividade_curricular_extensao)
        )

    def to_dict(self) -> dict:
        """Converte a estrutura interna para dicionário."""
        return {
            "carga_extensao": self.carga_extensao,
            "atividade_complementar": self.atividade_complementar,
            "atividade_curricular_extensao": self.atividade_curricular_extensao
        }

    def salvar_json(self, caminho_arquivo: str):
        """Salva todas as horas complementares cadastradas em um arquivo JSON."""
        dados = self.to_dict()
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError(f"Erro ao salvar o arquivo de horas complementares: {e}")

    @classmethod
    def carregar_json(cls, caminho_arquivo: str) -> "HorasComplementares":
        """Carrega os dados de um arquivo JSON e retorna uma nova instância de HorasComplementares."""
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"O arquivo '{caminho_arquivo}' possui um formato JSON inválido: {e}")
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o arquivo de horas complementares: {e}")

        instancia = cls()
        instancia.carga_extensao = dados.get("carga_extensao", [])
        instancia.atividade_complementar = dados.get("atividade_complementar", [])
        instancia.atividade_curricular_extensao = dados.get("atividade_curricular_extensao", [])
        return instancia
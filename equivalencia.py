class EquivalenciasCurriculares:

    def __init__(self):
        self._mapa = {}
        
    def cadastrar(self, codigo_antigo, codigo_novo):
        self._mapa[codigo_antigo] = codigo_novo

    def consultar(self, codigo_antigo):
        return self._mapa.get(codigo_antigo)
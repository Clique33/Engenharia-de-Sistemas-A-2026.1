class HorasComplementares:
    def __init__(self, meta_horas):
        self.meta_horas = meta_horas
        self.atividades = []

    def registrar_atividade(self, nome_atividade, horas):
        if horas <= 0:
            return False
        self.atividades.append({"atividade": nome_atividade, "horas": horas})
        return True

    def calcular_total(self):
        return sum(item["horas"] for item in self.atividades)

    def meta_atingida(self):
        return self.calcular_total() >= self.meta_horas

    def horas_faltantes(self):
        faltam = self.meta_horas - self.calcular_total()
        return faltam if faltam > 0 else 0
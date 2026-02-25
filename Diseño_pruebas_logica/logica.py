# Archivo: core/ahorro.py

class AhorroProgramado:
    def __init__(self, meta, plazo, extra=0, mes_extra=0):
        self.meta = meta
        self.plazo = plazo
        self.extra = extra
        self.mes_extra = mes_extra

    def calcular_ahorro(self):
        # 1. Validaciones (Estas lanzan el ValueError que esperan los tests)
        if self.meta <= 0:
            raise ValueError("El valor de la meta debe ser mayor a 0")
        if self.plazo <= 0:
            raise ValueError("El plazo debe ser mayor a 0")
        if self.extra > self.meta:
            raise ValueError("El abono extra no puede superar la meta")
        if self.mes_extra > self.plazo:
            raise ValueError("El mes del abono no puede superar el plazo")

        # 2. Lógica de cálculo (División simple según acordamos en el Excel)
        meta_restante = self.meta - self.extra
        
        if meta_restante <= 0:
            return 0.0
            
        cuota = meta_restante / self.plazo
        return round(cuota, 2)
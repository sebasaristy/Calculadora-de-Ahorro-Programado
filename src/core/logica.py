class ErrorMetaMayorACero(Exception):
    """La meta debe ser mayor que 0"""
    pass

class ErrorPlazoMayorACero(Exception):
    """El plazo debe ser mayor que 0"""
    pass

class ErrorAbonoExtraMenorACero(Exception):
    """El abono extra no puede ser menor que 0"""
    pass

class ErrorAbonoSuperaMeta(Exception):
    """El abono extra no puede superar la meta"""
    pass

class ErrorMesExtraFueraDelRango(Exception):
    """El mes del abono no puede superar el plazo"""
    pass

class AhorroProgramado:
    def __init__(self, meta, plazo, extra = 0, mes_extra = 0):
        self.meta = meta
        self.plazo = plazo
        self.abono_extra = extra
        self.mes_abono_extra = mes_extra
        self.tasa_interes = 0.0075

    def calcular_ahorro(self):
        # Validaciones de integridad de datos
        if self.meta <= 0:
            raise ErrorMetaMayorACero()

        if self.plazo <= 0:
            raise ErrorPlazoMayorACero()

        if self.abono_extra < 0:
            raise ErrorAbonoExtraMenorACero()

        if self.abono_extra > self.meta:
            raise ErrorAbonoSuperaMeta()

        if self.mes_abono_extra > self.plazo:
            raise ErrorMesExtraFueraDelRango()

       
        interes = self.tasa_interes
        total_periodos = self.plazo
        momento_abono_extra = self.mes_abono_extra

        if momento_abono_extra > 0:
            periodos_restantes = total_periodos - momento_abono_extra
            valor_futuro_abono_extra = self.abono_extra * ((1 + interes) ** periodos_restantes)
        else:
            valor_futuro_abono_extra = 0

        factor_acumulacion = ((1 + interes) ** total_periodos - 1) / interes
        cuota_mensual = (self.meta - valor_futuro_abono_extra) / factor_acumulacion

        return round(cuota_mensual, 2)
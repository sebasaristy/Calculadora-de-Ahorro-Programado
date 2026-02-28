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
    def __init__(self, meta, plazo, extra=0, mes_extra=0):
        self.meta = meta
        self.plazo = plazo
        self.extra = extra
        self.mes_extra = mes_extra
        self.tasa = 0.0075

    def calcular_ahorro(self):
        # Validaciones
        if self.meta <= 0:
            raise ErrorMetaMayorACero()

        if self.plazo <= 0:
            raise ErrorPlazoMayorACero()

        if self.extra < 0:
            raise ErrorAbonoExtraMenorACero()

        if self.extra > self.meta:
            raise ErrorAbonoSuperaMeta()

        if self.mes_extra > self.plazo:
            raise ErrorMesExtraFueraDelRango()

        # Cálculo
        i = self.tasa
        n = self.plazo
        k = self.mes_extra

        fv_extra = self.extra * ((1 + i) ** (n - k)) if k > 0 else 0
        factor = ((1 + i) ** n - 1) / i
        cuota = (self.meta - fv_extra) / factor

        return round(cuota, 2)



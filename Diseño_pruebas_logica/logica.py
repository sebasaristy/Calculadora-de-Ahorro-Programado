class ErrorMetaMayorACero(Exception):

       # Se usa cuando la meta del ahorro es menor o igual que 0
     
    pass
class ErrorPlazoMayorACero(Exception):
    
       # Se usa cuando el plazo del ahorro es igual o menor que 0 
    
    pass
class ErrorAbonoSuperaMeta(Exception): 
  
       # Se usa cuando el abono extra supera la meta de ahorro
  
    pass

class ErrorMesExtraFueraDelRango(Exception): 
    
       # Se usa cuando el mes donde se hace el abono extra es mayor que la meta del ahorro programado
    
    pass

class ErrorAbonoExtraMenorAcero(Exception):
    
    
       # Se usa cuando el abono extra es menor que 0
    pass

class AhorroProgramado:
    def __init__(self, meta, plazo, extra=0, mes_extra=0):
        self.meta = meta
        self.plazo = plazo 
        self.extra = extra
        self.mes_extra = mes_extra

    def calcular_ahorro(self):
        # 1. Validaciones 
        if self.meta <= 0:
            raise ErrorMetaMayorACero("La meta debe ser mayor a 0")

        if self.plazo <= 0:
            raise ErrorPlazoMayorACero("El plazo debe ser mayor a 0")

        if self.extra < 0:
            raise ErrorAbonoExtraMenorACero("El abono extra no puede ser menor a 0")

        if self.extra > self.meta:
            raise ErrorAbonoSuperaMeta("El abono extra no puede superar la meta")

        if self.mes_extra > self.plazo:
            raise ErrorMesExtraFueraDelRango("El mes del abono no puede superar el plazo")

        # 2. Lógica de cálculo
        i = self.tasa
        n = self.plazo
        k = self.mes_extra

        if k > 0:
            fv_extra = self.extra * (1 + i)**(n - k)
        else:
            fv_extra = 0
    
        factor = ((1 + i)**n - 1) / i

        cuota = (self.meta - fv_extra) / factor

        return round(cuota, 2)
    
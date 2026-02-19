def calcular_cuota_ahorro(meta, plazo_meses, tasa_mensual, abono_extra=0, mes_abono=0):
    """
    Calcula la cuota mensual para llegar a una meta de ahorro,
    considerando intereses compuestos y un abono extra inteligente.
    """
    
    if meta <= 0 or plazo_meses <= 0:
        return "Error: La meta y el plazo deben ser mayores a 0"
    
    if mes_abono > plazo_meses:
        return "Error: El mes del abono no puede ser mayor al plazo total"

    
    meses_rendimiento = max(0, plazo_meses - mes_abono)
    valor_futuro_abono = abono_extra * ((1 + tasa_mensual) ** meses_rendimiento)
    

    meta_restante = meta - valor_futuro_abono
    
    
    if meta_restante <= 0:
        return 0.0
    
   
    cuota = (meta_restante * tasa_mensual) / (((1 + tasa_mensual) ** plazo_meses) - 1)
    
    return round(cuota, 2)
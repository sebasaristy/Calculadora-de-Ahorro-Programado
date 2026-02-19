import unittest

from logica import calcular_cuota_ahorro

class TestCalculadoraAhorro(unittest.TestCase):

    def test_caso_1_ahorro_estandar(self):
        """
        Caso 1: Ahorro Normal
        Meta: 1.2M, 12 meses, 1% tasa.
        Resultado esperado: $94,618.55
        """
        resultado = calcular_cuota_ahorro(meta=1200000, plazo_meses=12, tasa_mensual=0.01)
        self.assertAlmostEqual(resultado, 94618.55, delta=1.0)

    def test_caso_2_empujon_abono(self):
        """
        Caso 2: Ahorro con Abono a Mitad de Camino
        Meta: 5M, 24 meses, 1.5% tasa. Abono de 1M en el mes 12.
        Resultado esperado: $132,864.62
        """
        resultado = calcular_cuota_ahorro(
            meta=5000000, 
            plazo_meses=24, 
            tasa_mensual=0.015, 
            abono_extra=1000000, 
            mes_abono=12
        )
        self.assertAlmostEqual(resultado, 132864.62, delta=1.0)

    def test_caso_3_micro_ahorro(self):
        """
        Caso 3: Micro Ahorro Corto Plazo
        Meta: 500k, 6 meses, 2% tasa.
        Resultado esperado: $79,262.91
        """
        resultado = calcular_cuota_ahorro(meta=500000, plazo_meses=6, tasa_mensual=0.02)
        self.assertAlmostEqual(resultado, 79262.91, delta=1.0)

    def test_error_mes_abono_invalido(self):
        """Prueba de Error: Mes de Abono > Plazo"""
        resultado = calcular_cuota_ahorro(
            meta=1000000, 
            plazo_meses=12, 
            tasa_mensual=0.01, 
            abono_extra=500000, 
            mes_abono=15
        )
        self.assertEqual(resultado, "Error: El mes del abono no puede ser mayor al plazo total")

    def test_error_valores_negativos(self):
        """Prueba de Error: Meta Negativa"""
        resultado = calcular_cuota_ahorro(meta=-500000, plazo_meses=12, tasa_mensual=0.01)
        self.assertEqual(resultado, "Error: La meta y el plazo deben ser mayores a 0")

if __name__ == '__main__':
    print("Iniciando pruebas unitarias...")
    unittest.main()
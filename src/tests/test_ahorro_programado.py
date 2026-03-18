import unittest
import sys
from pathlib import Path

# Permite importar desde la raíz del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.logica import (
    AhorroProgramado,
    ErrorMetaMayorACero,
    ErrorPlazoMayorACero,
    ErrorAbonoExtraMenorACero,
    ErrorAbonoSuperaMeta,
    ErrorMesExtraFueraDelRango
)

class TestAhorroProgramado(unittest.TestCase):

    # CASOS NORMALES
    def test_caso_normal_uno(self):
        """Ahorro estándar a 12 meses sin abonos"""
        ahorro = AhorroProgramado(meta=1200000, plazo=12, extra=0, mes_extra=0)
        # Usamos assertAlmostEqual con places=2 (2 decimales)
        self.assertAlmostEqual(ahorro.calcular_ahorro(),95941.77, places=2)

    def test_caso_normal_dos(self):
        """Meta grande a largo plazo"""
        ahorro = AhorroProgramado(meta=5000000, plazo=20, extra=0, mes_extra=0)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), 232653.16, places=2)

    def test_caso_normal_tres(self):
        """Meta corta a corto plazo"""
        ahorro = AhorroProgramado(meta=450000, plazo=3, extra=0, mes_extra=0)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), 148880.60, places=2)

    # CASOS EXTRAORDINARIOS
    
    def test_abono_parcial(self):
        """Abono de 1M en el mes 5 para una meta de 2M a 10 meses"""
        ahorro = AhorroProgramado(meta=2000000, plazo=10, extra=1000000, mes_extra=5)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), 92593.63, places=2)

    def test_abono_total(self):
        """Abono que cubre el 100% de la meta en el mes 12"""
        ahorro = AhorroProgramado(meta=8000000, plazo=24, extra=8000000, mes_extra=12)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), 0.00, places=2)

    def test_micro_ahorro(self):
        """Ahorro muy pequeño sin abonos"""
        ahorro = AhorroProgramado(meta=60000, plazo=2, extra=0, mes_extra=0)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), 29887.78, places=2)

    # CASOS DE ERROR (Validaciones)
    
    def test_meta_menor_a_cero(self):
        """Validar que rechace metas negativas"""
        with self.assertRaises(ErrorMetaMayorACero):
            ahorro = AhorroProgramado(meta=-500000, plazo=12, extra=0, mes_extra=0)
            ahorro.calcular_ahorro()

    def test_meta_cero(self):
        """Validar que rechace metas de $0"""
        with self.assertRaises(ErrorMetaMayorACero):
            ahorro = AhorroProgramado(meta=0, plazo=6, extra=0, mes_extra=0)
            ahorro.calcular_ahorro()

    def test_plazo_cero(self):
        """Validar que no se pueda calcular sin meses de plazo"""
        with self.assertRaises(ErrorPlazoMayorACero):
            ahorro = AhorroProgramado(meta=1000000, plazo=0, extra=0, mes_extra=0)
            ahorro.calcular_ahorro()

    def test_abono_supera_meta(self):
        """Validar que el abono no pueda ser mayor que lo que se quiere ahorrar"""
        with self.assertRaises(ErrorAbonoSuperaMeta):
            ahorro = AhorroProgramado(meta=1500000, plazo=12, extra=2000000, mes_extra=6)
            ahorro.calcular_ahorro()

    def test_mes_extra_fuera_de_rango(self):
        """Validar que no se pueda hacer un abono en un mes que no existe en el plazo"""
        with self.assertRaises(ErrorMesExtraFueraDelRango):
            ahorro = AhorroProgramado(meta=1000000, plazo=12, extra=500000, mes_extra=15)
            ahorro.calcular_ahorro()

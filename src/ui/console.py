from src.core.logica import (
    AhorroProgramado,
    ErrorMetaMayorACero,
    ErrorPlazoMayorACero,
    ErrorAbonoExtraMenorACero,
    ErrorAbonoSuperaMeta,
    ErrorMesExtraFueraDelRango
)


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número entero.")


def main():
    print("===================================")
    print("   CALCULADORA DE AHORRO PROGRAMADO ")
    print("===================================\n")

    try:
        meta = pedir_entero("Ingrese la meta de ahorro ($): ")
        plazo = pedir_entero("Ingrese el plazo en meses: ")
        extra = pedir_entero("Ingrese el abono extra (0 si no hay): ")
        mes_extra = pedir_entero("Ingrese el mes del abono extra (0 si no hay): ")

        ahorro = AhorroProgramado(
            meta=meta,
            plazo=plazo,
            extra=extra,
            mes_extra=mes_extra
        )

        cuota = ahorro.calcular_ahorro()

        print("\n✅ Cálculo exitoso")
        print(f"Debes ahorrar mensualmente: ${cuota:,.2f}")

    except ErrorMetaMayorACero:
        print("❌ Error: la meta debe ser mayor que 0.")

    except ErrorPlazoMayorACero:
        print("❌ Error: el plazo debe ser mayor que 0.")

    except ErrorAbonoExtraMenorACero:
        print("❌ Error: el abono extra no puede ser negativo.")

    except ErrorAbonoSuperaMeta:
        print("❌ Error: el abono extra no puede superar la meta.")

    except ErrorMesExtraFueraDelRango:
        print("❌ Error: el mes del abono está fuera del plazo.")

    except Exception as e:
        print("❌ Error inesperado:", e)


if __name__ == "__main__":
    main()
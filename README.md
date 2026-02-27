# 💻 Simulador de Ahorro Programado

# grupo comformado por jose angel sanchez y miguel angel salazar
Herramienta financiera construida para la asignatura **lenguajes de programacion y codigo limpio**. Este sistema está diseñado aplicando **Clean Code**, manejo preventivo de errores y un entorno riguroso de pruebas unitarias automatizadas.

Su función principal es calcular la cuota mensual requerida para cumplir un objetivo de ahorro en un tiempo definido, tomando en cuenta el rendimiento de una tasa de interés mensual y el impacto de inyecciones de capital (abonos extra) en fechas específicas.

---

## 🚀 Propósito del Proyecto

El objetivo central es automatizar el cálculo de la **cuota mensual fija** que un usuario debe depositar para alcanzar una meta económica. Para esto, el algoritmo se apoya en el modelo matemático de **anualidades de valor futuro con interés compuesto**, evaluando cómo un aporte extraordinario disminuye la carga mensual del ahorrador.

---

## 📊 Bases Matemáticas y Fórmulas

El motor de cálculo financiero del programa se rige por las siguientes premisas:

- 📌 **Tasa de rendimiento mensual:** Fijada en `0.75%` (0.0075) para las proyecciones.
- 📌 **Proyección del capital extra:** Todo abono extraordinario genera rendimientos desde el mes en que se deposita (`k`) hasta el vencimiento del plan.

\[
![Fórmula Valor Futuro](assets/images//fvextra.svg)
\]

- 📌 **Crecimiento de las cuotas (Anualidad):** Calcula cómo el dinero aportado mes a mes va sumando valor con los intereses.

\[
![Fórmula Valor Futuro](assets/images//formula2.svg)
\]

- 📌 **Cálculo de la cuota final:** Al total de la meta se le descuenta el valor futuro generado por el abono extra. La diferencia restante se divide por el factor de anualidad para hallar el pago mensual exacto.

\[
![Fórmula Valor Futuro](assets/images//cuotamensual.svg)
\]

Todos los valores monetarios de salida se redondean a **2 decimales** para garantizar precisión contable.

---

## 📥 Parámetros de Entrada

Para operar, la herramienta requiere que se definan cuatro variables clave (ya sea por consola o mediante la instanciación de la clase):

| Variable | Tipo de Dato | Definición |
|----------|--------|--------------|
| `meta` | `float` | Capital final que el usuario desea acumular. |
| `plazo` | `int` | Cantidad total de meses contemplados para el ahorro. |
| `extra` | `float` | Inyección de capital adicional (indicar `0` si no se hará ningún abono extra). |
| `mes_extra` | `int` | Mes exacto durante el cual se efectuará el depósito adicional. |

---

## 🛡️ Reglas de Negocio y Validaciones

Para asegurar la integridad matemática del sistema, se configuraron restricciones estrictas. El programa evalúa que:

- El capital a ahorrar (meta) sea estrictamente positivo.
- El horizonte de tiempo (plazo) sea mayor a cero meses.
- El monto del aporte extra nunca sea un número negativo.
- La inyección extra de capital no sea mayor que la meta misma.
- La fecha del abono (mes extra) ocurra dentro de la vigencia del plan de ahorro.

El incumplimiento de cualquiera de estas reglas interrumpe el proceso y dispara **excepciones personalizadas**.

---

## 🔄 Flujo de Ejecución

1. Recepción de los parámetros de configuración del ahorro.
2. Filtro de seguridad (evaluación de las reglas de negocio).
3. Determinación de los intereses ganados por el abono extraordinario.
4. Estimación del factor matemático de la anualidad.
5. Determinación de la cuota mensual requerida para cubrir la diferencia.
6. Retorno del valor a pagar o impresión del respectivo código de error.

---

## 🖥️ Resultados Esperados

### ✅ Escenario de Éxito
Si los parámetros cumplen todas las reglas, el sistema arroja la proyección financiera de manera limpia:

```text
📈 SIMULADOR DE AHORRO PROGRAMADO

> Indique su meta de ahorro: 1100000
> Indique el plazo (meses): 6
> Ingrese un abono extraordinario (0 si no aplica): 0

✅ PROYECCIÓN CALCULADA
Cuota mensual sugerida: $179,925.80

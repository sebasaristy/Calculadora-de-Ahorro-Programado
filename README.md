# 💻 Simulador de Ahorro Programado

# grupo conformado por jose angel sanchez y miguel angel salazar
Herramienta financiera construida para la asignatura **lenguajes de programacion y codigo limpio**. Este sistema está diseñado aplicando **pruebas unitarias y una pequeña logica con retorno en la consola**, manejo preventivo de errores y un entorno riguroso de pruebas unitarias automatizadas.

Su función principal es calcular la cuota mensual requerida para cumplir un objetivo de ahorro en un tiempo definido, tomando en cuenta el rendimiento de una tasa de interés mensual y el impacto de inyecciones de capital (abonos extra) en fechas específicas.

---

## 🚀 Propósito del Proyecto

El objetivo central es automatizar el cálculo de la **cuota mensual fija** que un usuario debe depositar para alcanzar una meta económica. Para esto, el algoritmo se apoya en el modelo matemático de **anualidades de valor futuro con interés compuesto**, evaluando cómo un aporte extraordinario disminuye la carga mensual del ahorrador.

---

## 📊 Bases Matemáticas y Fórmulas

El motor de cálculo financiero del programa se rige por las siguientes premisas:

- 📌 **Tasa de rendimiento mensual:** Fijada en `0.75%` (0.0075) para las proyecciones.
- 📌 **Proyección del capital extra:** Todo abono extraordinario genera rendimientos desde el mes en que se deposita (`k`) hasta el vencimiento del plan.
## 📊 Bases Matemáticas y Fórmulas

El motor de cálculo financiero del programa se rige por las siguientes premisas:

- 📌 **Tasa de rendimiento mensual ($i$):** Fijada en `0.75%` (0.0075) para las proyecciones.

- 📌 **Si existe un abono extra, se calcula su valor futuro:** Este aporte ($Extra$) genera rendimientos desde el mes en que se deposita ($k$) hasta el vencimiento del plan ($n$). La fórmula aplicada es:

$$VF_{extra} = Extra \times (1 + i)^{(n - k)}$$

- 📌 **Valor Futuro de Anualidad Ordinaria:** Calcula cómo el dinero aportado mes a mes ($C$) va sumando valor con los intereses para alcanzar una Meta ($VF$). La fórmula general es:

$$VF = C \times \frac{(1 + i)^n - 1}{i}$$

- 📌 **Finalmente, se despeja la cuota mensual ($C$):** Al total de la meta original se le descuenta el valor futuro generado por el abono extra. Sobre ese nuevo total, se despeja $C$ para hallar el pago exacto:

$$C = \frac{(Meta - VF_{extra}) \times i}{(1 + i)^n - 1}$$

Todos los valores monetarios de salida se redondean a **2 decimales** para garantizar precisión contable.
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

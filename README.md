# 📈 Calculadora de Ahorro Programado

Proyecto académico desarrollado bajo principios de código limpio, validaciones robustas, manejo de excepciones y pruebas unitarias para la asignatura lenguajes de programacion y codigo limpio, equipo comformado por miguel angel salazar orrego, jose angel sanchez martinez

Esta aplicación calcula cuánto se debe ahorrar mensualmente para alcanzar una meta financiera en un plazo determinado, considerando una tasa de interés mensual fija y el impacto de un abono extra en un mes específico.

---

## 🎯 Objetivo

Calcular la **cuota mensual de ahorro necesaria** para alcanzar una meta financiera utilizando el modelo de **valor futuro de una anualidad con interés compuesto**, incluyendo la posibilidad de un aporte extraordinario que reduce la carga mensual.

---

## 🧮 Fundamento Matemático

La aplicación utiliza matemática financiera para proyectar el crecimiento del dinero:

- 📌 **Tasa de interés mensual fija:** (Ej. `0.75%` o la parametrizada en el código).
- 📌 **Valor futuro del abono extra:** Si existe un abono en el mes `k`, este genera intereses hasta el final del plazo `n`.
  
  

- 📌 **Fórmula de valor futuro de anualidad ordinaria:** Para calcular cómo las cuotas mensuales construyen el capital restante.
  
  

- 📌 **Despeje de la Cuota Mensual:** Se resta el valor futuro del abono a la meta original, y sobre esa diferencia se calcula la cuota final requerida.
  
  

El resultado final se redondea a **2 decimales** para su representación en moneda.

---

## 📥 Entradas del Sistema

El programa trabaja con los siguientes datos ingresados por el usuario o enviados al constructor de la clase:

| Entrada | Tipo | Descripción |
|----------|--------|--------------|
| `meta` | `float` | Monto total que se desea alcanzar al final del periodo. |
| `plazo` | `int` | Número total de meses para alcanzar la meta. |
| `extra` | `float` | Abono adicional realizado en un mes específico (0 si no aplica). |
| `mes_extra` | `int` | Mes exacto en el que se realiza el abono extra. |

---

## 🔎 Validaciones Implementadas

El sistema está blindado contra datos irreales. Se valida estrictamente que:

- La meta sea mayor que 0.
- El plazo sea mayor que 0.
- El abono extra no sea negativo.
- El abono extra no supere la meta total de ahorro.
- El mes del abono esté dentro del rango lógico (entre 1 y el plazo total).

Si alguna condición falla, el sistema lanza **excepciones personalizadas** (`ValueError`) para detener la ejecución y alertar al usuario.

---

## ⚙️ Proceso de Ejecución

1. El usuario (o el script de pruebas) ingresa los parámetros solicitados.
2. Se ejecutan las validaciones de integridad de datos.
3. Se calcula el valor futuro del abono extra (si existe) basado en el tiempo que permanecerá ganando intereses.
4. Se calcula el factor de anualidad para el plazo establecido.
5. Se despeja la cuota mensual sobre la meta restante.
6. Se retorna el resultado monetario o se captura el mensaje de error correspondiente.

---

## 📤 Salida del Sistema

### ✅ Caso Exitoso
Cuando los datos son válidos, el cálculo es directo y preciso:

```text
📈 CALCULADORA DE AHORRO PROGRAMADO

Ingrese la meta de ahorro: 1100000
Ingrese el plazo en meses: 6
Ingrese el monto extra (0 si no aplica): 0

✅ RESULTADO
Debes ahorrar mensualmente: $179,925.80

# PORTADA
# Nombre: Jesus Benjamin Gonzalez Vallejo
# Matrícula: 2630199
# Grupo: 3
# Materia: Metodologias de la programacion
# Tarea: Tipos numéricos (int, float) y booleanos en Python

"""
RESUMEN EJECUTIVO

En Python, un int es un número entero sin decimales (age, items_count),
mientras que un float es un número con parte decimal (salary, temperature_c).
Los enteros hacen aritmética exacta; los flotantes son aproximaciones, por
eso se redondean al mostrar resultados. Un bool solo tiene dos valores,
True y False, y normalmente se obtiene de una comparación como age >= 18
o de operadores lógicos (and, or, not).
Validar rangos y evitar la división entre cero es importante porque datos
incorrectos (horas negativas, ingreso cero) dan resultados erróneos o hacen
que el programa falle con ZeroDivisionError.
Este documento cubre 6 problemas: convertidor de temperatura, pago de horas
extra, elegibilidad de descuento, estadísticas de tres enteros, elegibilidad
de préstamo e IMC (BMI). Cada uno tiene descripción, entradas, salidas,
validaciones y tres casos de prueba, y usa enteros, flotantes y booleanos para tomar decisiones.
"""

"""
PRINCIPIOS Y BUENAS PRÁCTICAS

Usar el tipo adecuado: int para contadores, float para valores con decimales.
Evitar repetir expresiones complejas: guardar resultados intermedios en
variables (por ejemplo regular_hours y overtime_hours).
Validar los datos antes de operar (horas y salarios no pueden ser negativos).
Usar nombres de variables descriptivos y mensajes claros para el usuario.
Escribir el código directamente (sin funciones def), con input(), if/else
y print(), para que sea más compacto y fácil de seguir de arriba hacia abajo.

"""

"""
Documentar qué significa cada booleano:

is_high_temperature - True si temp_c >= 30.0
has_overtime - True si hours_worked > 40
discount_eligible - True si es estudiante, adulto mayor o compra >= 1000.0
all_even - True si los tres números son pares
eligible - True si ingreso, razón de deuda y score cumplen
is_underweight / is_normal / is_overweight -> banderas de categoría de IMC

"""

import math

# Constantes (UPPER_SNAKE_CASE)
HIGH_TEMPERATURE_LIMIT = 30.0
REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_RATE = 0.10
DISCOUNT_MIN_PURCHASE = 1000.0
MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0

ERROR_MESSAGE = "Error: invalid input"

"""
En cada problema se usa la bandera is_valid (un booleano):

Se lee el dato como texto con input().
Dentro de try se convierte a int/float y se revisan los rangos.
Si la conversión falla (por ejemplo "abc"), except marca is_valid = False.
Si is_valid es True se calcula y se muestra el resultado; si no, el error.
Los booleanos se muestran como "true"/"false" con str(valor).lower().

"""


# Problem 1: Temperature converter and range flag
# Description: Convierte una cierta temperatura de Celsius a Fahrenheit y Kelvin. 
# También crea el booleano is_high_temperature, que es True cuando la temperatura es 30.0 °C o mayor.
# Inputs:
#- temp_c (float): temperatura en grados Celsius.

# Outputs:
#"Fahrenheit:" <temp_f>
#"Kelvin:" <temp_k>
#"High temperature:" true|false

# Validations:
#temp_c debe poder convertirse a float.
#temp_k no debe ser menor que 0.0 (físicamente imposible).

# Test cases:
#1) Normal: temp_c = 25.0 - Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false
#2) Border: temp_c = 30.0 - Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
#3) Error:  temp_c = -300 - Error: invalid input (Kelvin sería -26.85) temp_c = "abc" -> Error: invalid input

print("\nTemperature converter")
temp_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_text)
    # Debe ser un número real y su Kelvin no puede ser negativo
    is_valid = math.isfinite(temp_c) and (temp_c + 273.15) >= 0.0
except ValueError:
    is_valid = False

if is_valid:
    temp_k = temp_c + 273.15
    temp_f = temp_c * 9 / 5 + 32
    is_high_temperature = (temp_c >= HIGH_TEMPERATURE_LIMIT)

    print("Fahrenheit:", round(temp_f, 2))
    print("Kelvin:", round(temp_k, 2))
    print("High temperature:", str(is_high_temperature).lower())
else:
    print(ERROR_MESSAGE)


# Problem 2: Work hours and overtime payment
# Description: Calcula el pago semanal de un trabajador. Hasta 40 horas se
# pagan a hourly_rate. Las horas extra (> 40) se pagan al 150%
#de la tarifa normal. has_overtime indica si hubo horas extra.

# Inputs:
#hours_worked (float): horas trabajadas en la semana.
#hourly_rate (float): pago por hora.

# Outputs:
#"Regular pay:" <regular_pay>
#"Overtime pay:" <overtime_pay>
#"Total pay:" <total_pay>
#"Has overtime:" true|false

# Validations:
#hours_worked >= 0
#hourly_rate > 0
#Si alguno no cumple, mostrar "Error: invalid input".

# Test cases:
#1) Normal: hours = 45, rate = 100 - Regular: 4000.0, Overtime: 750.0, Total: 4750.0, Has overtime: true
#2) Border: hours = 40, rate = 100 - Regular: 4000.0, Overtime: 0.0, Total: 4000.0, Has overtime: false
#3) Error:  hours = -5, rate = 100 - Error: invalid input

print("\nOvertime payment")
hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)
    is_valid = (math.isfinite(hours_worked) and math.isfinite(hourly_rate)
                and hours_worked >= 0 and hourly_rate > 0)
except ValueError:
    is_valid = False

if is_valid:
    # min() limita las horas normales a 40; max() evita horas extra negativas
    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = (hours_worked > REGULAR_HOURS_LIMIT)

    print("Regular pay:", round(regular_pay, 2))
    print("Overtime pay:", round(overtime_pay, 2))
    print("Total pay:", round(total_pay, 2))
    print("Has overtime:", str(has_overtime).lower())
else:
    print(ERROR_MESSAGE)


# Problem 3: Discount eligibility with booleans
# Description: Decide si un cliente recibe un 10% de descuento. El cliente es
#elegible si is_student es true OR is_senior es true OR el total de la compra es 1000.0 o más.

# Inputs:
#purchase_total (float): total de la compra.
#is_student_text (string): "YES" o "NO".
#is_senior_text (string): "YES" o "NO".

# Outputs:
#"Discount eligible:" true|false
#"Final total:" <final_total>

# Validations:
#purchase_total >= 0.0
#Los textos se pasan a mayúsculas y deben ser "YES" o "NO".
#Si no, mostrar "Error: invalid input".

# Test cases:
#1) Normal: total = 500, student = NO, senior = NO - Discount eligible: false, Final total: 500.0
#2) Border: total = 1000, student = no, senior = NO - Discount eligible: true, Final total: 900.0
#3) Error:  total = 200, student = MAYBE, senior = NO - Error: invalid input

print("\nDiscount eligibility")
purchase_text = input("Enter purchase total: ")
is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

try:
    purchase_total = float(purchase_text)
    is_valid = (math.isfinite(purchase_total) and purchase_total >= 0.0
                and is_student_text in ("YES", "NO")
                and is_senior_text in ("YES", "NO"))
except ValueError:
    is_valid = False

if is_valid:
    # Comparar strings produce un booleano
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    # "or": basta con que se cumpla una condición
    discount_eligible = (is_student or is_senior
                         or purchase_total >= DISCOUNT_MIN_PURCHASE)

    if discount_eligible:
        final_total = purchase_total * (1 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", round(final_total, 2))
else:
    print(ERROR_MESSAGE)


# Problem 4: Basic statistics of three integers
# Description: Lee tres enteros y calcula la suma, el promedio (float), el 
# máximo, el mínimo y un booleano all_even que indica si los tres números son pares.

# Inputs:
#n1 (int), n2 (int), n3 (int)

#Outputs:
# "Sum:" <sum_value>
# "Average:" <average_value>
# "Max:" <max_value>
# "Min:" <min_value>
# "All even:" true|false

# Validations:
# Los tres valores deben poder convertirse a int (se permiten negativos).

#Test cases:
#1) Normal: 2, 4, 6 - Sum: 12, Average: 4.0, Max: 6, Min: 2, All even: true
#2) Border: -3, 0, 3 - Sum: 0, Average: 0.0, Max: 3, Min: -3, All even: false
#3) Error:  5.5, 2, 1 - Error: invalid input (5.5 no es un int)

print("\nStatistics of three integers")
n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
    is_valid = True
except ValueError:
    is_valid = False

if is_valid:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3  # "/" siempre regresa un float
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    # "and": deben cumplirse las tres condiciones
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())
else:
    print(ERROR_MESSAGE)


# Problem 5: Loan eligibility (income and debt ratio)
# Description: Decide si una persona es elegible para un préstamo según su
#ingreso mensual, su deuda mensual y su score de crédito. debt_ratio = monthly_debt / monthly_income
#eligible es true si income >= 8000.0 AND debt_ratio <= 0.4 AND credit_score >= 650.

# Inputs:
# monthly_income (float)
# monthly_debt (float)
# credit_score (int)

# Outputs:
# "Debt ratio:" <debt_ratio>
# "Eligible:" true|false

# Validations:
# monthly_income > 0.0 (evita división entre cero)
# monthly_debt >= 0.0
# credit_score >= 0
# Si no se cumple, mostrar "Error: invalid input".

# Test cases:
#1) Normal: income = 10000, debt = 3000, score = 700 - Debt ratio: 0.3, Eligible: true
#2) Border: income = 8000, debt = 3200, score = 650 - Debt ratio: 0.4, Eligible: true
#3) Error:  income = 0, debt = 500, score = 700 - Error: invalid input

print("\nLoan eligibility")
income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt payments: ")
score_text = input("Enter credit score: ")

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)
    is_valid = (math.isfinite(monthly_income) and math.isfinite(monthly_debt)
                and monthly_income > 0.0 and monthly_debt >= 0.0
                and credit_score >= 0)
except ValueError:
    is_valid = False

if is_valid:
    # Aquí monthly_income ya es > 0, así que no hay división entre cero
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_INCOME
                and debt_ratio <= MAX_DEBT_RATIO
                and credit_score >= MIN_CREDIT_SCORE)

    print("Debt ratio:", round(debt_ratio, 2))
    print("Eligible:", str(eligible).lower())
else:
    print(ERROR_MESSAGE)


# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calcula el IMC con bmi = weight_kg / (height_m * height_m) y
#crea tres booleanos para la categoría: is_underweight (bmi < 18.5), is_normal (18.5 <= bmi < 25.0),
#is_overweight (bmi >= 25.0).

# Inputs:
# weight_kg (float): peso en kilogramos.
# height_m (float): estatura en metros.

# Outputs:
# "BMI:" <rounded_bmi>
# "Underweight:" true|false
# "Normal:" true|false
# "Overweight:" true|false

# Validations:
# weight_kg > 0.0
# height_m > 0.0
# Si no se cumple, mostrar "Error: invalid input".

# Test cases:
#1) Normal: weight = 70, height = 1.75 - BMI: 22.86, Underweight: false, Normal: true, Overweight: false
#2) Border: weight = 100, height = 2.0 - BMI: 25.0, Underweight: false, Normal: false, Overweight: true
#3) Error:  weight = 70, height = 0 - Error: invalid input

print("\nBody Mass Index")
weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)
    is_valid = (math.isfinite(weight_kg) and math.isfinite(height_m)
                and weight_kg > 0.0 and height_m > 0.0)
except ValueError:
    is_valid = False

if is_valid:
    bmi = weight_kg / (height_m * height_m)

    is_underweight = (bmi < UNDERWEIGHT_LIMIT)
    is_normal = (UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT)  # rango encadenado
    is_overweight = (bmi >= OVERWEIGHT_LIMIT)

    print("BMI:", round(bmi, 2))
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())
else:
    print(ERROR_MESSAGE)


"""
CONCLUSIONES

Los enteros y flotantes se usan juntos en cálculos reales: por ejemplo, en
los problemas de nómina e IMC los flotantes guardan dinero y medidas, y los 
enteros guardan cosas como el credit_score. Las comparaciones como
hours > 40 producen booleanos, y esos booleanos nos permiten decidir qué
hacer con las sentencias if. Validar rangos y evitar la división entre cero
es esencial, porque un ingreso o una estatura de cero haría fallar el
programa o daría resultados sin sentido. Aprendí que las condiciones
combinadas con and, or, not deben diseñarse con cuidado: "and" necesita que
todo sea verdadero (préstamo), mientras que "or" solo necesita una condición
(descuento). Estos mismos patrones se repiten en nómina, descuentos,
préstamos y aplicaciones de salud, por lo que dominarlos sirve para muchos
programas reales.

"""

"""
References:
1) Python documentation - Built-in Types: Numeric Types (int, float)
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python documentation - Boolean Type (bool)
https://docs.python.org/3/library/stdtypes.html#boolean-type-bool

3) Python documentation - Built-in Functions (round, min, max, abs)
https://docs.python.org/3/library/functions.html

4) Python Tutorial - An Informal Introduction to Python (numbers)
https://docs.python.org/3/tutorial/introduction.html

5) Apuntes de clase - Fundamentos de programación: operadores y validación de datos

"""
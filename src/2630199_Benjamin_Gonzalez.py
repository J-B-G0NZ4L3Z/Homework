# PORTADA
# Nombre: Jesus Benjamin Gonzalez Vallejo
# Matrícula: 2630199
# Grupo: 3
# Materia: Metodologias de la Programación
# Tarea: Colecciones en Python (list, tuple)

"""
 RESUMEN EJECUTIVO

 Una lista (list) es una colección ordenada y mutable: se puede agregar,
 quitar o cambiar elementos. Una tupla (tuple) es ordenada pero inmutable:
 una vez creada no se puede modificar, por eso sirve para datos fijos como
 coordenadas. Mutable significa que puede cambiar después de creada
 (append, pop); en una tupla inmutable eso da error.
 Este documento cubre 2 problemas: lista de compras (listas) y puntos con
 distancias (tuplas), cada uno con descripción, entradas, salidas,
 validaciones y tres casos de prueba.

"""

"""
PRINCIPIOS Y BUENAS PRÁCTICAS

Usar listas cuando se necesite agregar o eliminar elementos con frecuencia.
Usar tuplas para datos que no deben cambiar (coordenadas, fechas, config).
Evitar modificar una lista mientras se recorre con un for.
Usar nombres de variables descriptivos ("items_list", "point_a").
Escribir código legible y mensajes claros para el usuario.
Escribir el código directamente (sin funciones def), con input(), if/else y print(), para que sea más compacto y fácil de seguir de arriba hacia abajo.

"""

import math

# Constantes (UPPER_SNAKE_CASE)
ERROR_MESSAGE = "Error: invalid input"

# En el problema con datos numéricos (2) se usa la bandera is_valid
# (un booleano): el dato se lee como texto con input(), dentro de try se
# convierte a float y se revisa que sea un número real, y si la conversión
# falla (por ejemplo "abc") except marca is_valid = False.
# Los booleanos se muestran como "true"/"false" con str(valor).lower().


# Problem 1: Shopping list basics (list operations)
# Description: Crea una lista de productos a partir de un texto separado por comas, agrega un producto nuevo al final, muestra cuántos
#elementos hay y revisa si un producto está en la lista. Decisión de diseño: los productos se guardan en minúsculas
#para que la búsqueda no distinga mayúsculas de minúsculas, y una lista inicial vacía se considera un error.

# Inputs:
# -initial_items_text (string): por ejemplo "apple,banana,orange".
# -new_item (string): producto a agregar.
# -search_item (string): producto a buscar.

# Outputs:
# -"Items list:" <items_list>
# -"Total items:" <len_list>
# -"Found item:" true|false

# Validations:
# -initial_items_text no vacío tras strip().
# -Se separa por comas y se quitan espacios extra de cada elemento (los elementos vacíos, como en "a,,b", se descartan).
# -new_item y search_item no vacíos.

# Test cases:
#1) Normal: initial = "apple,banana,orange", new = "grape", search = "banana" -> Items list: ['apple', 'banana',
#'orange', 'grape'], Total items: 4, Found item: true
#2) Border: initial = "apple" (un solo elemento), new = "pear", search = "kiwi" -> Items list: ['apple', 'pear'],
#Total items: 2, Found item: false
#3) Error:  initial = "   " (solo espacios) -> Error: invalid input

print("\nProblem 1")
print("Shopping list basics")
initial_items_text = input("Enter initial items (comma separated): ").strip()
new_item = input("Enter new item: ").strip().lower()
search_item = input("Enter item to search: ").strip().lower()

# split() separa por comas; strip() limpia cada elemento
items_list = []
for raw_item in initial_items_text.split(","):
    clean_item = raw_item.strip().lower()
    if clean_item != "":
        items_list.append(clean_item)

# Si el texto inicial estaba vacío, items_list queda con 0 elementos
if len(items_list) == 0 or new_item == "" or search_item == "":
    print(ERROR_MESSAGE)
else:
    items_list.append(new_item)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())


# Problem 2: Points and distances with tuples
# Description: Representa dos puntos 2D como tuplas (x, y), calcula la distancia euclidiana entre ellos y crea una nueva tupla con
#el punto medio.

# Inputs:
# -x1, y1, x2, y2 (float): coordenadas de los puntos.

# Outputs:
# -"Point A:" (x1, y1)
# -"Point B:" (x2, y2)
# -"Distance:" <distance>
# -"Midpoint:" (mx, my)

# Validations:
# -Las 4 entradas deben poder convertirse a float.

# Test cases:
#   1) Normal: A = (0, 0), B = (3, 4) -> Point A: (0.0, 0.0), Point B: (3.0, 4.0), Distance: 5.0, Midpoint: (1.5, 2.0)
#   2) Border: A = (2, 2), B = (2, 2) (mismo punto) -> Distance: 0.0, Midpoint: (2.0, 2.0)
#   3) Error:  x1 = "abc" -> Error: invalid input

print("\nProblem 2")
print("Points and distances")
x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
    # float() acepta "nan" e "inf", pero no son números reales
    is_valid = (math.isfinite(x1) and math.isfinite(y1)
                and math.isfinite(x2) and math.isfinite(y2))
except ValueError:
    is_valid = False

if is_valid:
    # Las tuplas son inmutables: los puntos no cambian después de creados
    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = (round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2))

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
else:
    print(ERROR_MESSAGE)

# CONCLUSIONES

# Las listas conviene usarlas cuando los datos cambian seguido, porque con
# append() y pop() se agrega y elimina de forma flexible; en el problema 1
# sirvieron para armar la lista de compras y buscar un producto con "in".
# Las tuplas son útiles para datos que no deben cambiar, como las
# coordenadas de un punto, porque Python impide modificarlas por error; en el
# problema 2 se usaron para los puntos y el punto medio. También aprendí a
# validar antes de operar: listas vacías o números inválidos dan errores si
# no se revisan primero.

# REFERENCIAS

# References:
# 1) Python documentation - Built-in Types: list, tuple
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python documentation - String Methods (split, strip, lower)
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 4) Python documentation - Built-in Functions (len, round, float)
#    https://docs.python.org/3/library/functions.html
# 5) Apuntes de clase - Metodologías de la Programación: colecciones y validación

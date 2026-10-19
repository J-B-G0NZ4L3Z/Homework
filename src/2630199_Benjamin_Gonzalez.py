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
 coordenadas. Para relacionar datos (nombre -> precio) se usan listas
 paralelas: la posición (índice) de un elemento en una lista corresponde a
 la del elemento relacionado en la otra. Mutable significa que puede cambiar
 después de creada (append, pop); en una tupla inmutable eso da error.
 Este documento cubre 6 problemas: lista de compras, puntos con tuplas,
 catálogo, calificaciones, contador de palabras y agenda de contactos, cada
 uno con descripción, entradas, salidas, validaciones y tres casos de prueba.

"""

"""
PRINCIPIOS Y BUENAS PRÁCTICAS

Usar listas cuando se necesite agregar o eliminar elementos con frecuencia.
Usar tuplas para datos que no deben cambiar (coordenadas, fechas, config).
Usar listas paralelas cuando se necesite relacionar datos (nombre y precio)  y mantenerlas siempre con la misma longitud y el mismo orden.
Evitar modificar una lista mientras se recorre con un for.
Usar nombres de variables descriptivos ("product_names", "product_prices").
Escribir código legible y mensajes claros para el usuario.
Escribir el código directamente (sin funciones def), con input(), if/else y print(), para que sea más compacto y fácil de seguir de arriba hacia abajo.

"""

import math

# Constantes (UPPER_SNAKE_CASE)
PASSING_GRADE = 70.0
PUNCTUATION_CHARS = ".,;:!?\"'()¡¿"

ERROR_MESSAGE = "Error: invalid input"

# En los problemas con datos numéricos (2 y 3) se usa la bandera is_valid
# (un booleano): el dato se lee como texto con input(), dentro de try se
# convierte a int/float y se revisan los rangos, y si la conversión falla
# (por ejemplo "abc") except marca is_valid = False.
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


# Problem 3: Product catalog with parallel lists
# Description: Usa dos listas paralelas: product_names y product_prices (el precio de la posición i
#pertenece al producto de la posición i). Lee un producto y una cantidad, y calcula el total a pagar si el producto
#existe; si no existe, muestra un error. Decisión de diseño: el nombre se pasa a minúsculas.

# Inputs:
# -product_name (string).
# -quantity (int): cantidad a comprar.

# Outputs:
# -Si existe: "Unit price:" <unit_price>, "Quantity:" <quantity>,
#                "Total:" <total_price>
# -Si no existe: "Error: product not found"

# Validations:
# -quantity > 0 y debe ser int.
# -product_name no vacío tras strip().
# -Se verifica que product_name esté en la lista product_names.

# Test cases:
#   1) Normal: product = "bread", quantity = 3 -> Unit price: 10.0, Quantity: 3, Total: 30.0
#   2) Border: product = "avocado", quantity = 1 -> Unit price: 22.5, Quantity: 1, Total: 22.5
#   3) Error:  product = "grape", quantity = 0 -> Error: invalid input product = "banana", quantity = 2 -> Error: product not found

print("\nProblem 3")
print("Product catalog")
# Listas paralelas: misma posición = mismo producto
product_names = ["bread", "grape", "apple", "avocado"]
product_prices = [10.0, 5.5, 8.0, 22.5]

product_name = input("Enter product name: ").strip().lower()
quantity_text = input("Enter quantity: ")

try:
    quantity = int(quantity_text)
    is_valid = (product_name != "" and quantity > 0)
except ValueError:
    is_valid = False

if is_valid:
    if product_name in product_names:
        position = product_names.index(product_name)  # posición del producto
        unit_price = product_prices[position]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))
    else:
        print("Error: product not found")
else:
    print(ERROR_MESSAGE)


# Problem 4: Student grades with parallel lists (list of lists)
# Description: Usa una lista de nombres (student_names) y una lista de listas de calificaciones
#(all_grades), donde la posición i de all_grades tiene las calificaciones del estudiante i. Lee el
#nombre de un estudiante, calcula su promedio y dice si está aprobado (promedio >= 70.0) con is_passed.
#Decisión de diseño: el nombre se normaliza con title(); "Diego" tiene lista vacía a propósito (prueba de validación).

# Inputs:
# -student_name (string).

# Outputs:
# -Si existe: "Grades:" <grades_list>, "Average:" <average>,
#                "Passed:" true|false
# -Si no existe: "Error: student not found"

# Validations:
# -student_name no vacío tras strip().
# -Se verifica que student_name esté en la lista student_names.
# -La lista de calificaciones no debe estar vacía antes de promediar.

# Test cases:
#   1) Normal: "Alice" -> Grades: [90.0, 85.0, 95.0], Average: 90.0, Passed: true
#   2) Border: "carla" -> Grades: [70.0, 70.0, 70.0], Average: 70.0, Passed: true (justo en el límite de 70.0)
#   3) Error:  "" -> Error: invalid input "Zoe" -> Error: student not found
#"Diego" -> Error: no grades available

print("\nProblem 4")
print("Student grades")
student_names = ["Benjamin", "Flor", "Jean", "Sofia"]
all_grades = [
    [90.0, 85.0, 95.0],
    [60.0, 70.0, 65.0],
    [70.0, 70.0, 70.0],
    [],
]

student_name = input("Enter student name: ").strip().title()

if student_name == "":
    print(ERROR_MESSAGE)
else:
    if student_name not in student_names:
        print("Error: student not found")
    else:
        position = student_names.index(student_name)
        grades_list = all_grades[position]

        # Evita dividir entre cero con una lista vacía
        if len(grades_list) == 0:
            print("Error: no grades available")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = (average >= PASSING_GRADE)

            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            print("Passed:", str(is_passed).lower())


# Problem 5: Word frequency counter (lists + tuples)
# Description: Lee una oración, la pasa a minúsculas, la separa en una lista
# de palabras y construye una lista de tuplas (palabra, frecuencia). Muestra también la palabra más frecuente.
#Decisión de diseño: los signos de puntuación simples se quitan con replace(); si hay empate, gana la palabra que
#apareció primero.

# Inputs:
# -sentence (string).
#
# Outputs:
# -"Words list:" <words_list>
# -"Frequencies:" <freq_list> (lista de tuplas (palabra, frecuencia))
# -"Most common word:" <word>
#
# Validations:
# -sentence no vacía tras strip().
# -La lista de palabras no debe quedar vacía (por ejemplo "!!!").
#
# Test cases:
#1) Normal: "The cat and the dog" -> Words list: ['the', 'cat', 'and', 'the', 'dog'], Frequencies: [('the', 2), ('cat', 1),
#('and', 1), ('dog', 1)], Most common word: the
#2) Border: "Hello" (una sola palabra) -> Words list: ['hello'], Frequencies: [('hello', 1)], Most common word: hello
#"Hi, hi!" -> Frequencies: [('hi', 2)] (ignora puntuación)
#3) Error:  "   " o "!!!" -> Error: invalid input

print("\nProblem 5")
print("Word frequency counter")
sentence = input("Enter a sentence: ").strip().lower()

# Quita signos de puntuación simples
for char in PUNCTUATION_CHARS:
    sentence = sentence.replace(char, "")

words_list = sentence.split()

# Una oración vacía, de solo espacios o de solo signos da 0 palabras
if len(words_list) == 0:
    print(ERROR_MESSAGE)
else:
    # Construye la lista de tuplas (palabra, frecuencia) en orden de aparición
    freq_list = []
    seen_words = []
    for word in words_list:
        if word not in seen_words:
            seen_words.append(word)
            freq_list.append((word, words_list.count(word)))

    # Busca la palabra con mayor frecuencia (en empate gana la primera)
    most_common_word = ""
    max_count = 0
    for word, count in freq_list:
        if count > max_count:
            max_count = count
            most_common_word = word

    print("Words list:", words_list)
    print("Frequencies:", freq_list)
    print("Most common word:", most_common_word)


# Problem 6: Simple contact book (parallel lists CRUD)
# Description: Mini agenda de contactos con dos listas paralelas: contact_names y contact_phones.
#Según la acción (ADD, SEARCH o DELETE) agrega/actualiza, busca o elimina un contacto y muestra el resultado.
#Cada vez que se ejecuta el problema, la agenda empieza con los contactos iniciales (Alice, Bob y Carla). El nombre se
#normaliza con title().

# Inputs:
# -action_text (string): "ADD", "SEARCH" o "DELETE".
# -name (string).
# -phone (string): solo para "ADD".

# Outputs:
# -ADD: "Contact saved:" name, phone
# -SEARCH: "Phone:" <phone>  o  "Error: contact not found"
# -DELETE: "Contact deleted:" name  o  "Error: contact not found"

# Validations:
# -action_text se pasa a mayúsculas y debe ser una de las 3 opciones.
# -name no vacío tras strip().
# -Para ADD: phone no vacío tras strip().

# Test cases:
#1) Normal: ADD, "David", "5559998888" -> Contact saved: David 5559998888
#2) Border: ADD, "Alice", "1111111111" (contacto que ya existe, se actualiza) -> Contact saved: Alice 1111111111
#SEARCH, "alice" (minúsculas) -> Phone: 1234567890
#3) Error:  action = "UPDATE" -> Error: invalid input SEARCH, "Zoe" -> Error: contact not found

print("\nProblem 6")
print("Contact book")
# Listas paralelas: misma posición = mismo contacto
contact_names = ["Benjamin", "Lorena", "Miguel"]
contact_phones = ["1234567890", "0987654321", "6767676767"]

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print(ERROR_MESSAGE)
else:
    name = input("Enter contact name: ").strip().title()

    if name == "":
        print(ERROR_MESSAGE)
    else:
        # Solo uno de estos tres if se cumple, según la acción elegida
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if phone == "":
                print(ERROR_MESSAGE)
            else:
                if name in contact_names:
                    # Ya existía: se actualiza su teléfono
                    position = contact_names.index(name)
                    contact_phones[position] = phone
                else:
                    # No existía: se agrega al final de ambas listas
                    contact_names.append(name)
                    contact_phones.append(phone)
                print("Contact saved:", name, phone)

        if action_text == "SEARCH":
            if name in contact_names:
                position = contact_names.index(name)
                print("Phone:", contact_phones[position])
            else:
                print("Error: contact not found")

        if action_text == "DELETE":
            if name in contact_names:
                position = contact_names.index(name)
                contact_names.pop(position)   # se elimina de ambas listas
                contact_phones.pop(position)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")


# CONCLUSIONES

# Las listas conviene usarlas cuando los datos cambian seguido, porque con
# append() y pop() se agrega y elimina de forma flexible. Las tuplas son
# útiles para datos que no deben cambiar, como las coordenadas de un punto,
# porque Python impide modificarlas por error. Las listas paralelas relacionan
# datos (producto y precio, contacto y teléfono) usando el índice: con "in" e
# index() se encuentra la posición y con ella el dato relacionado. Un patrón
# común fue la lista de listas (calificaciones) y la lista de tuplas (palabra,
# frecuencia). Validar antes de operar evita errores con listas vacías.

# REFERENCIAS

# References:
# 1) Python documentation - Built-in Types: list, tuple
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python documentation - String Methods (split, strip, lower, replace)
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 4) Python documentation - Built-in Functions (len, sum, min, max, sorted)
#    https://docs.python.org/3/library/functions.html
# 5) Apuntes de clase - Metodologías de la Programación: colecciones y validación

"""
PORTADA
Nombre del estudiante: Jesus Benjamin Gonzalez Vallejo 
Matrícula: 2630199
Grupo: 3
Tarea: Manejo de Cadenas de Texto (Strings) en Python
"""

"""
RESUMEN EJECUTIVO

Un string en Python es un tipo de datos secuencial compuesto por caracteres 
inmutables, lo que significa que cualquier modificación genera un nuevo 
objeto de cadena en la memoria. Las operaciones básicas incluyen concatenación, 
cálculo de longitud, extracción de subcadenas usando slicing (rebanado), 
búsqueda de patrones y reemplazo de texto. Validar y normalizar la entrada 
del usuario (como correos, nombres y contraseñas) es fundamental para garantizar 
la integridad de los datos, la seguridad y prevenir errores lógicos o inyecciones. 
Este documento cubre seis problemas prácticos que demuestran la normalización 
de entradas, validaciones robustas, métodos de manipulación de cadenas y casos de prueba.

"""

"""
PRINCIPIOS Y BUENAS PRÁCTICAS

- Los strings son inmutables: cualquier cambio crea una nueva cadena.
- Es buena práctica normalizar la entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero verificar que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
- Escribir el código directamente (sin funciones def), con input(), if/else
  y print(), para que sea más compacto y fácil de seguir de arriba hacia abajo.

"""

# Constante(UPPER_SNAKE_CASE) en todos los programas esta es la constante 
ERROR_MESSAGE = "Error: invalid input"

# PROBLEMA 1: Formateador de nombre completo (nombre + iniciales)
"""
Problem 1: Full name formatter (name + initials)
Descripción: Toma una cadena con el nombre completo, normaliza los espacios, 
lo formatea en formato de título (Title Case) y extrae las iniciales 
en mayúsculas separadas por puntos.

Entradas:
full_name (string; nombre completo, mayúsculas/minúsculas mezcladas, espacios extra).

Salidas:
"Formatted name: <Name In Title Case>"
"Initials: <X.X.X.>"

Validaciones:
full_name no debe estar vacío después de strip().
Debe contener al menos dos palabras (nombre y apellido).
No puede ser solo espacios.

Casos de prueba:
1) Normal: "jesus benjamin gonzalez vallejo" - Formatted: Jesus benjamin gonzalez vallejo, Initials: J.B.G.V.
2) Border (Borde): " agripino  " - Error: invalid input (solo una palabra).
3) Error: "   " - Error: invalid input (cadena vacía).
"""
print("\nProblem 1")
print("Full name formatter")
full_name_input = input("Enter your full name: ")
cleaned_name = full_name_input.strip()
words = cleaned_name.split()  # split() ignora los espacios extra

# Una cadena vacía o de solo espacios da 0 palabras, y "agripino" da 1: ambas < 2
if len(words) < 2:
    print(ERROR_MESSAGE)
else:
    formatted_name = " ".join(words).title()

    initials_str = ""
    for word in words:
        initials_str = initials_str + word[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials_str}")


# PROBLEMA 2: Validador simple de correo electrónico (estructura + dominio)
"""
Problem 2: Simple email validator (structure + domain)
Descripción: Valida la estructura básica de un correo verificando que tenga 
exactamente una '@', al menos un '.' después de la '@' y sin espacios en blanco. 
Extrae el dominio si es válido.

Entradas:
email_text (string).

Salidas:
"Valid email: true" o "Valid email: false"
Si es válido: "Domain: <domain_part>"

Validaciones:
email_text no vacío tras strip().
Debe contener exactamente una '@'.
No se permiten espacios en blanco.
Al menos un '.' después de la '@'.

Casos de prueba:
1) Normal: "user@example.com" - Valid: true, Domain: example.com
2) Border: "user@com" - Valid: false (falta punto en el dominio)
3) Error: "user name@domain.com" - Valid: false (contiene espacio)
"""
print("\nProblema 2")
print("Email validator")
email_text = input("Enter an email: ").strip()

# Primero se revisa la estructura general (bandera booleana)
is_valid = (email_text != "" and " " not in email_text
            and email_text.count("@") == 1)

# Si la estructura es correcta, se revisa el dominio (lo que va después de '@')
domain_part = ""
if is_valid:
    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]
    is_valid = ("." in domain_part
                and not domain_part.startswith(".")
                and not domain_part.endswith("."))

if is_valid:
    print("Valid email: true")
    print(f"Domain: {domain_part}")
else:
    print("Valid email: false")


# PROBLEMA 3: Verificador de palíndromos (ignorando espacios y mayúsculas)
"""
Problem 3: Palindrome checker (ignoring spaces and case)
Descripción: Determina si una frase se lee igual de izquierda a derecha 
que de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- Muestra la versión normalizada.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima de al menos 3 caracteres después de limpiar espacios.

Casos de prueba:
1) Normal: "Anita lava la tina" -> Is palindrome: true
2) Border: "Ab a" -> Is palindrome: true
3) Error: "Hi" -> Error: invalid input (muy corto)
"""
print("\nProblem 3")
print("Palindrome checker ---")
phrase = input("Enter a phrase: ")
normalized = phrase.strip().lower().replace(" ", "")

# Si queda con menos de 3 caracteres (incluida la cadena vacía) es un error
if len(normalized) < 3:
    print(ERROR_MESSAGE)
else:
    is_pal = (normalized == normalized[::-1])  # [::-1] invierte el string
    print(f"Normalized phrase: {normalized}")
    print(f"Is palindrome: {str(is_pal).lower()}")


# PROBLEMA 4: Estadísticas de palabras en una oración (longitudes, primera y última)

"""
Problem 4: Sentence word stats (lengths and first/last word)
Descripción: Analiza una oración para extraer el conteo total de palabras, 
la primera palabra, la última, la más corta y la más larga.

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida tras el split().

Casos de prueba:
1) Normal: "Python programming is amazing" -> Count: 4, First: Python, Last: amazing, Shortest: is, Longest: programming
2) Border: "Hello" -> Count: 1, First: Hello, Last: Hello, Shortest: Hello, Longest: Hello
3) Error: "   " -> Error: invalid input
"""
print("\nProblem 4")
print("Sentence word stats ---")
sentence = input("Enter a sentence: ")
sentence_words = sentence.strip().split()

if len(sentence_words) == 0:
    print(ERROR_MESSAGE)
else:
    shortest_word = sentence_words[0]
    longest_word = sentence_words[0]

    for current_word in sentence_words:
        if len(current_word) < len(shortest_word):
            shortest_word = current_word
        if len(current_word) > len(longest_word):
            longest_word = current_word

    print(f"Word count: {len(sentence_words)}")
    print(f"First word: {sentence_words[0]}")
    print(f"Last word: {sentence_words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# PROBLEMA 5: Clasificador de fortaleza de contraseñas

"""
Problem 5: Password strength classifier
Descripción: Clasifica una contraseña como débil (weak), media (medium) 
o fuerte (strong) según su longitud y la variedad de caracteres 
(mayúsculas, minúsculas, dígitos y símbolos).

Entradas:
- password_input (string).

Outputs:
- "Password strength: weak" / "medium" / "strong"

Validaciones:
- La contraseña no debe estar vacía.
- Se verifica mediante len() y banderas de inspección de caracteres.

Casos de prueba:
1) Normal: "P@ssw0rd123" -> Password strength: strong
2) Border: "password123" -> Password strength: medium
3) Error: "" -> Error: invalid input
"""
print("\nProblem 5")
print("Password strength ---")
password_input = input("Enter a password: ")

if password_input == "":
    print(ERROR_MESSAGE)
else:
    length = len(password_input)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Cada carácter es de un solo tipo, así que bastan if separados
    for char in password_input:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_symbol = True

    if length < 8 or (not has_upper and not has_digit):
        strength = "weak"
    else:
        if has_upper and has_lower and has_digit and has_symbol:
            strength = "strong"
        else:
            strength = "medium"

    print(f"Password strength: {strength}")


# PROBLEMA 6: Formateador de etiquetas de productos (texto de ancho fijo)

"""
Problem 6: Product label formatter (fixed-width text)
Descripción: Genera una etiqueta de producto en una sola línea combinando 
el nombre y el precio con una longitud fija exacta de 30 caracteres 
(rellenando con espacios o recortando si es necesario).

Entradas:
- product_name (string).
- price_value (string o número).

Salidas:
- "Label: <exactly 30 characters>"

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Casos de prueba:
1) Normal: "Pen", 5.5 -> Label: "Product: Pen | Price: $5.5" + 4 espacios (30 caracteres)
2) Border: "VeryLongProductNamethatexceedslimit", 99.99 -> Se recorta a 30 caracteres.
3) Error: "", 50 -> Error: invalid input

"""

print("\nProblem 6")
print("Product label formatter")
product_name = input("Enter product name: ").strip()
price_text = input("Enter price: ")

# Si el precio no se puede convertir a número, se marca como inválido (-1)
try:
    numeric_price = float(price_text)
except ValueError:
    numeric_price = -1

if product_name == "" or numeric_price <= 0:
    print(ERROR_MESSAGE)
else:
    raw_label = f"Product: {product_name} | Price: ${numeric_price}"

    # Formato de ancho fijo: exactamente 30 caracteres
    if len(raw_label) < 30:
        fixed_label = raw_label.ljust(30)  # rellena con espacios
    else:
        fixed_label = raw_label[:30]  # recorta

    print(f"Label: \"{fixed_label}\" (Length: {len(fixed_label)})")


"""
CONCLUSIONES
El manejo de cadenas de texto es esencial en el desarrollo de software para una 
correcta entrada y salida de datos. Métodos como lower(), strip() y split() 
permiten limpiar, tokenizar y estandarizar datos de usuario desordenados de 
forma sencilla. Normalizar el texto antes de compararlo previene errores sutiles 
causados por diferencias de mayúsculas o espacios en blanco al final. Las 
validaciones robustas protegen las aplicaciones frente a entradas maliciosas, 
valores vacíos y formatos inesperados. Finalmente, comprender la inmutabilidad 
de los strings y el uso de slices otorga un control eficiente sobre los segmentos 
de texto sin comprometer la seguridad en memoria.
"""

"""
REFERENCIAS
1) Python Software Foundation. (2026). Built-in Types: Text Sequence Type — str.  Python Documentation. Retrieved from https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
2) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media.
3) Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. Green Tea Press.
4) Sweigart, A. (2019). Automate the Boring Stuff with Python (2nd ed.). No Starch Press.
5) Python Documentation Team. (2026). Input and Output Operations and Best Practices for Data Validation in Python Applications.
"""
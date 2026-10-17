"""
PORTADA
Nombre del estudiante: Jesus Benjamin Gonzalez Vallejo 
Matrícula: 2630199
Grupo: 3
Tarea: Manejo de Cadenas de Texto (Strings) en Python
Repositorio de GitHub: https://github.com/J-B-G0NZ4L3Z/Homework.git

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

"""

# PROBLEMA 1: Formateador de nombre completo (nombre + iniciales)
"""
Problem 1: Full name formatter (name + initials)
Descripción: Toma una cadena con el nombre completo, normaliza los espacios, 
lo formatea en formato de título (Title Case) y extrae las iniciales 
en mayúsculas separadas por puntos.

Entradas:
- full_name (string; nombre completo, mayúsculas/minúsculas mezcladas, espacios extra).

Salidas:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (nombre y apellido).
- No puede ser solo espacios.

Casos de prueba:
1) Normal: "juan carlos tovar" -> Formatted: Juan Carlos Tovar, Initials: J.C.T.
2) Border (Borde): "  maria  " -> Error: invalid input (solo una palabra).
3) Error: "   " -> Error: invalid input (cadena vacía).
"""

def format_full_name(full_name_input):
    cleaned_name = full_name_input.strip()
    
    # Validar si está vacío o solo contiene espacios
    if not cleaned_name:
        return "Error: invalid input"
    
    words = cleaned_name.split()
    
    # Validar que contenga al menos dos palabras
    if len(words) < 2:
        return "Error: invalid input"
    
    formatted_name = cleaned_name.title()
    
    initials_list = []
    for word in words:
        initials_list.append(word[0].upper() + ".")
    
    initials_str = "".join(initials_list)
    
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials_str}")
    return True


# ====================================================================
# PROBLEMA 2: Validador simple de correo electrónico (estructura + dominio)
# ====================================================================
"""
Problem 2: Simple email validator (structure + domain)
Descripción: Valida la estructura básica de un correo verificando que tenga 
exactamente una '@', al menos un '.' después de la '@' y sin espacios en blanco. 
Extrae el dominio si es válido.

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Debe contener exactamente una '@'.
- No se permiten espacios en blanco.
- Al menos un '.' después de la '@'.

Casos de prueba:
1) Normal: "user@example.com" -> Valid: true, Domain: example.com
2) Border: "user@com" -> Valid: false (falta punto en el dominio)
3) Error: "user name@domain.com" -> Valid: false (contiene espacio)
"""

def validate_email(email_text):
    cleaned_email = email_text.strip()
    
    if not cleaned_email or " " in cleaned_email:
        print("Valid email: false")
        return False
        
    if cleaned_email.count("@") != 1:
        print("Valid email: false")
        return False
        
    at_index = cleaned_email.find("@")
    domain_part = cleaned_email[at_index + 1:]
    
    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        print("Valid email: false")
        return False
        
    print("Valid email: true")
    print(f"Domain: {domain_part}")
    return True


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

def check_palindrome(phrase):
    cleaned_phrase = phrase.strip()
    
    if not cleaned_phrase:
        return "Error: invalid input"
        
    normalized = cleaned_phrase.lower().replace(" ", "")
    
    if len(normalized) < 3:
        return "Error: invalid input"
        
    is_pal = normalized == normalized[::-1]
    
    print(f"Normalized phrase: {normalized}")
    print(f"Is palindrome: {str(is_pal).lower()}")
    return is_pal


# ====================================================================
# PROBLEMA 4: Estadísticas de palabras en una oración (longitudes, primera y última)
# ====================================================================
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

def analyze_sentence(sentence):
    cleaned_sentence = sentence.strip()
    
    if not cleaned_sentence:
        return "Error: invalid input"
        
    words = cleaned_sentence.split()
    if not words:
        return "Error: invalid input"
        
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]
    
    shortest_word = words[0]
    longest_word = words[0]
    
    for w in words:
        if len(w) < len(shortest_word):
            shortest_word = w
        if len(w) > len(longest_word):
            longest_word = w
            
    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")
    return True


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

def classify_password(password_input):
    if not password_input:
        return "Error: invalid input"
        
    length = len(password_input)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True
            
    if length < 8 or (not has_upper and not has_digit):
        strength = "weak"
    elif length >= 8 and ((has_upper and has_lower) or has_digit) and not has_symbol:
        strength = "medium"
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"
        
    print(f"Password strength: {strength}")
    return strength

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
1) Normal: "Laptop", 1200.50 -> Label: "Product: Laptop | Price: $1200.5"
2) Border: "VeryLongProductNamethatexceedslimit", 99.99 -> Se recorta a 30 caracteres.
3) Error: "", 50 -> Error: invalid input
"""

def format_product_label(product_name, price_value):
    cleaned_name = product_name.strip()
    
    if not cleaned_name:
        return "Error: invalid input"
        
    try:
        numeric_price = float(price_value)
        if numeric_price < 0:
            return "Error: invalid input"
    except ValueError:
        return "Error: invalid input"
        
    raw_label = f"Product: {cleaned_name} | Price: ${numeric_price}"
    
    # Formato de ancho fijo: exactamente 30 caracteres
    if len(raw_label) < 30:
        fixed_label = raw_label.ljust(30)
    else:
        fixed_label = raw_label[:30]
        
    print(f"Label: \"{fixed_label}\" (Length: {len(fixed_label)})")
    return fixed_label


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

# Bloque de ejecución para probar los casos de prueba
if __name__ == "__main__":
    print("Casos de Prueba")
    print("\n[Prueba Problema 1]")
    format_full_name("Jesus Benjamin Gonzalez Vallejo")
    
    print("\n[Prueba Problema 2]")
    validate_email("2630199@upv.edu.mx")
    
    print("\n[Prueba Problema 3]")
    check_palindrome("Anita lava la tina")
    
    print("\n[Prueba Problema 4]")
    analyze_sentence("En python esta chido trabajar")
    
    print("\n[Prueba Problema 5]")
    classify_password("P@ssw0rd123")
    
    print("\n[Prueba Problema 6]")
    format_product_label("Laptop", 1200.50)
# Diccionario de traducción inglés -> español
diccionario_ingles_a_espanol = {
    "hello": "hola",
    "good": "bueno",
    "morning": "mañana",
    "how": "cómo",
    "are": "estás",
    "you": "tú",
    "thank": "gracias",
    "bye": "adiós",
    "my": "mi",
    "name": "nombre",
    "is": "es"
}

# Diccionario de traducción español -> inglés
diccionario_espanol_a_ingles = {v: k for k, v in diccionario_ingles_a_espanol.items()}

# Función para traducir una palabra
def traducir_palabra(palabra, direccion):
    # Convertir la palabra a minúsculas para evitar problemas con mayúsculas
    palabra = palabra.lower()
    
    if direccion == "ingles_a_espanol":
        # Traducir de inglés a español
        return diccionario_ingles_a_espanol.get(palabra, palabra)
    elif direccion == "espanol_a_ingles":
        # Traducir de español a inglés
        return diccionario_espanol_a_ingles.get(palabra, palabra)
    else:
        return palabra

# Función para traducir una oración completa
def traducir_oracion(oracion, direccion):
    # Separar la oración en palabras (usando el espacio como separador)
    palabras = oracion.split()
    # Traducir cada palabra usando la función traducir_palabra
    oracion_traducida = [traducir_palabra(palabra, direccion) for palabra in palabras]
    # Unir las palabras traducidas en una nueva oración
    return " ".join(oracion_traducida)

# Función principal que interactúa con el usuario
def traductor():
    print("Bienvenido al traductor de inglés y español.")
    
    # Elegir el sentido de la traducción
    direccion = input("Elige la dirección de la traducción (1) Inglés a Español (2) Español a Inglés: ")
    
    if direccion == "1":
        direccion = "ingles_a_espanol"
        print("Traducción de inglés a español.")
    elif direccion == "2":
        direccion = "espanol_a_ingles"
        print("Traducción de español a inglés.")
    else:
        print("Opción no válida. Se usará inglés a español por defecto.")
        direccion = "ingles_a_espanol"
    
    oracion = input("Introduce una oración: ")
    oracion_traducida = traducir_oracion(oracion, direccion)
    print(f"La traducción es: {oracion_traducida}")

# Ejecutar el programa
traductor()
#Autor: Dr. Aldo Gonzalez Vazquez
#Version: 0.2
#Licencia: MIT
#Fecha: 20/11/2024
# Diccionario con algunas palabras básicas español-inglés
diccionario = {
    'hola': 'hello',
    'buenos': 'good',
    'días': 'morning',
    'gracias': 'thank you',
    'porfavor': 'please',
    'amigo': 'friend',
    'gato': 'cat',
    'perro': 'dog',
    'casa': 'house',
    'libro': 'book',
    'un': 'a'
}

def traducir(oracion):
    """
    Traduce una oración simple del español al inglés
    usando un diccionario básico de palabras
    
    Args:
        oracion (str): La oración a traducir
    
    Returns:
        str: La traducción de la oración en inglés
    
    Raises:
        ValueError: Si se encuentran palabras en la oración que no están en el diccionario
    """
    # Convertir a minúsculas para hacer la búsqueda más fácil
    oracion = oracion.lower()
    
    # Dividir la oración en palabras
    palabras = oracion.split()
    
    # Traducir cada palabra
    traduccion = []
    for palabra in palabras:
        try:
            # Buscar la palabra en el diccionario
            palabra_traducida = diccionario.get(palabra, palabra)
            traduccion.append(palabra_traducida)
        except KeyError:
            raise ValueError(f"La palabra '{palabra}' no está en el diccionario")
    
    # Unir las palabras traducidas
    return ' '.join(traduccion)

# Ejemplo de uso
if __name__ == "__main__":
    oracion_es = "hola amigo un gato porfavor"
    try:
        traduccion = traducir(oracion_es)
        print(f"Español: {oracion_es}")
        print(f"Inglés: {traduccion}")
    except ValueError as e:
        print(f"Error: {e}")

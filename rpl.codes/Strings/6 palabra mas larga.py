"""Completar el cuerpo de la función. La misma recibe un texto y debe retornar cuál es la palabra más larga del mismo. Se puede asumir que todas las palabras están separadas por espacios y no hay caracteres especiales.

No se pueden utilizar funciones de otras estructuras de datos. El ejercicio se debe resolver iterando la cadena, llevando el registro de las variables que se consideren adecuadas.

Ayuda: Tener cuidado con el caso en el que la palabra más larga es la última de todo el texto.

Ejemplos:

    palabra_mas_larga("Hola como estas este es un texto de prueba") => "prueba"
    palabra_mas_larga("Quiero aprobar algoritmos y algebra") => "algoritmos"""

def palabra_mas_larga(texto):
    palabras = texto.split(" ")
    palabras_ordenadas = sorted(palabras, key= lambda x: len(x))
    return palabras_ordenadas[-1]
print(palabra_mas_larga("Hola como estas este es un texto de prueba"))

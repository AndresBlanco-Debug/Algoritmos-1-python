"""Completar el cuerpo de la función. La misma recibe una cadena y debe retornar la misma habiendo filtrado todas las vocales que contenía.

Ejemplos:

    filtrador_de_vocales("hola") => "hl"
    filtrador_de_vocales("facultad") => "fcltd"
    filtrador_de_vocales("algoritmos") => "lgrtms"   """

def filtrador_de_vocales(cadena):
    vocales = "aeiou"
    for letra in cadena:
        if letra in vocales:
            cadena = cadena.replace(letra,"")
    return cadena
print(filtrador_de_vocales("hola"))

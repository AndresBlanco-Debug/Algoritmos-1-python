"""Completar el cuerpo de la función. La misma recibe una cadena de caracteres y dos caracteres individuales. 
Debe retornar la suma de la cantidad de veces que aparecen cada uno de los caracteres en la cadena.
Hint: No utilizar la función .count() de las cadenas. Cada vez que la invocamos, Python realiza un recorrido por la cadena buscando la subcadena que la función recibe -
como parámetro. Resolver el ejercicio realizando una única iteración en toda la cadena.

Ejemplo:

    contar_caracteres("casa", "c", "a") => 3
    contar_caracteres("cosa", "c", "a") => 2
    contar_caracteres("algoritmos", "a", "o") => 3
    contar_caracteres("algoritmos", "w", "x") => 0"""

def contar_caracteres(cadena, caracter_1, caracter_2):
    
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0

    for letra in cadena:
        if caracter_1 == letra:
            contador_1 = contador_1 + 1
        elif caracter_2 == letra:
            contador_2 = contador_2 + 1
    contador_3 = contador_1 + contador_2
    return contador_3

print(contar_caracteres("casa","c","a"))

"""Completar los cuerpos de las distintas funciones. A continuación se encuentran los requerimientos que deben cumplir cada una de las funciones. Las funciones deben ser resueltas realizando iteraciones sobre las listas, no se pueden usar funciones de ordenamiento.

filtrar_pares: Recibe una lista con variables numéricas enteras. 
Retorna una nueva lista con todos los números pares que estaban en la lista que se recibió como parámetro. Los elementos de la lista devuelta deben estar en el orden original.

Ejemplo:

    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]
filtrar_primos: Recibe una lista con variables numéricas enteras. 
Retorna una nueva lista con todos los números primos que estaban en la lista que se recibió como parámetro Los elementos de la lista devuelta deben estar en el orden original.

Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

Ejemplo:

    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]
sumar_elementos: Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
No se puede utilizar la función sum(), ya existente en Python.

Ejemplo:

    sumar_elementos([5,6,13,7,11,9,10,11]) => 72
esta_ordenada: Recibe una lista con variables numericas. 
Retorna True en caso de que la lista este ordenada ascendentemente (es decir, los mas chicos en las primeras posiciones), False en caso contrario.

Ejemplos:

    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True
producto_escalar: Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores. Retorna el producto escalar entre ambos vectores.

Ejemplos:

    producto_escalar([2,5,3], [4,6,7]) => 59
letras_en_palabras: Recibe una lista de letras y una cadena. La lista contiene en cada índice de la misma una letra (string de longitud 1). 
Retorna True en caso de que todas las letras se encuentren en la palabra, False en caso contrario.

Ejemplos:

    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => False """

def filtrar_pares(lista):
    lista_final = []
    for numero in lista:
        if numero % 2 == 0:
            lista_final.append(numero)
    return lista_final

def filtrar_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos

def es_primo(numero):
    condicion = False
    if(numero == 2):
        condicion = True
    elif(numero > 2):
        for i in range(2, numero):
            if (numero % i == 0):
                break
        if (i+1 == numero):
            condicion = True
    return condicion

def sumar_elementos(lista):
    contador = 0
    for numero in lista:
        contador = contador + numero
    return contador
#print(sumar_elementos([5,6,13,7,11,9,10,11]))

def esta_ordenada(lista):
    ordenada = False
    if lista == sorted(lista):
        ordenada = True
    else:
        ordenada
    return ordenada
#print(esta_ordenada([5,6,13,7,11,9,10,11]))
    
def producto_escalar(vector_1, vector_2):
    componente_1 = vector_1[0] * vector_2[0]
    componente_2 = vector_1[1] * vector_2[1]
    componente_3 = vector_1[2] * vector_2[2]
    sumatoria = componente_1 + componente_2 + componente_3
    return sumatoria
#print(producto_escalar([2,5,3], [4,6,7]))
    

def letras_en_palabra(letras, frase):
    incluidas = False
    lista_fantasma = []
    for letra in letras:
        if letra in frase:
            lista_fantasma.append(letra)
            if len(lista_fantasma) == len(letras):
                incluidas = True
    else:
        incluidas
    return incluidas
print(letras_en_palabra(["a","h","e"], "hola como estas"))

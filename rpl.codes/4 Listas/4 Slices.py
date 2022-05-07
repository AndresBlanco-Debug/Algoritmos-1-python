"""Para este apartado, se propone la utilización de la funcionalidad de slices de indexación aplicada a listas.

ultimos_tres_elementos: Recibe una lista previamente inicializada, de longitud mayor o igual a 3. Retorna una lista con los últimos tres elementos de la que se recibi.

Ejemplo:

ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]) => [6,4,7]
ultimos_tres_elementos_concatenados: Recibe una lista de listas. Retorna una única lista que tiene concatenados los últimos tres elementos de cada una de las listas individuales en el orden original.

Ejemplo:

ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) => [2,3,4, 6,7,8,10,11,12]
indices_pares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices pares de la lista que recibió como parámetro.

Hint: Recordar que los índices comienzan en 0.

Ejemplo:

indices_pares(["a","b","c","d","e"]) -> ["a","c","e"]
indices_impares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices impares de la lista que recibió como parámetro.

Ejemplo:

indices_pares(["a","b","c","d","e", "f"]) -> ["b","d","f"]
invertir: Recibe una lista previamente inicializada. Retorna dicha lista invertida.

Ejemplo:

invertir([1,2,3,4,5]) => [5,4,3,2,1]"""

from operator import invert


def ultimmos_tres_elementos(lista):
    return lista[-3::]
#print(ultimmos_tres_elementos([5,3,6,2,5,32,6,4,7]))

def ultimos_tres_elementos_concatenados(lista):
    nueva_lista = []
    for mini_lista in lista:
        nueva_lista = nueva_lista + (mini_lista[-3::])
    return nueva_lista
#print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))

def indices_pares(lista):
    nueva_lista = []
    for elemento in lista:
        if lista.index(elemento) == 0:
            nueva_lista.append(elemento)
        elif lista.index(elemento) % 2 == 0:
            nueva_lista.append(elemento)
    return nueva_lista
#print(indices_pares(["a","b","c","d","e"]))

def indices_impares(lista):
    nueva_lista = []
    for elemento in lista:
        if lista.index(elemento) % 2 != 0:
            nueva_lista.append(elemento)
    return nueva_lista
#print(indices_impares(["a","b","c","d","e","f"]))

def invertir(lista):
    return sorted(lista,reverse= True)
#print(invertir([1,2,3,4,5]))

"""La idea de esta sección es completar las distintas funciones de acuerdo a los requerimientos especificados para cada una de ellas, tal como se hizo para el resto del módulo de listas.

filtrar_primos: Recibe una lista de números enteros y un número adicional. 
Retorna una nueva lista filtrada, que contiene aquellos números que sean primos y además sean mayores al segundo número que se recibió como parámetro.

HINT: Pueden utilizar la función es_primo(), correspondiente al módulo de funciones.

Ejemplos:

    filtrar_primos([3, 7, 11, 13], 8) => [11, 13]
    filtrar_primos([11, 7, 3, 19], 15) => [19]
ordenar_por_longitud_de_tuplas: Recibe una lista de tuplas. Retorna una nueva lista ordenada de mayor a menor por la longitud de las mismas. Aclaración: No importa el tipo de los elementos que se encuentran contenidos en las tuplas.

Ejemplo:

    lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
    ordenar_por_longitud_de_tuplas(lista_tuplas) => [("asd", 9, 5.6, "l", "s"), (6,4,5,6), (1,5,6), (1,2), (1,)]
concatenar_primeros_elementos: Recibe una lista de lista de listas. Se puede asumir que cada una de las listas internas tiene una longitud mayor a 3. Retorna una única lista, que resulta de la concatenación de los primeros 2 elementos de cada una de las listas internas, en el orden original.

Ejemplo:

    lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
    concatenar_primeros_elementos(lista) => [1,4,2,3,6,4,5,6]"""

def es_primo(numero):
    primo = False
    if numero == 2:
        primo = True
    elif numero > 2:
        for num in range(2,numero):
            if numero % num == 0:
                primo
                break
        else:
            primo = True
    return primo

def filtrar_primos(numeros, menor_numero):
    lista_final = []
    for numero in numeros:
        if es_primo(numero) == True and numero > menor_numero:
            lista_final.append(numero)
    return lista_final
#print(filtrar_primos([3, 7, 11, 13], 8))

def ordenar_por_longitud_de_tuplas(tuplas):
    return sorted(tuplas,key=len,reverse= True)
#print(ordenar_por_longitud_de_tuplas([(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]))

def concatenar_primeros_elementos(lista):
    nueva_lista = []
    for mini_lista in lista:
        nueva_lista = nueva_lista + (mini_lista[0:2])
    return nueva_lista
#print(concatenar_primeros_elementos([[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]))

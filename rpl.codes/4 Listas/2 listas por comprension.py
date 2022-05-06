"""Los distintos ejercicios propuestos en este apartado fueron pensados para ser resueltos utilizando listas por compresión. Correr un test para probar una función solamente implica testear el resultado; esto significa que un test puede pasar sin que los ejercicios sean resueltos utilizando listas por comprensión y realizando simples iteraciones sobre las listas. Esta claro que no deben hacer esto último, recuerden que los docentes pueden ver el código que envían. Confiamos en su honestidad y responsabilidad.

numeros_positivos: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos(5) => [1,2,3,4,5]
numeros_positivos_pares: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos pares hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos_pares(7) => [2,4,6]
numeros_positivos_pares_cuadrado: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos PARES elevados al cuadrado hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos_pares(7) => [4,16,36]
impares_al_cuadrado: Recibe una lista de enteros positivos. Retorna una nueva lista donde los números impares están elevados al cuadrado, mientras que los pares se conservan sin sufrir ninguna modificación.

Ejemplo:

    impares_al_cuadrado([1,2,3,4,5,6,7]) => [1,2,9,4,25,6,49]
filtrar_tuplas_por_suma: Recibe una lista de tuplas de longitud 2 que contiene un número entero en cada índice. Retorna una nueva lista que contiene únicamente a aquellas tuplas que, al sumar sus dos elementos, el resultado sea positivo (mayor o igual a 0). Se debe conservar el orden original.

Ejemplo:

    filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]) => [(7, -5),(1, 2)]
filtrar_tupla_elemento_par: Recibe una lista de tuplas de longitud 2 que contiene un número entero en cada índice. Retorna una nueva lista que contiene ínicamente aquellas tuplas que contengan al menos un numero par, conservando el orden original.

Ejemplo:

    filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]) => [(4, 5),(1, 2), (4,2)]"""
    
def numeros_positivos(numero):
    return[x for x in range(1,numero+1) if x > 0 ]
#print(numeros_positivos(5))

def numeros_positivos_pares(numero):
    return[x for x in range(1,numero+1) if x > 0 and x % 2 == 0]
#print(numeros_positivos_pares(7))

def numeros_positivos_pares_cuadrados(numero):
    return[x**2 for x in range(1,numero+1) if x % 2 == 0]
#print(numeros_positivos_pares_cuadrados(6))

def impares_al_cuadrados(lista):
    return[x if x % 2 == 0 else x**2 for x in lista ]
#print(impares_al_cuadrados([1,2,3,4,5,6,7]))

def filtrar_tuplas_por_suma(lista_de_tuplas):
    return [x for x in lista_de_tuplas if sum(x)>0]
#print(filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]))

def filtrar_tupla_elemento_par(lista_de_tuplas):
    return [lista_de_tuplas[x] for x in range(len(lista_de_tuplas)) if lista_de_tuplas[x][0] % 2 == 0 or lista_de_tuplas[x][1] % 2 == 0]
#print(filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]))

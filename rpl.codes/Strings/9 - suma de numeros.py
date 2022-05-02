"""Completar el cuerpo de la función. La misma recibe una cadena como parámetro y debe retornar el resultado de sumar todos los caracteres numéricos que aparezcan en la misma.

Ejemplo:

    sumar_caracteres_numericos("1") => 1
    sumar_caracteres_numericos("a1") => 1
    sumar_caracteres_numericos("12") => 3
    sumar_caracteres_numericos("123") => 6
    sumar_caracteres_numericos("o1la293fr") => 1 + 2 + 9 + 3 = 15"""

def sumar_caracteres_numericos(cadena):

    abecedario = "abcdefghijklmnopqrstuvwxyz" 
    lista_numerica = ""
    lista_final = []
    
    for letra in cadena.lower(): 
      
        if letra in abecedario:
            cadena = cadena.replace(letra,"")
            cadena = cadena.replace(" ","")
            lista_numerica = list(cadena)
        elif letra not in abecedario:
            lista_numerica = list(cadena)
            
    for numero in lista_numerica:
        lista_final.append(int(numero))
    #print(lista_final)
    return sum(lista_final)

print(sumar_caracteres_numericos("12asd 3"))


"""Completar el cuerpo de la función. La misma debe retornar valor un valor booleano: True en caso de que la contraseña sea válida, False en caso contrario.
Se considera válida una contraseña si:

Tiene al menos un número.
Tiene al menos una mayúscula.
Tiene al menos un caracter no alfanumérico
(Hint: Se puede evaluar utilizando la conjunción de la negación entre .isalpha() y
la negación de .isnumeric())
Tiene una longitud mayor a 7 caracteres pero menor a 15.
Ejemplo:

   validar_contraseña("!Algoritmos123") => True
   validar_contraseña("!Algoritmos123!Algoritmos123") => False
   validar_contraseña("algoritmos") => False
   validar_contraseña("algoritmos123") => False
   validar_contraseña("Algoritmos123") => False
   validar_contraseña("!Alg123") => False"""

def validar_contrasenia(contrasenia):
    es_valida = False
    caracter_raro = False
    cumple = False
    caracter_especial = "!@#$%^&*()_-.;:"
        
    if len(contrasenia) > 7 and len(contrasenia) < 15:
        for caracter in caracter_especial:
            if caracter in contrasenia:
                caracter_raro = True
            else:
                caracter_raro
            if contrasenia.islower() or  contrasenia.isupper() or contrasenia.isdigit() or contrasenia.isalpha():
                es_valida
            else: es_valida = True 
    if es_valida == True and caracter_raro == True:
        cumple = True
    return cumple
print(validar_contrasenia("Algoritmos123"))

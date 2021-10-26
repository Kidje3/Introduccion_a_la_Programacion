#ejercicio 4

##  Hacer una función que reciba una cadena y retorne un entero calculado de la siguiente forma:
##  Cada vocal en minúscula suma 1 punto, cada vocal en mayúscula suma 2 puntos y si contiene consonantes poco
##  frecuentes como q,k,x,y,z, sin importar mayúsculas o minúsculas, suma 10 puntos. Cualquier otra consonante
##  suma 4 puntos. Ejemplo: Axioma = 2+10+1+1+4+1 Devuelve: 19

# vocal      =  1 puntos
# vocal May  =  2 puntos
# q,k,x,y,z  = 10 puntos
# resto cons =  4 puntos

def valorSuma(cadena):
    puntaje=0
    vocal="aeiou"
    vocMay="AIEOU"
    pocofrec="qkxyzQKXYZ"
    for char in cadena:
        if char in pocofrec:
            puntaje=puntaje+10
        elif char in vocMay:
            puntaje=puntaje+2
        elif char in vocal:
            puntaje=puntaje+1
        else:
            puntaje=puntaje+4
    return puntaje

cadena="Axioma"

print(valorSuma(cadena))

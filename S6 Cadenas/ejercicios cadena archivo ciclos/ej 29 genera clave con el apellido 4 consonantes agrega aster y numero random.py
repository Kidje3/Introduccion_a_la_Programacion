
# ejercicio 29 de cadenas:  se le pide  un apellido, se toman las primeras 4 consonantes
# y va generando en una nueva cadena , si no llega a las 4 consonantes completa con asteriscos
# y luego le agrega un numero aleatorio al final.


import random


apellido= input("Ingrese su apellido")
vocales="aeiou"
nueva=""


# aca lo que hace es recorre el apellido, si no es vocal crea una nueva cadena hasta 4 letras.
for letra in apellido:
    if letra not in vocales:  # o sea si es una consonante
        if len (nueva) < 4:
            nueva= nueva + letra

# si la nueva cadena es menor a 4 caracteres hay que agregar asteriscos
if len (nueva) < 4:      # hay que agregar
    cantAsteriscos = 4 - len(nueva)
    nueva= nueva + "*" * cantAsteriscos

# genero un numero azar para sumarlo al final de la nueva cadena.
azar=  random.randrange(10)

print ( nueva + str (azar))


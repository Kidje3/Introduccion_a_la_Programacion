# ejercicio de los parciales, donde pide un apellido y debe imprimir si hay mas consonantes o vocales
# imprime lo que haya mas, y completar con la cantidad "len" de lo que no elegimos.


import random

apellido= input  ("ingrese su apellido")

vocales="aeiou"
lasVocales=""
lasConsonantes=""


for letra in apellido:       #recorremos las letras del apellido
    if letra in vocales:
        lasVocales = lasVocales + letra.upper()   # si esas letras que encuentra estan en "vocales" sumarla a la cadena "las vocales"
    else:
        lasConsonantes= lasConsonantes + letra.upper()  # si no estan en vocales, sumarla en consonantes

if len(lasVocales) < len (lasConsonantes):      # ahora lo que hacemos es, si la cantidad de vocales es menor a consonante
    print (lasConsonantes + str ( len( lasVocales)))   #imprimir consonantes + len de las vocales
else:
    if len(lasVocales) > len (lasConsonantes):       # caso contrario hacer lo opuesto
        print (lasVocales + str ( len( lasConsonantes)))
    else:                                             # y si no se cumple tampoco, significa que son = por lo tanto  armo un azar
        azar= random.randint(1,10)
        if azar <=5:                                    # luego en el azar elijo si imprimo una u otra segun el parametro.
            print (lasVocales + str ( len( lasConsonantes)))
        else:
             print (lasConsonantes + str ( len( lasVocales)))







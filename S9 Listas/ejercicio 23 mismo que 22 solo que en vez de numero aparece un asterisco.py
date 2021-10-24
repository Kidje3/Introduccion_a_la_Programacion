# ejercicio  23

##  Modificar el programa del ejercicio 22 para que muestre visualmente los resultados, repitiendo
##  asteriscos. Ej:

def cantApariciones(letra,cadena):
    cont=0
    for elem in cadena:
        if letra == elem:
            cont=cont+1

    return cont*"*"

# en esta otra parte,  recorre la cadena, si no esta la agrega en una lista nueva
# y llama a la funcion para decirnos cuantas veces aparece.
# en otra lista nueva agrega la letra  y la cantidad.
def buscarletras(cadena):
    letrasRecorridas= []
    lista=[]
    for letra in cadena:
        if letra not in letrasRecorridas:
            letrasRecorridas.append(letra)
            cantidad= cantApariciones(letra,cadena)
            lista.append([letra,cantidad])
    return lista

cadena="conocidos"

for arreglo in buscarletras(cadena):
    print(arreglo)
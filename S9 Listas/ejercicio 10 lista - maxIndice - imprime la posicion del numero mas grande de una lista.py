# ejercicio 10

## Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
## índice del máximo elemento.

def maxIndice (lista):
    maximo=lista[0]
    for i in range (len(lista)):
        if lista[i] > maximo:
            maximo=lista[i]
    for i in range (len(lista)):
        if lista[i] == maximo:
            print (i)
lista=[3,1,20,5,7,12,100]
maxIndice(lista)


# ejercicio 9

##Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
##máximo elemento.

def maxElemento (lista):
    maximo=lista[0]
    for i in range (len(lista)):
        if lista[i] > maximo:
            maximo=lista[i]
    return maximo



lista=[3,1,3,5,7,20,12]
print(maxElemento(lista))

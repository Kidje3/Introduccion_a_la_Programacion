# ejercicio 20

##  a) Definir una función que tome una lista de números s y un número decimal x y
##     devuelva la cantidad de elementos de s que sean menores que x.
##  b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¿cómo
##     podría modificarse el programa para que haga menos iteraciones?


# a:  recorro la lista, si cada elemento del recorrido es menor a x lo agrega en la lista nueva.

def elementosX (lista,x):
    nueva=[]
    for i in range (len(lista)):
        if lista[i]< x:
            nueva.append(lista[i])

    return nueva

s=[21,14,3,54,20,7,9,13]
x= 18
#print(elementosX(s,x))


# b:  para resolver esto uso la funcion de ordenar listas:

######################################################
def ordenarMayaMenor (lista):
    for recorrido in range (1,len(lista)):
        for posicion in range (len(lista) - recorrido):
            if lista[posicion] < lista [posicion +1 ]:
                aux=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion + 1 ]= aux
    return lista

#######################################################

def elementosX (lista,x):
    nueva=[]
    for i in range (len(lista)):
        if lista[i]< x:
            nueva.append(lista[i])
    ordenarMayaMenor(nueva)
    return nueva

print(elementosX(s,x))




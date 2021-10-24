# ejercicio 11

##  Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
##  menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
##  los que están entre el índice a y el índice b.

# esta es la misma funcion que Maximo de pero ahora entre en una lista acotada entre 2 numeros

##def maximoEntre (lista,a,b):
##    maximo=lista[0]
##    for i in range ((len(lista)-b-1),(len(lista)-a)):
##        if lista[i] > maximo:
##            maximo=lista[i]
##    for i in range (len(lista)):
##        if lista[i] == maximo:
##            print (i)


##lista=[3,12,5,700,80,5,21,14,100]
##a=2
##b=6
##maximoEntre(lista,a,b)


def maxElemento (lista):
    maximo=lista[0]
    for i in range (len(lista)):
        if lista[i] > maximo:
            maximo=lista[i]
    return maximo

def maximoEntre (lista, a, b):
    nueva=[]
    for i in range ((len(lista)-b-1),(len(lista)-a)):
        nueva.append(lista[i])
    maxim=maxElemento(nueva)
    return maxim

lista=[3,12,5,700,80,5,21,14,100]
a=2
b=6
print(maximoEntre(lista,a,b))





